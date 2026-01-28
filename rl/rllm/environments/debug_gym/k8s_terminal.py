"""
Kubernetes Terminal for Debug-Gym

提供Kubernetes Pod作为执行环境的Terminal实现。
"""
import logging
import os
import re
import shlex
import subprocess
import tempfile
from pathlib import Path
from typing import Any

logger = logging.getLogger(__name__)

try:
    from kubernetes import client, config
    from kubernetes.stream import stream
    KUBERNETES_AVAILABLE = True
except ImportError:
    KUBERNETES_AVAILABLE = False
    logger.warning("Kubernetes Python client not available. K8s support disabled.")

try:
    from debug_gym.gym.terminal import DockerTerminal, Terminal
    from debug_gym.logger import DebugGymLogger
except ImportError:
    Terminal = None
    DockerTerminal = None
    DebugGymLogger = None


DEFAULT_NAMESPACE = "default"
CMD_TIMEOUT = 60
DEFAULT_PS1 = "DEBUG_GYM_PS1"

# Shell 内置命令和特殊语法，需要用 bash -c 包装
SHELL_BUILTINS = {
    'source ', 'conda ', 'export ', 'alias ', 'ulimit ',
    'set ', 'unset ', 'declare ', 'typeset ', 'readonly ',
    'local ', '. ',  # 点命令是 source 的简写
    'pyenv ', 'nvm ', 'rbenv ',  # 环境管理工具
}

# Bash 特有功能
BASH_FEATURES = {
    '<(',  # 进程替换
    '>(',  # 进程替换
    '[[',  # bash 的测试语法（双方括号）
}


def needs_bash_wrapper(command: str) -> bool:
    """
    检查命令是否需要 bash -c 包装。
    
    某些命令是 shell 内置命令或使用了 bash 特有功能，
    在 /bin/sh 中可能不可用或行为不同，需要用 bash -c 包装。
    
    Args:
        command: 要检查的命令字符串
        
    Returns:
        bool: True 表示需要 bash -c 包装
    """
    # 检查 shell 内置命令
    for builtin in SHELL_BUILTINS:
        if builtin in command:
            return True
    
    # 检查 bash 特有功能
    for feature in BASH_FEATURES:
        if feature in command:
            return True
    
    return False


class K8sShellSession:
    """
    Kubernetes Shell会话，模拟debug-gym的ShellSession。
    
    使用subprocess + kubectl run -i --tty创建真正的交互式会话。
    这样可以支持PDB等需要持久状态的工具。
    """
    
    def __init__(
        self,
        pod_name: str,
        namespace: str,
        core_v1,
        working_dir: str,
        session_commands: list[str] | None = None,
        env_vars: dict[str, str] | None = None,
        logger: Any | None = None,
        image: str = "python:3.12",  # 会话使用的镜像
    ):
        self.pod_name = pod_name
        self.namespace = namespace
        self.core_v1 = core_v1
        self.working_dir = working_dir
        self.session_commands = session_commands or []
        self.env_vars = env_vars or {}
        self.logger = logger or logging.getLogger(__name__)
        self.image = image
        
        # 确保有PS1用于读取
        if not self.env_vars.get("PS1"):
            self.env_vars["PS1"] = DEFAULT_PS1
        
        self.default_read_until = self.env_vars["PS1"]
        self._session_id = str(os.urandom(4).hex())
        self.session_pod_name = f"{pod_name}-session-{self._session_id}"
        
        # PTY文件描述符（用于交互）
        self.filedescriptor = None
        self.process = None
    
    @property
    def is_running(self):
        """会话是否运行中"""
        return self.process is not None and self.process.poll() is None
    
    def start(self, command=None, read_until=None):
        """
        启动交互式会话。
        
        利用主Pod的tty: True特性，使用kubectl exec -it创建交互式会话。
        """
        self.close()  # 关闭已有会话
        
        # 准备命令
        if command:
            full_command = " && ".join(self.session_commands + [command])
        else:
            full_command = "bash"
        
        # 使用kubectl exec -it连接到主Pod的TTY
        # 主Pod已经设置了tty: True, stdin: True
        kubectl_cmd = [
            "kubectl", "exec",
            "-it",  # 交互式 + TTY
            self.pod_name,  # 使用主Pod，不创建新Pod！
            f"--namespace={self.namespace}",
            "--",
            "/bin/bash", "-c",
            f"cd {self.working_dir} && {full_command}"
        ]
        
        self.logger.debug(f"Starting K8s interactive session: {kubectl_cmd}")
        
        # 使用PTY启动进程（类似ShellSession）
        import pty
        import fcntl
        import termios
        
        server, client = pty.openpty()
        self.filedescriptor = server
        
        # 设置非阻塞
        flags = fcntl.fcntl(server, fcntl.F_GETFL)
        fcntl.fcntl(server, fcntl.F_SETFL, flags | os.O_NONBLOCK)
        
        # 关闭echo
        attrs = termios.tcgetattr(client)
        attrs[3] = attrs[3] & ~termios.ECHO
        termios.tcsetattr(client, termios.TCSANOW, attrs)
        
        # 启动kubectl exec -it进程
        self.process = subprocess.Popen(
            kubectl_cmd,
            stdin=client,
            stdout=client,
            stderr=client,
            close_fds=True,
        )
        
        os.close(client)
        
        # 读取初始输出
        output = self.read(read_until=read_until, timeout=60)
        
        if not self.is_running:
            self.close()
            raise RuntimeError(f"K8s session failed to start. Output:\n{output}")
        
        return output
    
    def read(self, read_until: str | None = None, timeout: int | None = None) -> str:
        """读取输出直到指定字符串"""
        import time
        import errno
        
        read_until = read_until or self.default_read_until
        timeout = timeout or 300
        
        output = ""
        start_time = time.time()
        
        while True:
            if time.time() - start_time > timeout:
                raise TimeoutError(f"Read timeout after {timeout}s. Output: {output}")
            
            try:
                data = os.read(self.filedescriptor, 4096).decode("utf-8", errors="ignore")
                if data:
                    output += data
                    if read_until and read_until in output:
                        break
                else:
                    time.sleep(0.01)
            except BlockingIOError:
                time.sleep(0.1)
            except OSError as e:
                if e.errno == errno.EIO:
                    break
                if e.errno != errno.EAGAIN:
                    raise
        
        # 清理输出
        output = re.sub(r"\x1b\[[0-9;]*m|\r", "", output)
        if read_until:
            output = output.replace(read_until, "")
        return output.strip()
    
    def run(self, command: str, read_until: str | None = None, timeout: int | None = None):
        """
        在会话中运行命令（发送到PTY）。
        """
        if not self.is_running:
            raise RuntimeError("Session not running")
        
        self.logger.debug(f"K8sSession running: {command}")
        
        # 写入命令到PTY
        os.write(self.filedescriptor, command.encode("utf-8") + b"\n")
        
        # 读取输出
        try:
            output = self.read(read_until=read_until, timeout=timeout)
        except TimeoutError as e:
            self.close()
            raise
        
        return output
    
    def close(self):
        """关闭会话"""
        if self.filedescriptor is not None:
            self.logger.debug(f"Closing K8sShellSession[{self._session_id}]")
            try:
                os.close(self.filedescriptor)
            except OSError:
                pass
            self.filedescriptor = None
        
        if self.process:
            try:
                self.process.terminate()
                self.process.wait(timeout=5)
            except:
                try:
                    self.process.kill()
                except:
                    pass
            self.process = None
    
    def __str__(self):
        return f"K8sShell[{self._session_id}, Pod:{self.session_pod_name}]"
    
    def __del__(self):
        try:
            self.close()
        except:
            pass


class KubernetesTerminal(DockerTerminal if DockerTerminal else object):
    """
    Kubernetes Terminal实现，使用K8s Pod作为执行环境。
    
    继承自DockerTerminal以确保完全兼容SWEBenchEnv的类型检查。
    使用Kubernetes Pod而不是Docker容器执行命令。
    
    参考r2egym的DockerRuntime实现了生产级特性：
    - Watch监控Pod状态
    - 重试机制和指数退避
    - 线程池执行+超时控制
    - Tar over exec文件传输
    - 自动配置pip镜像源
    """
    
    def __init__(
        self,
        pod_name: str | None = None,
        namespace: str = DEFAULT_NAMESPACE,
        image: str = "python:3.12",
        base_image: str | None = None,  # 兼容DockerTerminal参数
        kubeconfig: str | None = None,
        working_dir: str | None = None,
        session_commands: list[str] | None = None,
        env_vars: dict[str, str] | None = None,
        include_os_env_vars: bool = False,
        setup_commands: list[str] | None = None,
        pip_mirror: str | None = "https://mirrors.zju.edu.cn/pypi/web/simple",  # 默认使用ZJU镜像
        apt_mirror: str | None = "mirrors.zju.edu.cn",  # 默认使用ZJU apt镜像
        logger: Any | None = None,
        **kwargs
    ):
        """
        初始化Kubernetes Terminal。
        
        Args:
            pod_name: Pod名称（如果为None，会自动生成）
            namespace: Kubernetes命名空间
            image: 容器镜像
            base_image: 基础镜像（兼容DockerTerminal，优先使用）
            kubeconfig: kubeconfig文件路径（None使用默认）
            working_dir: 工作目录
            session_commands: 会话命令列表
            env_vars: 环境变量字典
            include_os_env_vars: 是否包含OS环境变量（兼容DockerTerminal）
            setup_commands: 设置命令列表
            pip_mirror: PyPI镜像源URL（None表示不配置，默认使用ZJU镜像）
            apt_mirror: apt镜像源域名（None表示不配置，默认使用ZJU镜像）
            logger: 日志记录器
            **kwargs: 其他参数
        """
        if not KUBERNETES_AVAILABLE:
            raise ImportError(
                "Kubernetes Python client not installed. "
                "Install with: pip install kubernetes"
            )
        
        # 不调用super().__init__以避免DockerTerminal的初始化
        # 直接初始化我们需要的属性
        self.pod_name = pod_name or self._generate_pod_name()
        self.namespace = namespace
        self._base_image = base_image or image  # 内部存储
        self.image = self._base_image  # 优先使用base_image（SWE-bench会设置）
        self._working_dir = working_dir or "/workspace"
        self.session_commands = session_commands or []
        self.env_vars = env_vars or {}
        self.include_os_env_vars = include_os_env_vars
        self.setup_commands = setup_commands or []
        self.pip_mirror = pip_mirror
        self.apt_mirror = apt_mirror
        self.logger = logger or logging.getLogger(__name__)
        self._pod = None
        
        # 模拟DockerTerminal的属性
        self.docker_client = None  # 不需要，但为了兼容性
        self._container = None  # 会通过property映射到_pod
        self._sessions = []  # Shell会话列表
        
        # 初始化Kubernetes客户端
        if kubeconfig:
            config.load_kube_config(config_file=kubeconfig)
        else:
            try:
                config.load_incluster_config()
            except config.ConfigException:
                config.load_kube_config()
        
        self.core_v1 = client.CoreV1Api()
    
    @property
    def working_dir(self):
        """获取工作目录。"""
        return self._working_dir
    
    @working_dir.setter
    def working_dir(self, value):
        """设置工作目录（兼容SWEBenchEnv）。"""
        self._working_dir = value
    
    @property
    def base_image(self):
        """获取基础镜像。"""
        return self._base_image
    
    @base_image.setter
    def base_image(self, value):
        """设置基础镜像，同时同步更新image属性。"""
        self._base_image = value
        self.image = value  # 保持image和base_image同步，确保Pod使用正确的镜像
    
    @property
    def pod(self):
        """延迟初始化Pod（兼容DockerTerminal.container的延迟初始化）。"""
        if self._pod is None:
            self._setup_pod()
        return self._pod
    
    @property
    def container(self):
        """别名，兼容DockerTerminal.container接口。"""
        return self.pod
    
    @container.setter
    def container(self, value):
        """设置container（映射到pod）。"""
        self._pod = value
    
    def _generate_pod_name(self) -> str:
        """生成唯一的Pod名称。"""
        import uuid
        return f"debug-gym-{uuid.uuid4().hex[:8]}"
    
    def setup_container(self):
        """
        创建并返回Pod（兼容DockerTerminal.setup_container接口）。
        """
        if self._pod is None:
            self._setup_pod()
        return self._pod
    
    def _setup_pod(self):
        """
        创建并启动Pod。
        
        参考r2egym的_start_kubernetes_pod实现：
        - 使用watch高效监控Pod状态
        - 重试机制处理API限流
        - 详细的资源配置
        """
        # 构建环境变量列表（添加PATH）
        from kubernetes import watch
        
        DOCKER_PATH = "/root/.venv/bin:/root/.local/bin:/root/.cargo/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
        env_vars_merged = {"PATH": DOCKER_PATH, **self.env_vars}
        env_list = [{"name": k, "value": str(v)} for k, v in env_vars_merged.items()]
        
        pod_manifest = {
            "apiVersion": "v1",
            "kind": "Pod",
            "metadata": {
                "name": self.pod_name,
                "namespace": self.namespace,
                "labels": {
                    "app": "debug-gym",
                    "component": "terminal",
                    "type": "swe-bench"
                }
            },
            "spec": {
                "restartPolicy": "Never",
                "hostNetwork": True,  # 与宿主机共享网络
                "containers": [{
                    "name": self.pod_name,  # 容器名=Pod名（兼容r2egym）
                    "image": self.image,
                    "command": ["/bin/sh", "-c"],
                    "args": ["sleep infinity"],  # 保持Pod运行
                    "stdin": True,  # 支持交互
                    "tty": True,
                    "env": env_list,
                    "resources": {
                        "requests": {
                            "cpu": "1",  # r2egym的配置
                            "memory": "2Gi"
                        },
                        "limits": {
                            "memory": "4Gi",
                            "cpu": "2"
                        }
                    }
                }],
                # 可选：添加imagePullSecrets（如果需要私有仓库）
                # "imagePullSecrets": [{"name": "dockerhub-pro"}],  # 注释掉：secret不存在时会导致警告
                "nodeSelector": {"karpenter.sh/nodepool": "bigcpu-standby"},
                "tolerations": [
                    {
                        "key": "node.kubernetes.io/disk-pressure",
                        "operator": "Exists",
                        "effect": "NoExecute",
                        "tolerationSeconds": 10800
                    },
                    {
                        "key": "node-role.kubernetes.io/control-plane",
                        "operator": "Exists",
                        "effect": "NoSchedule"
                    }
                ],
            }
        }
        
        # 使用重试机制创建Pod（参考r2egym）
        max_retries = 5
        backoff = 5  # seconds
        pod = None
        
        for attempt in range(1, max_retries + 1):
            try:
                self.logger.info(
                    f"Creating Pod: {self.pod_name} with image: {self.image} "
                    f"(attempt {attempt}/{max_retries})"
                )
                pod = self.core_v1.create_namespaced_pod(
                    namespace=self.namespace,
                    body=pod_manifest,
                    _request_timeout=120
                )
                break  # 成功
            except client.ApiException as e:
                # 重试API限流或临时错误
                if e.status in (409, 429, 500, 503):
                    self.logger.warning(
                        f"Transient K8s error {e.status} creating pod '{self.pod_name}' "
                        f"(attempt {attempt}/{max_retries}); retrying in {backoff}s"
                    )
                    import time
                    time.sleep(backoff)
                    backoff = min(backoff * 2, 60)  # 指数退避
                    continue
                # 非重试错误 → 抛出
                self.logger.error(f"Failed to create Pod '{self.pod_name}': {e}")
                raise
        else:
            raise RuntimeError(
                f"Exceeded retry limit ({max_retries}) creating pod '{self.pod_name}'"
            )
        
        # 立即保存pod引用
        self._pod = pod
        
        # 使用watch高效监控Pod状态（参考r2egym）
        try:
            rv = pod.metadata.resource_version
            w = watch.Watch()
            stream_events = w.stream(
                self.core_v1.list_namespaced_pod,
                namespace=self.namespace,
                field_selector=f"metadata.name={self.pod_name}",
                resource_version=rv,
                timeout_seconds=600,  # 10分钟超时
            )
            
            import time
            start_time = time.time()
            
            for event in stream_events:
                obj = event["object"]
                phase = obj.status.phase
                
                if time.time() - start_time > 600:
                    w.stop()
                    raise RuntimeError(f"Pod '{self.pod_name}' timed out after 600s")
                
                self.logger.debug(f"Event {event['type']} → pod.phase={phase}")
                
                if phase == "Running":
                    # self.logger.info(f"Pod '{self.pod_name}' is Running")
                    # w.stop()
                    # break
                    # 检查容器是否就绪
                    container_statuses = obj.status.container_statuses
                    if container_statuses and all(c.ready for c in container_statuses):
                        self.logger.info(f"Pod '{self.pod_name}' is Running and Ready")
                        w.stop()
                        break
                    else:
                        # Pod 在 Running 但容器未就绪，继续等待
                        self.logger.debug(f"Pod '{self.pod_name}' is Running but containers not ready yet")
                
                if phase in ["Failed", "Succeeded", "Unknown"]:
                    w.stop()
                    raise RuntimeError(
                        f"Pod '{self.pod_name}' entered terminal phase '{phase}'"
                    )
            
        except client.ApiException as e:
            self.logger.error(f"Failed to watch Pod '{self.pod_name}': {e}")
            raise
        except Exception as e:
            # Watch超时或其他错误，直接检查Pod状态
            self.logger.warning(f"Error watching pod: {e}, checking status directly")
            try:
                pod_status = self.core_v1.read_namespaced_pod(
                    name=self.pod_name,
                    namespace=self.namespace,
                    _request_timeout=60
                )
                if pod_status.status.phase == "Running":
                    self.logger.info(
                        f"Pod '{self.pod_name}' is running (verified after watch error)"
                    )
                    self._pod = pod_status
                else:
                    raise RuntimeError(
                        f"Pod '{self.pod_name}' in state {pod_status.status.phase}"
                    )
            except Exception as status_error:
                self.logger.error(f"Failed to check pod status: {status_error}")
                raise
        
        # 确保工作目录存在（直接执行，不通过run()避免循环）
        # self.logger.info(f"Ensuring working directory exists: {self.working_dir}")
        # try:
        #     exec_command = ["/bin/sh", "-c", f"mkdir -p {self.working_dir}"]
        #     resp = stream(
        #         self.core_v1.connect_get_namespaced_pod_exec,
        #         self.pod_name,
        #         self.namespace,
        #         command=exec_command,
        #         container=self.pod_name,
        #         stderr=True,
        #         stdin=False,
        #         stdout=True,
        #         tty=False,
        #         _preload_content=False,
        #     )
        #     resp.close()
        #     self.logger.info(f"✓ Working directory created: {self.working_dir}")
        # except Exception as e:
        #     self.logger.warning(f"Failed to create working directory: {e}")
        
        # 运行设置命令
        self._run_setup_commands()
        
        # 返回pod对象
        return self._pod
    
    def set_apt_mirror(self, mirror_host: str = "mirrors.zju.edu.cn"):
        """
        配置apt镜像源。
        
        支持不同Linux发行版：
        - Ubuntu 22.04+: /etc/apt/sources.list.d/ubuntu.sources (DEB822格式)
        - Ubuntu 20.04: /etc/apt/sources.list (传统格式)
        - Debian: /etc/apt/sources.list (Debian格式)
        
        Args:
            mirror_host: 镜像源主机名（如"mirrors.zju.edu.cn"）
        """
        try:
            # 检测发行版
            success, distro = self.run("cat /etc/os-release | grep '^ID=' | cut -d= -f2 | tr -d '\"'", timeout=10)
            distro = distro.strip().lower() if success else "unknown"
            
            self.logger.info(f"Detected distro: {distro}")
            
            # Ubuntu 22.04+ (DEB822格式)
            if distro == "ubuntu":
                success, _ = self.run("test -f /etc/apt/sources.list.d/ubuntu.sources", timeout=10)
                if success:
                    self.logger.info(f"Configuring apt mirror (Ubuntu DEB822): {mirror_host}")
                    cmd = f"sed -i 's@//.*archive.ubuntu.com@//{mirror_host}@g' /etc/apt/sources.list.d/ubuntu.sources"
                    success, output = self.run(cmd, timeout=30)
                    if success:
                        self.logger.info(f"✓ Apt mirror configured: {mirror_host} (update manually if needed)")
                        return
                
                # Ubuntu传统格式
                success, _ = self.run("test -f /etc/apt/sources.list", timeout=10)
                if success:
                    self.logger.info(f"Configuring apt mirror (Ubuntu traditional): {mirror_host}")
                    cmd = f"sed -i 's@//.*archive.ubuntu.com@//{mirror_host}@g' /etc/apt/sources.list"
                    success, output = self.run(cmd, timeout=30)
                    if success:
                        self.logger.info(f"✓ Apt mirror configured: {mirror_host} (update manually if needed)")
                        return
            
            # Debian
            elif distro == "debian":
                # Debian 12+ (DEB822格式)
                success, _ = self.run("test -f /etc/apt/sources.list.d/debian.sources", timeout=10)
                if success:
                    self.logger.info(f"Configuring apt mirror (Debian 12+ DEB822): {mirror_host}")
                    cmd = f"sed -i 's@deb.debian.org@{mirror_host}/debian@g' /etc/apt/sources.list.d/debian.sources"
                    success, output = self.run(cmd, timeout=30)
                    if success:
                        self.logger.info(f"✓ Apt mirror configured: {mirror_host}/debian (update manually if needed)")
                        return
                
                # Debian传统格式
                success, _ = self.run("test -f /etc/apt/sources.list", timeout=10)
                if success:
                    self.logger.info(f"Configuring apt mirror (Debian traditional): {mirror_host}")
                    cmd = f"sed -i 's@deb.debian.org@{mirror_host}/debian@g' /etc/apt/sources.list"
                    success, output = self.run(cmd, timeout=30)
                    if success:
                        self.logger.info(f"✓ Apt mirror configured: {mirror_host}/debian (update manually if needed)")
                        return
                    else:
                        self.logger.warning(f"Failed to configure Debian mirror: {output}")
            
            # 未知发行版或无sources文件
            self.logger.info(f"Skipping apt mirror configuration for {distro} (sources file not found or not supported)")
                    
        except Exception as e:
            self.logger.warning(f"Failed to set apt mirror: {e}")
    
    
    def set_pip_mirror(self, mirror_url: str = "https://mirrors.zju.edu.cn/pypi/web/simple"):
        """
        配置pip镜像源（参考r2egym实现）。
        
        优先级：
        1. pip config set global.index-url
        2. python -m pip config set
        3. 写入 /root/.pip/pip.conf
        
        Args:
            mirror_url: 镜像源URL，默认使用浙江大学镜像
        """
        try:
            # 提取trusted host
            from urllib.parse import urlparse
            parsed = urlparse(mirror_url)
            trusted_host = parsed.netloc
            
            # 方法1: pip config (全局)
            success, output = self.run(
                f"pip config set global.index-url {mirror_url} && "
                f"pip config set global.trusted-host {trusted_host}",
                timeout=30
            )
            if success:
                self.logger.info(f"✓ Pip mirror configured via pip config: {mirror_url}")
                return
            
            # 方法2: python -m pip config (备用)
            success, output = self.run(
                f"python -m pip config set global.index-url {mirror_url} && "
                f"python -m pip config set global.trusted-host {trusted_host}",
                timeout=30
            )
            if success:
                self.logger.info(f"✓ Pip mirror configured via python -m pip: {mirror_url}")
                return
            
            # 方法3: 写入配置文件
            self.run("mkdir -p /root/.pip", timeout=10)
            pip_conf = f"""[global]
index-url = {mirror_url}
trusted-host = {trusted_host}
"""
            # 使用heredoc写入文件
            cmd = f"cat > /root/.pip/pip.conf << 'EOF'\n{pip_conf}\nEOF"
            self.run(cmd, timeout=10)
            self.logger.info(f"✓ Pip mirror configured via pip.conf: {mirror_url}")
            
        except Exception as e:
            self.logger.warning(f"Failed to set pip mirror: {e}")
    
    def _run_setup_commands(self):
        """
        运行设置命令（兼容DockerTerminal）。
        
        自动配置镜像源以加速包安装（参考r2egym）。
        """
        # 首先设置apt镜像源（如果配置了）
        if self.apt_mirror:
            self.logger.info(f"Configuring apt mirror: {self.apt_mirror}")
            self.set_apt_mirror(self.apt_mirror)
        
        # 然后设置pip镜像源（如果配置了）
        if self.pip_mirror:
            self.logger.info(f"Configuring pip mirror: {self.pip_mirror}")
            self.set_pip_mirror(self.pip_mirror)
        
        # 最后运行用户的setup命令
        for cmd in self.setup_commands:
            self.logger.info(f"Running setup command: {cmd}")
            success, output = self.run(cmd, timeout=300)
            if not success:
                self.logger.warning(f"Setup command failed: {cmd}\nOutput: {output}")
    
    def _wait_for_pod_ready_fallback(self, timeout: int = 300):
        """
        等待Pod就绪（备用方法，轮询方式）。
        仅在watch失败时使用。
        """
        import time
        start_time = time.time()
        
        while time.time() - start_time < timeout:
            try:
                pod = self.core_v1.read_namespaced_pod(
                    name=self.pod_name,
                    namespace=self.namespace
                )
                
                if pod.status.phase == "Running":
                    # 检查容器是否就绪
                    if pod.status.container_statuses:
                        if all(c.ready for c in pod.status.container_statuses):
                            return
                
                time.sleep(2)
            except Exception as e:
                self.logger.warning(f"Error checking Pod status: {e}")
                time.sleep(2)
        
        raise TimeoutError(f"Pod {self.pod_name} did not become ready within {timeout}s")
    
    def prepare_command(self, command: str | list[str]) -> str:
        """
        准备命令（兼容DockerTerminal接口）。
        
        Args:
            command: 命令字符串或列表
            
        Returns:
            准备好的命令字符串
        """
        if isinstance(command, list):
            command = " && ".join(command)
        
        # 添加session_commands（如conda activate等）
        if self.session_commands:
            all_commands = self.session_commands + [command]
            command = " && ".join(all_commands)
        
        return command
    
    def run(
        self,
        command: str | list[str],
        timeout: int = CMD_TIMEOUT,
        strip_output: bool = True,
        raises: bool = False
    ) -> tuple[bool, str]:
        """
        在Pod中执行命令。
        
        Args:
            command: 要执行的命令（字符串或列表）
            timeout: 超时时间（秒）
            strip_output: 是否清理输出
            raises: 失败时是否抛出异常
            
        Returns:
            (success, output) 元组
        """
        # 🔑 确保Pod已创建（延迟初始化）
        if self._pod is None:
            _ = self.pod  # 触发property，创建Pod
        
        # 准备命令
        prepared_command = self.prepare_command(command)
        
        # 检查后台执行
        if re.search(r'&\s*$', prepared_command):
            error_msg = "Error: Background execution ('&') is not supported."
            if raises:
                raise RuntimeError(error_msg)
            return False, error_msg
        
        # 构建完整命令（包含工作目录切换）
        # 注意：如果命令包含shell内置命令或bash特有功能，需要用bash -c包装
        # 用timeout包裹所有命令
        if needs_bash_wrapper(prepared_command):
            # 包含shell内置命令或bash特有功能，要用bash -c，外层加timeout
            full_command = f"cd {self.working_dir} && timeout {timeout} bash -c {shlex.quote(prepared_command)}"
        else:
            # 普通命令，外层加timeout
            full_command = f"cd {self.working_dir} && timeout {timeout} {prepared_command}"
        
        exec_command = ["/bin/sh", "-c", full_command]
        
        try:
            # 使用线程池执行（参考r2egym的超时处理）
            import concurrent.futures
            
            def execute_command():
                resp = stream(
                    self.core_v1.connect_get_namespaced_pod_exec,
                    self.pod_name,
                    self.namespace,
                    command=exec_command,
                    container=self.pod_name,  # 容器名=Pod名
                    stderr=True,
                    stdin=False,
                    stdout=True,
                    tty=False,
                    _preload_content=False,
                )
                
                # 读取输出
                combined_chunks = []
                stdout_chunks = []
                stderr_chunks = []
                
                while resp.is_open():
                    resp.update(timeout=1)
                    if resp.peek_stdout():
                        chunk = resp.read_stdout()
                        stdout_chunks.append(chunk)
                        combined_chunks.append(chunk)
                    if resp.peek_stderr():
                        chunk = resp.read_stderr()
                        stderr_chunks.append(chunk)
                        combined_chunks.append(chunk)
                
                resp.close()
                exit_code = resp.returncode
                combined_output = "".join(combined_chunks)
                return combined_output, exit_code
            
            # 使用稍长的超时（参考r2egym: timeout + 5）
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(execute_command)
                output, exit_code = future.result(timeout=timeout + 5)
            
            # 处理退出码
            if exit_code is None:
                self.logger.error("K8s exec: Exit code not found")
                return False, output if not raises else None
            
            # 清理ANSI转义码
            output = re.sub(r"\x1b\[[0-9;]*m|\r", "", output)
            if strip_output:
                output = output.strip()
            
            # 检查退出码
            success = exit_code == 0
            
            if not success:
                # 某些命令的非0退出码是预期的，不应记为ERROR
                is_expected_failure = (
                    ('test' in prepared_command and exit_code == 1) or  # test命令
                    prepared_command.startswith('test ') or  # test命令
                    'nothing to commit' in output or  # git commit无改动
                    'No such remote' in output or  # git remote已删除
                    "python $(which bin/test)" in prepared_command or  # SWE-Bench test命令
                    prepared_command.startswith('grep ') or  # grep未找到
                    prepared_command.startswith('which ') or  # which未找到
                    ('pytest' in prepared_command and exit_code == 1) or  # pytest有失败测试（初始状态预期）
                    ('python -m pytest' in prepared_command and exit_code == 1) or  # pytest失败
                    ('runtests.py' in prepared_command and exit_code == 1) or  # Django runtests.py
                    ('manage.py test' in prepared_command and exit_code == 1) or  # Django manage.py test
                    ('python -m unittest' in prepared_command and exit_code == 1) or  # unittest
                    ('python -m nose' in prepared_command and exit_code == 1)  # nose
                )
                
                if is_expected_failure:
                    # 预期的失败，记录为debug
                    self.logger.debug(
                        f"K8s exec: Exit code {exit_code} (expected)\n"
                        f"Command: {prepared_command}\n"
                        f"Output: {output}"
                    )
                else:
                    # 真正的错误
                    self.logger.error(
                        f"K8s exec Error: Exit code {exit_code}\n"
                        f"Command: {prepared_command}\n"
                        f"Error Message: {output}"
                    )
                
                if raises:
                    raise RuntimeError(f"Command failed with exit code {exit_code}: {output}")
            
            return success, output
        
        except concurrent.futures.TimeoutError:
            self.logger.error(f"K8s exec Overall Timeout: {timeout + 5}s, command: {prepared_command}")
            error_msg = f"The command took too long to execute (>{timeout}s), command: {prepared_command}"
            if raises:
                raise RuntimeError(error_msg)
            return False, error_msg
        
        except client.ApiException as e:
            self.logger.error(f"K8s API Error during exec: {e}")
            error_msg = f"Error executing command in pod: {repr(e)}"
            if raises:
                raise RuntimeError(error_msg) from e
            return False, error_msg
        
        except Exception as e:
            self.logger.error(f"Unexpected error during K8s exec: {repr(e)}")
            error_msg = f"Error: {repr(e)}"
            if raises:
                raise RuntimeError(error_msg) from e
            return False, error_msg
    
    def copy_content(self, src: str | Path, target: str | Path | None = None):
        """
        复制文件到Pod（使用tar over exec，参考r2egym实现）。
        
        Args:
            src: 源文件/目录路径（主机）
            target: 目标路径（Pod内）
        """
        import io
        import tarfile
        import time
        
        src = str(src)
        target = str(target or self.working_dir)
        
        # 确保Pod已创建
        if self._pod is None:
            _ = self.pod
        
        # 计算目标目录
        dest_dir = os.path.dirname(target)
        
        # 创建tar归档
        tar_stream = io.BytesIO()
        with tarfile.open(fileobj=tar_stream, mode="w") as tar:
            tar.add(src, arcname=os.path.basename(target))
        tar_stream.seek(0)
        
        # 使用重试机制（参考r2egym）
        max_retries = 5
        retry_delay = 5
        
        for attempt in range(max_retries):
            try:
                # 通过exec将tar数据流式传输到Pod
                exec_command = ["tar", "xmf", "-", "-C", dest_dir]
                resp = stream(
                    self.core_v1.connect_get_namespaced_pod_exec,
                    self.pod_name,
                    self.namespace,
                    command=exec_command,
                    container=self.pod_name,  # 容器名=Pod名
                    stderr=True,
                    stdin=True,
                    stdout=True,
                    tty=False,
                    _preload_content=False,
                )
                
                # 写入tar数据
                resp.write_stdin(tar_stream.read())
                resp.close()
                
                self.logger.info(f"Copied {src} to Pod {self.pod_name}:{target}")
                break  # 成功
                
            except Exception as e:
                if attempt < max_retries - 1:
                    self.logger.warning(
                        f"Copy failed (attempt {attempt+1}/{max_retries}): {e}"
                    )
                    time.sleep(retry_delay)
                    retry_delay = min(retry_delay * 2, 60)  # 指数退避
                    tar_stream.seek(0)  # 重置流
                else:
                    self.logger.error(
                        f"Copy failed after {max_retries} attempts: {e}"
                    )
                    raise
    
    def clean_up(self):
        """
        清理Pod（兼容DockerTerminal.clean_up）。
        
        简化版本：快速删除，不等待watch确认。
        """
        if not self._pod:
            return
        
        try:
            self.logger.info(f"Deleting Pod: {self.pod_name}")
            self.core_v1.delete_namespaced_pod(
                name=self.pod_name,
                namespace=self.namespace,
                body=client.V1DeleteOptions(
                    grace_period_seconds=0  # 立即删除
                ),
                _request_timeout=10  # 快速超时
            )
            self.logger.info(f"✓ Pod {self.pod_name} deletion requested")
            
            self._pod = None
            self._container = None
            
        except client.ApiException as e:
            if e.status == 404:
                # Pod已删除，正常
                self.logger.debug(f"Pod '{self.pod_name}' already deleted")
                self._pod = None
                self._container = None
            else:
                self.logger.warning(f"Error deleting Pod '{self.pod_name}': {e}")
                self._pod = None
                self._container = None
        except Exception as e:
            self.logger.warning(f"Error during cleanup: {e}")
            self._pod = None
            self._container = None
    
    def close(self):
        """关闭并删除Pod。"""
        # 先关闭所有会话
        for session in self._sessions[:]:  # 复制列表以避免迭代时修改
            try:
                self.close_shell_session(session)
            except Exception as e:
                self.logger.warning(f"Error closing session: {e}")
        
        # 然后清理Pod
        self.clean_up()
    
    def __del__(self):
        """析构函数，确保Pod被清理。"""
        try:
            self.close()
        except:
            pass  # 忽略析构时的错误
    
    def new_shell_session(self):
        """
        创建新的shell会话（兼容DockerTerminal接口）。
        
        对于K8s，创建一个K8sShellSession来模拟持久会话。
        """
        # 确保Pod已创建
        if self._pod is None:
            _ = self.pod
        
        # 创建K8s shell会话（使用kubectl run -i --tty）
        session = K8sShellSession(
            pod_name=self.pod_name,  # 基础Pod名（用于生成session pod名）
            namespace=self.namespace,
            core_v1=self.core_v1,
            working_dir=self.working_dir,
            session_commands=self.session_commands,
            env_vars=self.env_vars,
            image=self.image,  # 使用相同的镜像
            logger=self.logger,
        )
        self.sessions.append(session)
        return session
    
    @property  
    def sessions(self):
        """返回会话列表（兼容DockerTerminal）。"""
        if not hasattr(self, '_sessions'):
            self._sessions = []
        return self._sessions
    
    def close_shell_session(self, session):
        """关闭shell会话"""
        session.close()
        if session in self.sessions:
            self.sessions.remove(session)
    
    @property
    def default_shell_command(self) -> str:
        """返回默认shell命令（兼容DockerTerminal）。"""
        return f"kubectl exec -it {self.pod_name} -n {self.namespace} -- /bin/bash"
    
    def __str__(self):
        return f"KubernetesTerminal[Pod:{self.pod_name}, NS:{self.namespace}, Image:{self.image}]"
    
    def __repr__(self):
        return self.__str__()


def create_k8s_terminal_for_debug_gym(
    pod_name: str | None = None,
    namespace: str = DEFAULT_NAMESPACE,
    image: str = "python:3.12",
    working_dir: str = "/workspace",
    logger: Any | None = None,
    **kwargs
) -> "KubernetesTerminal":
    """
    创建用于debug-gym的Kubernetes Terminal。
    
    这是一个便捷函数，用于创建配置好的K8s Terminal。
    
    Args:
        pod_name: Pod名称
        namespace: K8s命名空间
        image: 容器镜像
        working_dir: 工作目录
        logger: 日志记录器
        **kwargs: 其他参数
        
    Returns:
        KubernetesTerminal实例
    """
    return KubernetesTerminal(
        pod_name=pod_name,
        namespace=namespace,
        image=image,
        working_dir=working_dir,
        logger=logger,
        **kwargs
    )



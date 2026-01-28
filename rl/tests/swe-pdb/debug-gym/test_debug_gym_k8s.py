#!/usr/bin/env python3
"""
Debug-Gym Kubernetes Terminal 测试套件

测试KubernetesTerminal的核心功能，包括：
1. Pod创建和生命周期管理
2. 命令执行和超时处理
3. 文件传输（tar over exec）
4. 镜像源配置（pip/apt）
5. 错误处理和资源清理
"""
import logging
import os
import sys
import tempfile
from pathlib import Path

import pytest

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 检查依赖
try:
    from kubernetes import client, config
    KUBERNETES_AVAILABLE = True
except ImportError:
    KUBERNETES_AVAILABLE = False
    logger.warning("Kubernetes Python client not available, skipping tests")

try:
    from rllm.environments.debug_gym.k8s_terminal import KubernetesTerminal
except ImportError:
    KubernetesTerminal = None
    logger.warning("KubernetesTerminal not available")


# Skip markers
pytestmark = pytest.mark.skipif(
    not KUBERNETES_AVAILABLE or KubernetesTerminal is None,
    reason="Kubernetes client or KubernetesTerminal not available"
)


@pytest.fixture(scope="function")
def k8s_terminal():
    """创建一个测试用的KubernetesTerminal实例"""
    try:
        # 尝试加载k8s配置
        try:
            config.load_incluster_config()
        except config.ConfigException:
            config.load_kube_config()
        
        terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12-slim",  # 使用slim镜像加快测试
            logger=logger,
            pip_mirror=None,  # 测试时不配置镜像源（加快速度）
            apt_mirror=None,
        )
        
        yield terminal
        
    finally:
        # 清理
        if terminal:
            try:
                terminal.close()
            except Exception as e:
                logger.warning(f"Cleanup error: {e}")


class TestKubernetesTerminalBasics:
    """测试KubernetesTerminal的基本功能"""
    
    def test_terminal_creation(self, k8s_terminal):
        """测试Terminal创建"""
        assert k8s_terminal is not None
        assert k8s_terminal.pod_name is not None
        assert k8s_terminal.namespace == "default"
        assert k8s_terminal.image == "python:3.12-slim"
        logger.info(f"✓ Terminal created: {k8s_terminal}")
    
    def test_pod_lazy_initialization(self, k8s_terminal):
        """测试Pod延迟初始化"""
        # Pod应该尚未创建
        assert k8s_terminal._pod is None
        
        # 访问pod property触发创建
        pod = k8s_terminal.pod
        assert pod is not None
        assert k8s_terminal._pod is not None
        logger.info(f"✓ Pod initialized: {k8s_terminal.pod_name}")
    
    def test_working_directory(self, k8s_terminal):
        """测试工作目录"""
        # 检查默认工作目录
        assert k8s_terminal.working_dir == "/workspace"
        
        # 测试目录切换
        success, output = k8s_terminal.run("pwd")
        assert success, f"pwd command failed: {output}"
        assert output.strip() == "/workspace"
        logger.info(f"✓ Working directory: {output.strip()}")


class TestCommandExecution:
    """测试命令执行功能"""
    
    def test_simple_command(self, k8s_terminal):
        """测试简单命令执行"""
        success, output = k8s_terminal.run("echo 'Hello K8s!'")
        assert success, f"Command failed: {output}"
        assert "Hello K8s!" in output
        logger.info(f"✓ Command output: {output.strip()}")
    
    def test_command_with_exit_code(self, k8s_terminal):
        """测试命令退出码处理"""
        # 成功命令
        success, _ = k8s_terminal.run("exit 0")
        assert success
        
        # 失败命令
        success, output = k8s_terminal.run("exit 1")
        assert not success
        logger.info("✓ Exit code handling works")
    
    def test_command_timeout(self, k8s_terminal):
        """测试命令超时"""
        # 设置短超时
        success, output = k8s_terminal.run("sleep 10", timeout=2)
        assert not success
        assert "too long" in output.lower() or "timeout" in output.lower()
        logger.info("✓ Timeout handling works")
    
    def test_command_with_output(self, k8s_terminal):
        """测试带输出的命令"""
        success, output = k8s_terminal.run("python --version")
        assert success, f"Command failed: {output}"
        assert "Python" in output
        logger.info(f"✓ Python version: {output.strip()}")
    
    def test_command_strips_ansi(self, k8s_terminal):
        """测试ANSI转义码清理"""
        # 运行带颜色的命令
        success, output = k8s_terminal.run("echo -e '\\033[31mRed\\033[0m'")
        assert success
        # 输出应该不包含ANSI转义码
        assert "\033[" not in output
        logger.info("✓ ANSI codes stripped")
    
    def test_multi_line_command(self, k8s_terminal):
        """测试多行命令"""
        cmd = "echo 'line1' && echo 'line2' && echo 'line3'"
        success, output = k8s_terminal.run(cmd)
        assert success
        assert "line1" in output
        assert "line2" in output
        assert "line3" in output
        logger.info("✓ Multi-line command works")
    
    def test_background_command_rejected(self, k8s_terminal):
        """测试后台命令被拒绝"""
        success, output = k8s_terminal.run("sleep 100 &")
        assert not success
        assert "not supported" in output.lower() or "error" in output.lower()
        logger.info("✓ Background command rejected")


class TestFileOperations:
    """测试文件操作功能"""
    
    def test_file_creation(self, k8s_terminal):
        """测试文件创建"""
        success, _ = k8s_terminal.run("echo 'test content' > /tmp/test.txt")
        assert success
        
        success, output = k8s_terminal.run("cat /tmp/test.txt")
        assert success
        assert "test content" in output
        logger.info("✓ File creation works")
    
    def test_copy_file(self, k8s_terminal):
        """测试文件复制到Pod"""
        # 创建临时文件
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
            f.write("Hello from host!")
            temp_path = f.name
        
        try:
            # 复制到Pod
            k8s_terminal.copy_content(temp_path, "/workspace/test_copy.txt")
            
            # 验证文件
            success, output = k8s_terminal.run("cat /workspace/test_copy.txt")
            assert success
            assert "Hello from host!" in output
            logger.info("✓ File copy works")
        finally:
            os.unlink(temp_path)
    
    def test_directory_operations(self, k8s_terminal):
        """测试目录操作"""
        # 创建目录
        success, _ = k8s_terminal.run("mkdir -p /tmp/test_dir/subdir")
        assert success
        
        # 检查目录存在
        success, _ = k8s_terminal.run("test -d /tmp/test_dir/subdir")
        assert success
        
        # 列出目录
        success, output = k8s_terminal.run("ls -la /tmp/test_dir")
        assert success
        assert "subdir" in output
        logger.info("✓ Directory operations work")


class TestMirrorConfiguration:
    """测试镜像源配置"""
    
    def test_pip_mirror_configuration(self):
        """测试pip镜像源配置"""
        terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12-slim",
            logger=logger,
            pip_mirror="https://pypi.tuna.tsinghua.edu.cn/simple",
            apt_mirror=None,
        )
        
        try:
            # 触发Pod创建（会自动配置镜像源）
            _ = terminal.pod
            
            # 检查pip配置
            success, output = terminal.run("pip config list")
            assert success
            # 应该包含配置的镜像源
            assert "pypi.tuna.tsinghua.edu.cn" in output or "index-url" in output
            logger.info("✓ Pip mirror configured")
        finally:
            terminal.close()
    
    def test_no_mirror_configuration(self):
        """测试不配置镜像源"""
        terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12-slim",
            logger=logger,
            pip_mirror=None,
            apt_mirror=None,
        )
        
        try:
            _ = terminal.pod
            logger.info("✓ No mirror configuration (as expected)")
        finally:
            terminal.close()


class TestErrorHandling:
    """测试错误处理"""
    
    def test_invalid_command(self, k8s_terminal):
        """测试无效命令"""
        success, output = k8s_terminal.run("this_command_does_not_exist")
        assert not success
        assert "not found" in output.lower() or "error" in output.lower()
        logger.info("✓ Invalid command handled")
    
    def test_command_failure(self, k8s_terminal):
        """测试命令失败"""
        success, output = k8s_terminal.run("ls /nonexistent_directory")
        assert not success
        logger.info("✓ Command failure handled")
    
    def test_raises_parameter(self, k8s_terminal):
        """测试raises参数"""
        # raises=False（默认）：返回错误
        success, _ = k8s_terminal.run("exit 1", raises=False)
        assert not success
        
        # raises=True：抛出异常
        with pytest.raises(RuntimeError):
            k8s_terminal.run("exit 1", raises=True)
        
        logger.info("✓ Raises parameter works")


class TestResourceCleanup:
    """测试资源清理"""
    
    def test_terminal_close(self):
        """测试Terminal关闭"""
        terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12-slim",
            logger=logger,
            pip_mirror=None,
            apt_mirror=None,
        )
        
        # 创建Pod
        pod_name = terminal.pod_name
        _ = terminal.pod
        
        # 关闭Terminal
        terminal.close()
        
        # 验证Pod被删除（可能需要等待）
        import time
        time.sleep(2)
        
        try:
            core_v1 = client.CoreV1Api()
            pod = core_v1.read_namespaced_pod(
                name=pod_name,
                namespace="default"
            )
            # Pod可能还在删除中
            assert pod.metadata.deletion_timestamp is not None
        except client.ApiException as e:
            # 404表示Pod已删除
            assert e.status == 404
        
        logger.info(f"✓ Pod {pod_name} cleaned up")
    
    def test_cleanup_idempotent(self, k8s_terminal):
        """测试清理操作的幂等性"""
        # 多次调用close应该是安全的
        k8s_terminal.close()
        k8s_terminal.close()
        k8s_terminal.close()
        logger.info("✓ Cleanup is idempotent")


class TestCompatibility:
    """测试DockerTerminal兼容性"""
    
    def test_container_property(self, k8s_terminal):
        """测试container属性（兼容DockerTerminal）"""
        # container应该映射到pod
        assert k8s_terminal.container is not None
        assert k8s_terminal.container == k8s_terminal.pod
        logger.info("✓ Container property works")
    
    def test_base_image_property(self, k8s_terminal):
        """测试base_image属性"""
        assert k8s_terminal.base_image == "python:3.12-slim"
        
        # 测试setter
        k8s_terminal.base_image = "python:3.11"
        assert k8s_terminal.base_image == "python:3.11"
        assert k8s_terminal.image == "python:3.11"
        logger.info("✓ Base image property works")
    
    def test_setup_container_method(self, k8s_terminal):
        """测试setup_container方法"""
        container = k8s_terminal.setup_container()
        assert container is not None
        assert container == k8s_terminal.pod
        logger.info("✓ Setup container method works")
    
    def test_clean_up_method(self, k8s_terminal):
        """测试clean_up方法（兼容DockerTerminal）"""
        pod_name = k8s_terminal.pod_name
        _ = k8s_terminal.pod  # 确保Pod已创建
        
        k8s_terminal.clean_up()
        
        # 验证清理
        assert k8s_terminal._pod is None
        logger.info(f"✓ Clean up method works for {pod_name}")


class TestSessionCommands:
    """测试会话命令（如conda activate）"""
    
    def test_session_commands(self):
        """测试session_commands参数"""
        terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12-slim",
            logger=logger,
            session_commands=["export TEST_VAR=hello"],
            pip_mirror=None,
            apt_mirror=None,
        )
        
        try:
            # 运行命令，应该包含session_commands
            success, output = terminal.run("echo $TEST_VAR")
            assert success
            assert "hello" in output
            logger.info("✓ Session commands work")
        finally:
            terminal.close()
    
    def test_prepare_command(self):
        """测试命令准备"""
        terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12-slim",
            logger=logger,
            session_commands=["export VAR=1"],
            pip_mirror=None,
            apt_mirror=None,
        )
        
        try:
            # 测试字符串命令
            cmd = terminal.prepare_command("echo test")
            assert "export VAR=1" in cmd
            assert "echo test" in cmd
            
            # 测试列表命令
            cmd = terminal.prepare_command(["echo a", "echo b"])
            assert "export VAR=1" in cmd
            assert "echo a" in cmd
            assert "echo b" in cmd
            
            logger.info("✓ Command preparation works")
        finally:
            terminal.close()


def test_integration_workflow():
    """集成测试：完整的工作流"""
    logger.info("=" * 60)
    logger.info("Running Integration Test")
    logger.info("=" * 60)
    
    terminal = None
    try:
        # 1. 创建Terminal
        terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12-slim",
            logger=logger,
            pip_mirror=None,
            apt_mirror=None,
        )
        logger.info(f"✓ Step 1: Terminal created: {terminal.pod_name}")
        
        # 2. 执行Python命令
        success, output = terminal.run("python -c 'print(sum(range(10)))'")
        assert success
        assert "45" in output
        logger.info(f"✓ Step 2: Python command executed: {output.strip()}")
        
        # 3. 创建文件
        success, _ = terminal.run("echo 'test data' > /tmp/data.txt")
        assert success
        logger.info("✓ Step 3: File created")
        
        # 4. 读取文件
        success, output = terminal.run("cat /tmp/data.txt")
        assert success
        assert "test data" in output
        logger.info(f"✓ Step 4: File read: {output.strip()}")
        
        # 5. 安装包（简单测试）
        success, _ = terminal.run("pip install --quiet requests", timeout=60)
        if success:
            logger.info("✓ Step 5: Package installed")
        else:
            logger.warning("⚠ Step 5: Package installation skipped or failed")
        
        # 6. 清理
        terminal.close()
        logger.info(f"✓ Step 6: Terminal closed")
        
        logger.info("=" * 60)
        logger.info("Integration Test PASSED ✓")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"Integration test failed: {e}")
        if terminal:
            terminal.close()
        raise


if __name__ == "__main__":
    # 可以直接运行此文件进行测试
    pytest.main([__file__, "-v", "-s"])


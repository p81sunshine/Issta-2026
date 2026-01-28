"""
SWE-bench Environment for Debug-Gym + rLLM

专门用于SWE-bench任务的环境适配器，包装debug_gym.gym.envs.swe_bench.SWEBenchEnv
"""
import json
import logging
import os
import sys
from typing import Any

# 添加debug-gym到路径
try:
    from debug_gym.gym.envs.swe_bench import SWEBenchEnv as DebugGymSWEBenchEnv
    from debug_gym.gym.terminals.docker import DockerTerminal
    from debug_gym.gym.terminals.local import LocalTerminal
    from debug_gym.gym.tools import BashTool
    from debug_gym.gym.tools import EvalTool
    from debug_gym.gym.tools import GrepTool
    from debug_gym.gym.tools import ListdirTool
    from debug_gym.gym.tools import PDBTool
    from debug_gym.gym.tools import RewriteTool
    from debug_gym.gym.tools import ViewTool
    from debug_gym.logger import DebugGymLogger
except ImportError as e:
    logging.warning(f"Failed to import debug-gym SWE-bench module: {e}")
    DebugGymSWEBenchEnv = None
    DockerTerminal = None
    BashTool = None
    EvalTool = None
    GrepTool = None
    ListdirTool = None
    PDBTool = None
    RewriteTool = None
    ViewTool = None
    DebugGymLogger = None

# 导入K8s Terminal
try:
    from rllm.environments.debug_gym.k8s_terminal import KubernetesTerminal
except ImportError:
    KubernetesTerminal = None

from rllm.environments.base.base_env import BaseEnv

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class SWEBenchDebugGymEnv(BaseEnv):
    """
    SWE-bench环境适配器，用于rLLM强化学习框架。
    
    这个类将debug-gym的SWEBenchEnv包装成rllm兼容的环境接口，
    保留了SWE-bench特定的逻辑（Docker镜像管理、测试评分等）。
    """
    
    def __init__(
        self,
        # SWE-bench数据集配置
        dataset_id: str = "SWE-bench/SWE-bench_Verified",
        dataset_revision: str = "99450355ca8c611021187a57ffac304b66666738",
        split: str = "test",
        instance_id: str | None = None,  # 单个任务ID
        
        # Debug-Gym配置
        enable_pdb: bool = True,
        enable_grep: bool = True,
        enable_bash: bool = False,
        persistent_breakpoints: bool = True,
        auto_list: bool = True,
        auto_eval_on_rewrite: bool = False,
        run_timeout: int = 300,
        dir_tree_depth: int = 2,
        max_steps: int = 50,
        
        # 后端配置
        backend: str = "docker",  # "docker" 或 "kubernetes"
        base_image: str | None = None,  # 如果为None，使用SWE-bench的镜像
        
        # K8s配置
        k8s_namespace: str = "default",
        k8s_pod_name: str | None = None,
        k8s_kubeconfig: str | None = None,
        k8s_pip_mirror: str | None = "https://mirrors.zju.edu.cn/pypi/web/simple",
        k8s_apt_mirror: str | None = "mirrors.zju.edu.cn",
        
        logger_name: str = "debug-gym-swe-rllm",
        **kwargs,
    ):
        """
        初始化SWE-bench Debug-Gym环境。
        
        Args:
            dataset_id: HuggingFace数据集ID
            dataset_revision: 数据集版本
            split: 数据集分割（train/test）
            instance_id: 具体的任务实例ID（如"django__django-11099"）
            enable_pdb: 启用pdb调试器
            enable_grep: 启用grep搜索
            enable_bash: 启用bash命令
            persistent_breakpoints: 持久化断点
            auto_list: 自动列出pdb上下文
            auto_eval_on_rewrite: 重写后自动评估
            run_timeout: 运行超时（秒）
            dir_tree_depth: 目录树显示深度
            max_steps: 最大步数
            backend: 运行后端（"docker"或"kubernetes"）
            base_image: 基础镜像（通常由SWE-bench自动确定）
            k8s_namespace: Kubernetes命名空间
            k8s_pod_name: Kubernetes Pod名称
            k8s_kubeconfig: kubeconfig文件路径
            k8s_pip_mirror: PyPI镜像源（默认ZJU镜像，None表示不配置）
            k8s_apt_mirror: apt镜像源域名（默认ZJU镜像，None表示不配置）
            logger_name: 日志器名称
        """
        if DebugGymSWEBenchEnv is None:
            raise ImportError(
                "debug-gym SWE-bench environment is not installed or cannot be imported. "
                "Please ensure debug-gym and its SWE-bench dependencies are installed."
            )
        
        # SWE-bench now supports both Docker and Kubernetes backends!
        if backend not in ["docker", "kubernetes"]:
            raise ValueError(f"Unsupported backend: {backend}. Please use 'docker' or 'kubernetes'")
        
        self.dataset_id = dataset_id
        self.dataset_revision = dataset_revision
        self.split = split
        self.instance_id = instance_id
        self.enable_pdb = enable_pdb
        self.enable_grep = enable_grep
        self.enable_bash = enable_bash
        self.persistent_breakpoints = persistent_breakpoints
        self.auto_list = auto_list
        self.auto_eval_on_rewrite = auto_eval_on_rewrite
        self.run_timeout = run_timeout
        self.dir_tree_depth = dir_tree_depth
        self.max_steps = max_steps
        self.backend = backend
        self.base_image = base_image
        self.k8s_namespace = k8s_namespace
        self.k8s_pod_name = k8s_pod_name
        self.k8s_kubeconfig = k8s_kubeconfig
        self.k8s_pip_mirror = k8s_pip_mirror
        self.k8s_apt_mirror = k8s_apt_mirror
        self.logger_name = logger_name
        self.additional_kwargs = kwargs
        
        # 初始化debug-gym日志器
        self.debug_gym_logger = DebugGymLogger(logger_name)
        
        # 创建Terminal
        self.terminal = self._create_terminal()
        
        # 创建SWE-bench环境
        self.env = None
        self.total_steps = 0
        self.current_task = None
        
        self._initialize_env()
    
    def _create_terminal(self):
        """创建Terminal实例（Docker或Kubernetes）。"""
        if self.backend == "docker":
            return DockerTerminal(
                base_image=self.base_image or "ubuntu:latest",
                logger=self.debug_gym_logger
            )
        elif self.backend == "kubernetes":
            # K8s支持
            if KubernetesTerminal is None:
                raise ImportError(
                    "KubernetesTerminal未安装。"
                    "请安装: pip install kubernetes"
                )
            return KubernetesTerminal(
                pod_name=self.k8s_pod_name,
                namespace=self.k8s_namespace,
                base_image=self.base_image or "python:3.12",  # SWE-bench会在setup_task中设置
                kubeconfig=self.k8s_kubeconfig,
                working_dir="/testbed",  # SWE-bench默认工作目录
                pip_mirror=self.k8s_pip_mirror,  # 配置pip镜像源
                apt_mirror=self.k8s_apt_mirror,  # 配置apt镜像源
                logger=self.debug_gym_logger,
            )
        else:
            raise ValueError(f"Unsupported backend: {self.backend}")
    
    def _initialize_env(self):
        """初始化debug-gym SWE-bench环境。"""
        # 对于K8s后端，需要特殊处理以避免Docker镜像预拉取
        if self.backend == "kubernetes":
            # 创建自定义的SWEBenchEnv，跳过Docker镜像预拉取
            self.env = self._create_k8s_swe_bench_env()
        else:
            # Docker后端使用标准流程
            self.env = DebugGymSWEBenchEnv(
                dataset_id=self.dataset_id,
                dataset_revision=self.dataset_revision,
                split=self.split,
                terminal=self.terminal,
                auto_eval_on_rewrite=self.auto_eval_on_rewrite,
                run_timeout=self.run_timeout,
                dir_tree_depth=self.dir_tree_depth,
                persistent_breakpoints=self.persistent_breakpoints,
                auto_list=self.auto_list,
                logger=self.debug_gym_logger,
                problems=self.instance_id,
                **self.additional_kwargs,
            )
        
        # 添加工具
        self._add_tools()
    
    def _create_k8s_swe_bench_env(self):
        """
        为K8s后端创建SWEBenchEnv，跳过Docker镜像预拉取。
        
        K8s会在Pod创建时自动拉取镜像到节点，不需要在host上预拉取。
        """
        # 创建一个修改版的SWEBenchEnv
        class K8sSWEBenchEnv(DebugGymSWEBenchEnv):
            """K8s优化的SWEBenchEnv"""
            
            def load_dataset(self, problems):
                """
                覆盖load_dataset，跳过Docker镜像预拉取。
                
                K8s会在创建Pod时自动拉取镜像到节点。
                """
                import datasets
                from debug_gym.gym.utils import filter_problems
                
                self.ds = datasets.load_dataset(
                    self.dataset_id, 
                    revision=self.dataset_revision
                )[self.split]
                
                dataset = {id: i for i, id in enumerate(self.ds["instance_id"])}
                problems = filter_problems(dataset, problems)
                dataset = {id: i for id, i in dataset.items() if id in problems}
                
                self.logger.info(
                    f"Loaded {len(dataset)} instances from {self.dataset_id}. "
                    f"Docker image pulling skipped (K8s will pull images automatically)."
                )
                
                # ✅ 跳过Docker镜像预拉取
                # K8s会在创建Pod时拉取镜像
                
                return dataset
        
        # 创建实例
        return K8sSWEBenchEnv(
            dataset_id=self.dataset_id,
            dataset_revision=self.dataset_revision,
            split=self.split,
            terminal=self.terminal,
            auto_eval_on_rewrite=self.auto_eval_on_rewrite,
            run_timeout=self.run_timeout,
            dir_tree_depth=self.dir_tree_depth,
            persistent_breakpoints=self.persistent_breakpoints,
            auto_list=self.auto_list,
            logger=self.debug_gym_logger,
            problems=self.instance_id,
            **self.additional_kwargs,
        )
    
    def _add_tools(self):
        """向环境添加工具。"""
        # 始终添加的核心工具
        self.env.add_tool(ViewTool())
        self.env.add_tool(ListdirTool())
        self.env.add_tool(EvalTool())
        self.env.add_tool(RewriteTool())
        
        # 可选工具
        if self.enable_pdb and PDBTool is not None:
            self.env.add_tool(PDBTool())
        
        if self.enable_grep and GrepTool is not None:
            self.env.add_tool(GrepTool())
        
        if self.enable_bash and BashTool is not None:
            self.env.add_tool(BashTool())
    
    def reset(self) -> tuple[str, dict]:
        """
        重置环境到初始状态。
        
        Returns:
            包含任务指令和额外信息的元组
        """
        self.total_steps = 0
        
        # 重置debug-gym环境
        # 如果instance_id已设置，使用它；否则需要从数据中获取
        task_name = self.instance_id or self._get_next_task()
        info = self.env.reset(options={"task_name": task_name})
        
        # 构建观察字符串
        observation = self._build_observation_string(info)
        
        # 构建额外信息字典（包含元信息）
        extra_info = {
            # 评分信息
            "score": info.score,
            "max_score": info.max_score,
            "done": info.done,
            "rewrite_counter": info.rewrite_counter,
            # 工具和环境状态
            "tools": [tool.name for tool in info.tools],
            "dir_tree": info.dir_tree,
            "current_breakpoints": info.current_breakpoints,
            # 任务信息
            "instructions": info.instructions,
            "instance_id": task_name,
            "repo": getattr(self.env, "repo", None),
            "version": getattr(self.env, "version", None),
            # 步骤限制
            "max_steps": self.max_steps,
        }
        
        return observation, extra_info
    
    def _get_next_task(self) -> str:
        """
        获取下一个任务ID。
        如果instance_id未设置，从数据集中随机选择一个。
        """
        if hasattr(self.env, 'dataset') and self.env.dataset:
            import random
            return random.choice(list(self.env.dataset.keys()))
        raise ValueError("Failed to get task: dataset is not initialized or empty")
    
    def _build_observation_string(self, info) -> str:
        """
        从EnvInfo构建观察字符串。
        
        参考swe.py：observation只包含工具的输出，不包含元信息。
        元信息（工具列表、得分等）放在extra_info中。
        
        Args:
            info: debug-gym的EnvInfo对象
            
        Returns:
            工具的输出字符串
        """
        # 只返回工具的观察结果（参考SWEEnv的实现）
        if info.step_observation:
            return str(info.step_observation.observation)
        return ""
    
    def step(self, action: str | dict) -> tuple[str, float, bool, dict]:
        """
        在环境中执行一步。
        
        Args:
            action: 要执行的动作（JSON字符串或字典）
            
        Returns:
            (observation, reward, done, info) 元组
        """
        # Parse action
        if isinstance(action, str):
            try:
                action_dict = json.loads(action)
            except json.JSONDecodeError:
                error_msg = f"Failed to parse action JSON: {action}"
                return error_msg, 0.0, False, False, {"error": error_msg}
        else:
            action_dict = action
        
        # 创建ToolCall对象
        from debug_gym.gym.tools.tool import ToolCall
        import uuid
        
        # 支持多种action格式
        # 格式1: {"name": "...", "arguments": {...}}
        # 格式2: {"tool": "...", "args": {...}}  (向后兼容)
        tool_name = action_dict.get("name") or action_dict.get("tool", "")
        tool_args = action_dict.get("arguments") or action_dict.get("args", {})
        
        tool_call = ToolCall(
            id=str(uuid.uuid4()),  # 生成唯一ID
            name=tool_name,
            arguments=tool_args,
        )
        
        # 执行步骤
        info = self.env.step(
            action_tool_call=tool_call,
            action_content=action_dict.get("content"),
            action_reasoning=action_dict.get("reasoning"),
        )
        
        self.total_steps += 1
        
        # 构建观察
        observation = self._build_observation_string(info)
        
        # 计算奖励（立即奖励，最终奖励由compute_final_reward计算）
        reward = 0.0
        
        # 检查是否完成
        terminated = info.done  # 环境自然终止（任务完成）
        truncated = self.total_steps >= self.max_steps and not info.done  # 达到最大步数限制
        done = terminated or truncated  # 总的完成状态
        
        # 构建信息字典（包含元信息）
        extra_info = {
            # 评分信息
            "score": info.score,
            "max_score": info.max_score,
            "done": done,
            "terminated": terminated,
            "truncated": truncated,
            "rewrite_counter": info.rewrite_counter,
            # 工具和环境状态
            "tools": [tool.name for tool in info.tools],
            "dir_tree": info.dir_tree,
            "current_breakpoints": info.current_breakpoints,
            # 任务信息
            "instructions": info.instructions,
            "instance_id": self.current_task or getattr(self.env, "task_name", None),
            "repo": getattr(self.env, "repo", None),
            # 步骤限制
            "max_steps": self.max_steps,
            "total_steps": self.total_steps,
        }
        
        return observation, reward, done, extra_info
    
    def compute_final_reward(self) -> float:
        """
        计算最终奖励（基于SWE-bench的测试通过率）。
        
        Returns:
            最终奖励值（0.0到1.0之间）
        """
        if self.env.infos is None:
            return 0.0
        
        # 基于最终得分计算奖励
        score = self.env.infos.score
        max_score = self.env.infos.max_score
        
        if max_score > 0:
            return float(score) / float(max_score)
        return 0.0
    
    def close(self) -> None:
        """关闭环境并清理资源。"""
        if self.env is not None:
            self.env.close()
    
    @staticmethod
    def from_dict(extra_info: dict | str) -> "SWEBenchDebugGymEnv":
        """
        从JSON配置创建环境实例。
        
        Args:
            extra_info: 包含配置参数的字典
            
        Returns:
            初始化的SWEBenchDebugGymEnv实例
        """
        if isinstance(extra_info, str):
            extra_info = json.loads(extra_info)
        
        return SWEBenchDebugGymEnv(**extra_info)
    
    def get_patch(self) -> str:
        """
        获取当前的git补丁。
        
        Returns:
            git diff 输出的补丁内容
        """
        if self.env is not None:
            return self.env.patch
        return ""
    
    def get_gold_patch(self) -> str:
        """
        获取gold patch（ground truth）。
        
        Returns:
            gold patch内容
        """
        if hasattr(self.env, 'gold_patch'):
            return self.env.gold_patch
        return ""
    
    def apply_gold_patch(self) -> bool:
        """
        应用gold patch（用于测试/验证）。
        
        Returns:
            是否成功应用
        """
        if self.env is not None and hasattr(self.env, 'apply_gold_patch'):
            try:
                self.env.apply_gold_patch()
                return True
            except Exception as e:
                logger.error(f"Failed to apply gold patch: {e}")
                return False
        return False
    
    def get_trajectory(self) -> dict:
        """
        获取环境的轨迹信息。
        
        Returns:
            包含轨迹信息的字典
        """
        if self.env is not None and self.env.infos is not None:
            return {
                "score": self.env.infos.score,
                "max_score": self.env.infos.max_score,
                "done": self.env.infos.done,
                "rewrite_counter": self.env.infos.rewrite_counter,
                "total_steps": self.total_steps,
                "instance_id": getattr(self.env, "task_name", None),
                "repo": getattr(self.env, "repo", None),
                "version": getattr(self.env, "version", None),
                "patch": self.get_patch(),
            }
        return {}
    
    @staticmethod
    def is_multithread_safe() -> bool:
        """SWE-bench环境是否线程安全。"""
        return True


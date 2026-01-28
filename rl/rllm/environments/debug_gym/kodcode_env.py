"""
KodCode Debug-Gym environment adapter for rLLM.

Wraps debug-gym's KodCodeEnv so it can be used by rLLM agents. Supports both
local and docker terminals and keeps the observation/info format aligned with
the existing SWE-bench adapter.
"""
import json
import logging
import random
import uuid
from pathlib import Path
from typing import Any
import shutil
import tempfile

try:
    from debug_gym.gym.envs.kodcode import DOCKER_KODCODE_IMAGE_NAME
    from debug_gym.gym.envs.kodcode import KodCodeEnv as DebugGymKodCodeEnv
    from debug_gym.gym.terminals.docker import DockerTerminal
    from debug_gym.gym.terminals.local import LocalTerminal
    from debug_gym.gym.tools import (
        BashTool,
        EvalTool,
        GrepTool,
        ListdirTool,
        PDBTool,
        RewriteTool,
        ViewTool,
    )
    from debug_gym.gym.tools.tool import ToolCall
    from debug_gym.logger import DebugGymLogger
except ImportError as e:
    logging.warning(f"Failed to import debug-gym KodCode modules: {e}")
    DebugGymKodCodeEnv = None
    DOCKER_KODCODE_IMAGE_NAME = "debug-gym:kodcode"
    DockerTerminal = None
    LocalTerminal = None
    BashTool = None
    EvalTool = None
    GrepTool = None
    ListdirTool = None
    PDBTool = None
    RewriteTool = None
    ViewTool = None
    ToolCall = None
    DebugGymLogger = None

from rllm.environments.base.base_env import BaseEnv

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


class KodCodeDebugGymEnv(BaseEnv):
    """KodCode Debug-Gym environment adapter for rLLM."""

    def __init__(
        self,
        entrypoint: str = "python -m pytest --tb=short -sq test.py",
        data_path: str | Path | None = None,
        problems: str | list[str] | None = "all",
        instance_id: str | None = None,
        enable_pdb: bool = True,
        enable_grep: bool = True,
        enable_bash: bool = False,
        persistent_breakpoints: bool = True,
        auto_list: bool = False,
        auto_eval_on_rewrite: bool = False,
        run_timeout: int = 30,
        dir_tree_depth: int = 1,
        show_directory_tree: bool = True,
        show_current_breakpoints: bool = False,
        max_steps: int = 80,
        backend: str = "local",
        base_image: str | None = None,
        logger_name: str = "debug-gym-kodcode",
        working_dir: str | None = None,
        **kwargs,
    ):
        if DebugGymKodCodeEnv is None:
            raise ImportError(
                "debug-gym KodCode environment is not installed or cannot be imported. "
                "Please ensure debug-gym is available."
            )

        self.entrypoint = entrypoint
        self.data_path = data_path
        self.problems = problems
        self.instance_id = instance_id
        self.enable_pdb = enable_pdb
        self.enable_grep = enable_grep
        self.enable_bash = enable_bash
        self.persistent_breakpoints = persistent_breakpoints
        self.auto_list = auto_list
        self.auto_eval_on_rewrite = auto_eval_on_rewrite
        self.run_timeout = run_timeout
        self.dir_tree_depth = dir_tree_depth
        self.show_directory_tree = show_directory_tree
        self.show_current_breakpoints = show_current_breakpoints
        self.max_steps = max_steps
        self.backend = backend
        self.base_image = base_image or DOCKER_KODCODE_IMAGE_NAME
        self.working_dir = working_dir
        self.additional_kwargs = kwargs

        self.debug_gym_logger = DebugGymLogger(logger_name)
        self.terminal = self._create_terminal()
        self._tmp_dataset_dir: Path | None = None
        self._cleanup_dataset_dir: bool = False

        # Instantiate underlying debug-gym env
        self.env = DebugGymKodCodeEnv(
            entrypoint=self.entrypoint,
            terminal=self.terminal,
            data_path=self.data_path,
            run_timeout=self.run_timeout,
            dir_tree_depth=self.dir_tree_depth,
            persistent_breakpoints=self.persistent_breakpoints,
            auto_list=self.auto_list,
            auto_eval_on_rewrite=self.auto_eval_on_rewrite,
            logger=self.debug_gym_logger,
            problems=self.problems,
            **self.additional_kwargs,
        )
        self._add_tools()

        self.total_steps = 0
        self.current_task = None

    def _create_terminal(self):
        """Create terminal backend (local or docker)."""
        if self.backend == "local":
            if LocalTerminal is None:
                raise ImportError("debug-gym LocalTerminal is unavailable.")
            return LocalTerminal(
                working_dir=self.working_dir,
                logger=self.debug_gym_logger,
            )
        if self.backend == "docker":
            if DockerTerminal is None:
                raise ImportError("debug-gym DockerTerminal is unavailable.")
            return DockerTerminal(
                base_image=self.base_image,
                logger=self.debug_gym_logger,
            )
        raise ValueError(f"Unsupported backend: {self.backend}. Use 'local' or 'docker'.")

    def _add_tools(self):
        """Attach default tools to the KodCode environment."""
        self.env.add_tool(ViewTool())
        self.env.add_tool(ListdirTool())
        self.env.add_tool(EvalTool())
        self.env.add_tool(RewriteTool())

        if self.enable_pdb and PDBTool is not None:
            self.env.add_tool(PDBTool())
        if self.enable_grep and GrepTool is not None:
            self.env.add_tool(GrepTool())
        if self.enable_bash and BashTool is not None:
            self.env.add_tool(BashTool())

    def get_tools_for_openai(self) -> list[dict]:
        """
        将环境中的 tools 转换为 OpenAI function calling 格式。
        
        Translates the list of tools into OpenAI function calling format.
        OpenAI function calling format: https://platform.openai.com/docs/guides/function-calling
        
        Returns:
            OpenAI 格式的 tools 列表，可以直接传递给 OpenAI API
        """
        if not hasattr(self.env, 'tools'):
            return []
        
        output = []
        for tool in self.env.tools:
            _tool = {"type": "function", "function": {}}
            _function = _tool["function"]
            _function["name"] = tool.name
            _function["description"] = tool.description
            _function["parameters"] = {
                "type": "object",
                "properties": tool.arguments,
                "additionalProperties": False,
            }
            # _function["strict"] = True  # this is not supported by reasoning models such as o3
            if len(tool.arguments) > 0:
                _function["parameters"]["required"] = list(tool.arguments.keys())
            output.append(_tool)
        return output

    def _get_next_task(self) -> str:
        """Pick the next task from the dataset."""
        if hasattr(self.env, "dataset") and self.env.dataset:
            return self.instance_id or random.choice(list(self.env.dataset.keys()))
        raise ValueError("Failed to get task: dataset is not initialized or empty")

    def _build_observation_string(self, info: Any) -> str:
        """Return tool output only (metadata goes to extra_info)."""
        if info.step_observation:
            return str(info.step_observation.observation)
        return ""

    def reset(self) -> tuple[str, dict]:
        """Reset environment to initial state."""
        self.total_steps = 0
        task_name = self._get_next_task()
        self.current_task = task_name

        info = self.env.reset(options={"task_name": task_name})
        observation = self._build_observation_string(info)

        done_flag = getattr(info, "terminated", getattr(info, "done", False))
        # If eval timed out during reset, mark as done immediately to mask this trajectory
        reset_eval_timeout = getattr(info, "reset_eval_timeout", False)
        if reset_eval_timeout:
            done_flag = True
            self.debug_gym_logger.warning(
                f"Eval timed out during reset for task {task_name}. "
                "This trajectory will be masked from RL training."
            )

        extra_info = {
            "score": info.score,
            "max_score": info.max_score,
            "done": done_flag,
            "rewrite_counter": info.rewrite_counter,
            "tools": [tool.name for tool in info.tools],
            "tools_openai_format": self.get_tools_for_openai(),  # 添加 OpenAI 格式的 tools
            "dir_tree": info.dir_tree if self.show_directory_tree else "",
            "current_breakpoints": (
                info.current_breakpoints if self.show_current_breakpoints else ""
            ),
            "instructions": info.instructions,
            "instance_id": task_name,
            "repo": getattr(self.env, "repo", None),
            "version": getattr(self.env, "version", None),
            "max_steps": self.max_steps,
            "reset_eval_timeout": reset_eval_timeout,  # Pass reset_eval_timeout flag to workflow
        }
        return observation, extra_info

    def step(self, action: str | dict) -> tuple[str, float, bool, dict]:
        """Take one step in the environment."""
        if isinstance(action, str):
            try:
                action_dict = json.loads(action)
            except json.JSONDecodeError:
                error_msg = f"Failed to parse action JSON: {action}"
                return error_msg, 0.0, False, {"error": error_msg}
        else:
            action_dict = action

        if ToolCall is None:
            raise ImportError("debug-gym ToolCall is unavailable.")

        tool_name = action_dict.get("name") or action_dict.get("tool", "")
        tool_args = action_dict.get("arguments") or action_dict.get("args", {})

        tool_call = ToolCall(
            id=str(uuid.uuid4()),
            name=tool_name,
            arguments=tool_args,
        )
        info = self.env.step(
            action_tool_call=tool_call,
            action_content=action_dict.get("content"),
            action_reasoning=action_dict.get("reasoning"),
        )
        self.total_steps += 1
        observation = self._build_observation_string(info)

        terminated = getattr(info, "terminated", getattr(info, "done", False))
        truncated = self.total_steps >= self.max_steps and not terminated
        done = terminated or truncated
        
        # 计算二元 reward：1.0 表示完全解决，0.0 表示未完全解决
        # 只有在任务终止且完全解决时才给 reward = 1.0
        if terminated and info.score == info.max_score and info.max_score > 0:
            reward = 1.0
        else:
            reward = 0.0

        extra_info = {
            "score": info.score,
            "max_score": info.max_score,
            "done": done,
            "terminated": terminated,
            "truncated": truncated,
            "rewrite_counter": info.rewrite_counter,
            "tools": [tool.name for tool in info.tools],
            "tools_openai_format": self.get_tools_for_openai(),  # 添加 OpenAI 格式的 tools
            "dir_tree": info.dir_tree if self.show_directory_tree else "",
            "current_breakpoints": (
                info.current_breakpoints if self.show_current_breakpoints else ""
            ),
            "instructions": info.instructions,
            "instance_id": self.current_task or getattr(self.env, "task_name", None),
            "repo": getattr(self.env, "repo", None),
            "max_steps": self.max_steps,
            "total_steps": self.total_steps,
        }

        return observation, reward, done, extra_info

    def compute_final_reward(self) -> float:
        """
        计算最终的二元 reward。
        
        返回 1.0 如果任务完全解决（所有测试都通过），否则返回 0.0。
        这与 SWE-bench 的评估方式一致。
        
        Calculate final binary reward.
        
        Returns 1.0 if the task is fully resolved (all tests pass), otherwise 0.0.
        This matches the evaluation approach used in SWE-bench.
        """
        if self.env.infos is None:
            return 0.0

        score = self.env.infos.score
        max_score = self.env.infos.max_score

        # 二元 reward：完全解决返回 1.0，否则返回 0.0
        if max_score > 0 and score == max_score:
            return 1.0
        return 0.0

    def close(self) -> None:
        if self.env is not None:
            self.env.close()
        if self._cleanup_dataset_dir and self._tmp_dataset_dir and self._tmp_dataset_dir.exists():
            shutil.rmtree(self._tmp_dataset_dir, ignore_errors=True)

    @staticmethod
    def from_dict(extra_info: dict | str) -> "KodCodeDebugGymEnv":
        """Create environment from serialized config."""
        import inspect

        if isinstance(extra_info, str):
            extra_info = json.loads(extra_info)

        # Merge nested extra_info if present (common in parquet rows)
        nested = extra_info.get("extra_info")
        if isinstance(nested, str):
            try:
                nested = json.loads(nested)
            except json.JSONDecodeError:
                nested = None
        if isinstance(nested, dict):
            merged = {**nested, **extra_info}
        else:
            merged = {**extra_info}

        # Promote wrapped entry payloads if present so both call paths are supported.
        entry_cfg: dict[str, Any] = {}
        entry_obj = merged.pop("entry", None)
        if isinstance(entry_obj, str):
            try:
                entry_cfg = json.loads(entry_obj)
            except json.JSONDecodeError:
                entry_cfg = {}
        elif isinstance(entry_obj, dict):
            entry_cfg = entry_obj
        if entry_cfg:
            merged = {**entry_cfg, **merged}

        files = merged.pop("files", None)
        # Determine task name
        task_name = merged.get("task_name") or merged.get("id") or merged.get("name") or merged.get("task_id")
        entrypoint = merged.get("entrypoint") or merged.get("env_entrypoint")
        user_data_path = merged.get("data_path")

        tmp_dataset_dir = None
        cleanup_dir = True
        # Check if files exists and is iterable (works for both list and numpy array)
        if files is not None and hasattr(files, "__iter__"):
            # Build a dataset directory with a single task
            # Always create a unique directory for each environment instance to avoid conflicts
            if not task_name:
                task_name = "task"
            
            if user_data_path:
                # If user provided data_path, create a unique subdirectory under it
                # to avoid conflicts when multiple problems share the same folder
                base_path = Path(user_data_path).resolve()
                # Create a unique subdirectory using task_name and a random suffix
                unique_suffix = str(uuid.uuid4())[:8]
                tmp_dataset_dir = base_path / f"{task_name}_{unique_suffix}"
                tmp_dataset_dir.mkdir(parents=True, exist_ok=True)
            else:
                # Use temporary directory that will be cleaned up
                tmp_dataset_dir = Path(tempfile.mkdtemp(prefix="kodcode-dataset-"))
            task_dir = tmp_dataset_dir / task_name
            task_dir.mkdir(parents=True, exist_ok=True)
            for file_rec in files:
                path = Path(file_rec.get("path", ""))
                content = file_rec.get("content", "")
                target = task_dir / path
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(content, encoding="utf-8")

            # default entrypoint
            # if not entrypoint:
            entrypoint = "python -m pytest --tb=short -sq test.py"

            # Override data_path to point to the unique subdirectory we created
            merged["data_path"] = str(tmp_dataset_dir)
            merged["instance_id"] = task_name
            merged["problems"] = [task_name]
            merged["entrypoint"] = entrypoint

        # Filter init kwargs to known signature + allow passthrough
        sig = inspect.signature(KodCodeDebugGymEnv.__init__)
        init_kwargs = {}
        for name, param in sig.parameters.items():
            if name == "self":
                continue
            if name in merged:
                init_kwargs[name] = merged[name]
        # Pass remaining items as kwargs
        # Note: data_path should be in init_kwargs if tmp_dataset_dir was set
        env = KodCodeDebugGymEnv(**init_kwargs, **{k: v for k, v in merged.items() if k not in init_kwargs})
        env._tmp_dataset_dir = tmp_dataset_dir
        env._cleanup_dataset_dir = cleanup_dir
        return env

    def get_patch(self) -> str:
        """Return git diff from the workspace if available."""
        if self.env is not None:
            return getattr(self.env, "patch", "")
        return ""

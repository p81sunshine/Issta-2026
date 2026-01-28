"""
Debug-Gym奖励函数模块。

提供用于Debug-Gym任务的奖励函数，用于强化学习训练。
"""
import json
import logging
import os
import subprocess
import tempfile
from pathlib import Path
from typing import Any

from rllm.rewards.reward_types import RewardConfig, RewardInput, RewardOutput

logger = logging.getLogger(__name__)


class RewardDebugGymFn:
    """
    Debug-Gym任务的奖励函数。
    
    根据agent的调试和修复结果计算奖励。奖励基于：
    1. 测试通过的比例
    2. 重写次数（惩罚过多的重写）
    3. 步骤数（惩罚低效的解决方案）
    """
    
    def __init__(self, config: RewardConfig | None = None):
        """
        初始化Debug-Gym奖励函数。
        
        Args:
            config: 奖励配置对象
        """
        self.config = config or RewardConfig()
        
        # 奖励权重
        self.score_weight = 1.0  # 测试通过率权重
        self.rewrite_penalty = 0.1  # 每次重写的惩罚
        self.step_penalty = 0.01  # 每步的惩罚
        self.success_bonus = 0.5  # 完全成功的额外奖励
    
    def __call__(
        self, 
        task_info: dict | RewardInput, 
        action: str | None = None
    ) -> RewardOutput:
        """
        计算奖励。
        
        Args:
            task_info: 任务信息字典或RewardInput对象
            action: agent的响应（可选，用于兼容性）
            
        Returns:
            RewardOutput对象，包含奖励值和元数据
        """
        if isinstance(task_info, RewardInput):
            task_info = task_info.task_info
        
        # 从环境信息中提取关键指标
        score = task_info.get("score", 0)
        max_score = task_info.get("max_score", 1)
        rewrite_counter = task_info.get("rewrite_counter", 0)
        total_steps = task_info.get("total_steps", 0)
        done = task_info.get("done", False)
        
        # 计算基础奖励（测试通过率）
        if max_score > 0:
            base_reward = float(score) / float(max_score)
        else:
            base_reward = 0.0
        
        # 应用权重
        reward = base_reward * self.score_weight
        
        # 应用惩罚
        if rewrite_counter > 0:
            rewrite_penalty = min(self.rewrite_penalty * rewrite_counter, 0.5)
            reward -= rewrite_penalty
        
        if total_steps > 0:
            step_penalty = min(self.step_penalty * total_steps, 0.3)
            reward -= step_penalty
        
        # 完全成功的奖励加成
        if done and score == max_score:
            reward += self.success_bonus
        
        # 确保奖励在合理范围内
        reward = max(-1.0, min(2.0, reward))
        
        # 构建元数据
        metadata = {
            "score": score,
            "max_score": max_score,
            "base_reward": base_reward,
            "rewrite_counter": rewrite_counter,
            "total_steps": total_steps,
            "done": done,
            "success": score == max_score if max_score > 0 else False,
        }
        
        return RewardOutput(reward=reward, metadata=metadata)


class RewardDebugGymWithPatchFn:
    """
    基于补丁质量的Debug-Gym奖励函数。
    
    除了测试通过率外，还考虑补丁的质量（例如补丁大小、代码质量等）。
    """
    
    def __init__(self, config: RewardConfig | None = None):
        """
        初始化基于补丁的Debug-Gym奖励函数。
        
        Args:
            config: 奖励配置对象
        """
        self.config = config or RewardConfig()
        self.base_reward_fn = RewardDebugGymFn(config)
        
        # 补丁质量权重
        self.patch_size_penalty = 0.001  # 每行改动的惩罚
        self.max_patch_penalty = 0.2  # 最大补丁惩罚
    
    def _analyze_patch(self, patch: str) -> dict:
        """
        分析git补丁。
        
        Args:
            patch: git diff输出的补丁内容
            
        Returns:
            包含补丁分析结果的字典
        """
        if not patch:
            return {
                "lines_added": 0,
                "lines_removed": 0,
                "files_changed": 0,
            }
        
        lines = patch.split("\n")
        lines_added = 0
        lines_removed = 0
        files_changed = set()
        
        for line in lines:
            if line.startswith("+++") or line.startswith("---"):
                # 提取文件名
                parts = line.split()
                if len(parts) > 1:
                    filename = parts[1]
                    if filename != "/dev/null":
                        files_changed.add(filename)
            elif line.startswith("+") and not line.startswith("+++"):
                lines_added += 1
            elif line.startswith("-") and not line.startswith("---"):
                lines_removed += 1
        
        return {
            "lines_added": lines_added,
            "lines_removed": lines_removed,
            "files_changed": len(files_changed),
            "total_changes": lines_added + lines_removed,
        }
    
    def __call__(
        self, 
        task_info: dict | RewardInput, 
        action: str | None = None
    ) -> RewardOutput:
        """
        计算包含补丁质量的奖励。
        
        Args:
            task_info: 任务信息字典或RewardInput对象
            action: agent的响应（可选）
            
        Returns:
            RewardOutput对象，包含奖励值和元数据
        """
        if isinstance(task_info, RewardInput):
            task_info = task_info.task_info
        
        # 获取基础奖励
        base_result = self.base_reward_fn(task_info, action)
        reward = base_result.reward
        metadata = base_result.metadata
        
        # 分析补丁（如果可用）
        patch = task_info.get("patch", "")
        if patch:
            patch_analysis = self._analyze_patch(patch)
            
            # 根据补丁大小应用惩罚
            total_changes = patch_analysis["total_changes"]
            patch_penalty = min(
                self.patch_size_penalty * total_changes,
                self.max_patch_penalty
            )
            reward -= patch_penalty
            
            # 更新元数据
            metadata.update({
                "patch_analysis": patch_analysis,
                "patch_penalty": patch_penalty,
            })
        
        return RewardOutput(reward=reward, metadata=metadata)


def debug_gym_reward_fn(task_info: dict, action: str | None = None) -> RewardOutput:
    """
    Debug-Gym任务的标准奖励函数。
    
    这是一个便捷函数，用于在训练中使用。
    
    Args:
        task_info: 任务信息字典
        action: agent的响应（可选）
        
    Returns:
        RewardOutput对象
    """
    reward_config = RewardConfig()
    reward_fn = RewardDebugGymFn(reward_config)
    return reward_fn(task_info, action)


def debug_gym_with_patch_reward_fn(
    task_info: dict, 
    action: str | None = None
) -> RewardOutput:
    """
    基于补丁质量的Debug-Gym奖励函数。
    
    Args:
        task_info: 任务信息字典
        action: agent的响应（可选）
        
    Returns:
        RewardOutput对象
    """
    reward_config = RewardConfig()
    reward_fn = RewardDebugGymWithPatchFn(reward_config)
    return reward_fn(task_info, action)




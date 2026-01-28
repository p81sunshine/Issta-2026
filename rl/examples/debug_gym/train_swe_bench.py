"""
SWE-bench Debug-Gym训练脚本

这个脚本展示了如何使用rLLM框架训练SWE-bench Debug-Gym agent。
"""
import argparse
import os
import sys
from pathlib import Path

# 添加rllm到路径
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from rllm.trainer.verl.train_agent_ppo import main as train_ppo


def parse_args():
    parser = argparse.ArgumentParser(description="Train SWE-bench Debug-Gym Agent with PPO")
    
    # 基础参数
    parser.add_argument(
        "--config",
        type=str,
        default="rllm/trainer/config/swe_bench_debug_gym_trainer.yaml",
        help="训练配置文件路径"
    )
    
    parser.add_argument(
        "--model_path",
        type=str,
        default="~/models/deepseek-llm-7b-chat",
        help="基础模型路径"
    )
    
    parser.add_argument(
        "--dataset_id",
        type=str,
        default="SWE-bench/SWE-bench_Verified",
        help="SWE-bench数据集ID"
    )
    
    parser.add_argument(
        "--split",
        type=str,
        default="test",
        help="数据集分割（train/test）"
    )
    
    parser.add_argument(
        "--instance_id",
        type=str,
        default=None,
        help="具体的任务实例ID（如django__django-11099）"
    )
    
    parser.add_argument(
        "--output_dir",
        type=str,
        default="checkpoints/swe_bench_debug_gym_rl",
        help="输出目录"
    )
    
    parser.add_argument(
        "--experiment_name",
        type=str,
        default="swe_bench_ppo",
        help="实验名称"
    )
    
    parser.add_argument(
        "--total_epochs",
        type=int,
        default=50,
        help="训练轮数"
    )
    
    parser.add_argument(
        "--n_gpus",
        type=int,
        default=8,
        help="每个节点的GPU数量"
    )
    
    parser.add_argument(
        "--max_steps",
        type=int,
        default=50,
        help="每个episode的最大步数"
    )
    
    parser.add_argument(
        "--enable_pdb",
        action="store_true",
        default=True,
        help="启用pdb调试器工具"
    )
    
    parser.add_argument(
        "--debug_gym_path",
        type=str,
        default="/home/jiaxingliu/workspace/swe-pdb/debug-gym",
        help="Debug-Gym安装路径"
    )
    
    return parser.parse_args()


def main():
    args = parse_args()
    
    # 设置环境变量
    os.environ["DEBUG_GYM_PATH"] = args.debug_gym_path
    
    # 构建配置覆盖
    config_overrides = [
        f"actor_rollout_ref.model.path={args.model_path}",
        f"critic.model.path={args.model_path}",
        f"trainer.default_local_dir={args.output_dir}",
        f"trainer.experiment_name={args.experiment_name}",
        f"trainer.total_epochs={args.total_epochs}",
        f"trainer.n_gpus_per_node={args.n_gpus}",
        f"agent.max_steps={args.max_steps}",
        f"env.env_args.max_steps={args.max_steps}",
        f"env.env_args.dataset_id={args.dataset_id}",
        f"env.env_args.split={args.split}",
        f"env.env_args.enable_pdb={args.enable_pdb}",
    ]
    
    # 如果指定了instance_id，添加到配置
    if args.instance_id:
        config_overrides.append(f"env.env_args.instance_id={args.instance_id}")
    
    # 将配置覆盖转换为sys.argv格式
    sys.argv = [
        sys.argv[0],
        args.config,
    ]
    for override in config_overrides:
        sys.argv.extend(["--override", override])
    
    # 运行训练
    print("=" * 80)
    print("开始SWE-bench Debug-Gym PPO训练")
    print("=" * 80)
    print(f"模型: {args.model_path}")
    print(f"数据集: {args.dataset_id}")
    print(f"分割: {args.split}")
    print(f"任务ID: {args.instance_id or '随机选择'}")
    print(f"输出目录: {args.output_dir}")
    print(f"实验名称: {args.experiment_name}")
    print(f"训练轮数: {args.total_epochs}")
    print(f"最大步数: {args.max_steps}")
    print(f"启用PDB: {args.enable_pdb}")
    print("=" * 80)
    
    train_ppo()


if __name__ == "__main__":
    main()



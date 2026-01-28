"""
准备Debug-Gym训练数据

这个脚本将debug-gym格式的数据转换为rllm训练所需的格式。
"""
import argparse
import json
import os
import sys
from pathlib import Path

import pandas as pd
from tqdm import tqdm

# 添加debug-gym到路径
DEBUG_GYM_PATH = os.environ.get(
    "DEBUG_GYM_PATH", 
    "/home/jiaxingliu/workspace/swe-pdb/debug-gym"
)
sys.path.insert(0, DEBUG_GYM_PATH)

try:
    from debug_gym.gym.envs.mini_nightmare import MiniNightmareEnv
    from debug_gym.gym.envs.swe_bench import SWEBenchEnv
    from debug_gym.gym.envs.swe_smith import SWESmithEnv
except ImportError as e:
    print(f"警告：无法导入debug-gym环境: {e}")
    MiniNightmareEnv = None
    SWEBenchEnv = None
    SWESmithEnv = None


def load_mini_nightmare_data():
    """加载Mini Nightmare数据集。"""
    if MiniNightmareEnv is None:
        raise ImportError("无法导入MiniNightmareEnv")
    
    env = MiniNightmareEnv()
    problems = list(env.dataset.keys())
    
    data = []
    for problem_name in tqdm(problems, desc="加载Mini Nightmare数据"):
        problem_data = env.dataset[problem_name]
        data.append({
            "problem_id": problem_name,
            "problem_statement": f"Debug the following Python code:\n\n{problem_data}",
            "data_source": "mini_nightmare",
            "repo_path": None,
            "entrypoint": "python -m pytest -sq .",
        })
    
    return data


def load_swebench_data(split="test", max_samples=None):
    """加载SWE-bench数据集。"""
    if SWEBenchEnv is None:
        raise ImportError("无法导入SWEBenchEnv")
    
    env = SWEBenchEnv(split=split)
    problems = list(env.dataset.keys())[:max_samples] if max_samples else list(env.dataset.keys())
    
    data = []
    for problem_name in tqdm(problems, desc=f"加载SWE-bench {split}数据"):
        problem_data = env.dataset[problem_name]
        data.append({
            "problem_id": problem_name,
            "problem_statement": problem_data.get("problem_statement", ""),
            "data_source": "swebench",
            "repo_path": problem_data.get("repo", None),
            "entrypoint": problem_data.get("test_cmd", "python -m pytest -sq ."),
        })
    
    return data


def load_swesmith_data(max_samples=None):
    """加载SWE-smith数据集。"""
    if SWESmithEnv is None:
        raise ImportError("无法导入SWESmithEnv")
    
    env = SWESmithEnv()
    problems = list(env.dataset.keys())[:max_samples] if max_samples else list(env.dataset.keys())
    
    data = []
    for problem_name in tqdm(problems, desc="加载SWE-smith数据"):
        problem_data = env.dataset[problem_name]
        data.append({
            "problem_id": problem_name,
            "problem_statement": problem_data.get("problem_statement", ""),
            "data_source": "swesmith",
            "repo_path": problem_data.get("repo", None),
            "entrypoint": problem_data.get("test_cmd", "python -m pytest -sq ."),
        })
    
    return data


def split_data(data, train_ratio=0.8):
    """将数据分割为训练集和验证集。"""
    import random
    random.shuffle(data)
    
    split_idx = int(len(data) * train_ratio)
    train_data = data[:split_idx]
    val_data = data[split_idx:]
    
    return train_data, val_data


def save_to_parquet(data, output_path):
    """保存数据为parquet格式。"""
    df = pd.DataFrame(data)
    df.to_parquet(output_path, index=False)
    print(f"保存了 {len(data)} 条数据到 {output_path}")


def main():
    parser = argparse.ArgumentParser(description="准备Debug-Gym训练数据")
    parser.add_argument(
        "--data_source",
        type=str,
        choices=["mini_nightmare", "swebench", "swesmith", "all"],
        default="mini_nightmare",
        help="数据源"
    )
    parser.add_argument(
        "--output_dir",
        type=str,
        default="~/data/debug_gym",
        help="输出目录"
    )
    parser.add_argument(
        "--train_ratio",
        type=float,
        default=0.8,
        help="训练集比例"
    )
    parser.add_argument(
        "--max_samples",
        type=int,
        default=None,
        help="最大样本数量（用于快速测试）"
    )
    
    args = parser.parse_args()
    
    # 创建输出目录
    output_dir = Path(args.output_dir).expanduser()
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 加载数据
    all_data = []
    
    if args.data_source in ["mini_nightmare", "all"]:
        print("加载Mini Nightmare数据...")
        mini_nightmare_data = load_mini_nightmare_data()
        all_data.extend(mini_nightmare_data)
    
    if args.data_source in ["swebench", "all"]:
        print("加载SWE-bench数据...")
        swebench_data = load_swebench_data(max_samples=args.max_samples)
        all_data.extend(swebench_data)
    
    if args.data_source in ["swesmith", "all"]:
        print("加载SWE-smith数据...")
        swesmith_data = load_swesmith_data(max_samples=args.max_samples)
        all_data.extend(swesmith_data)
    
    print(f"\n总共加载了 {len(all_data)} 条数据")
    
    # 分割数据
    train_data, val_data = split_data(all_data, args.train_ratio)
    print(f"训练集: {len(train_data)} 条")
    print(f"验证集: {len(val_data)} 条")
    
    # 保存数据
    train_path = output_dir / "train.parquet"
    val_path = output_dir / "val.parquet"
    
    save_to_parquet(train_data, train_path)
    save_to_parquet(val_data, val_path)
    
    print("\n数据准备完成！")
    print(f"训练数据: {train_path}")
    print(f"验证数据: {val_path}")


if __name__ == "__main__":
    main()




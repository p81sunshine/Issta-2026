"""
Run Debug-Gym KodCode environment with DebugGymAgent using tasks from a parquet file.

Each parquet row is passed to KodCodeDebugGymEnv.from_dict via AgentExecutionEngine.
"""

import argparse
import asyncio
import os
from pathlib import Path

import pandas as pd
from transformers import AutoTokenizer

from rllm.agents.debug_gym_agent import DebugGymAgent
from rllm.engine.agent_execution_engine import AgentExecutionEngine
from rllm.environments.debug_gym.kodcode_env import KodCodeDebugGymEnv
from rllm.utils import compute_pass_at_k


# Get project root directory
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent.parent.parent


def load_parquet_tasks(parquet_path: Path) -> list[dict]:
    if not parquet_path.exists():
        raise FileNotFoundError(f"Parquet file not found: {parquet_path}")
    df = pd.read_parquet(parquet_path)
    if df.empty:
        raise ValueError(f"Parquet file {parquet_path} has no rows")
    return df.to_dict(orient="records")


def main():
    parser = argparse.ArgumentParser(description="Run Debug-Gym KodCode tasks from parquet")

    # Get model path from environment variable or use default
    default_model = os.environ.get("SWE_PDB_MODEL_PATH", "Qwen/Qwen3-14B")

    parser.add_argument(
        "--parquet_path",
        type=Path,
        default=PROJECT_ROOT / "data/rl_train.parquets",
        help="Path to parquet containing KodCode tasks (with extra_info/files fields)",
    )
    parser.add_argument(
        "--model_name",
        type=str,
        default=default_model,
        help="Model name or endpoint model id (or set SWE_PDB_MODEL_PATH env var)",
    )
    parser.add_argument("--base_url", type=str, default="http://localhost:2331/v1", help="OpenAI-compatible base URL")
    parser.add_argument("--api_key", type=str, default="None", help="API key for the endpoint")
    parser.add_argument("--n_parallel", type=int, default=1, help="Number of parallel agents/envs")
    parser.add_argument("--max_problems", type=int, default=None, help="Max number of problems to run")
    parser.add_argument("--max_steps", type=int, default=60, help="Max env steps")
    args = parser.parse_args()

    tasks = load_parquet_tasks(args.parquet_path)
    tasks = tasks[:args.max_problems]

    tokenizer = AutoTokenizer.from_pretrained(args.model_name)
    sampling_params = {"temperature": 1.0, "model": args.model_name}

    env_args = {
        "backend": "local",
        "show_directory_tree": True,
        "persistent_breakpoints": True,
        "show_current_breakpoints": False,
        "auto_eval_on_rewrite": False,
        "enable_pdb": True,
        "enable_grep": True,
        "enable_bash": False,
        "max_steps": args.max_steps,
        "data_path": str(PROJECT_ROOT / "data")
    }

    engine = AgentExecutionEngine(
        agent_class=DebugGymAgent,
        env_class=KodCodeDebugGymEnv,
        agent_args={"use_tool_call_format": True},
        env_args=env_args,
        engine_name="openai",
        tokenizer=tokenizer,
        sampling_params=sampling_params,
        rollout_engine_args={
            "base_url": args.base_url,
            "api_key": args.api_key,
        },
        config={"rllm": {"disable_thinking": True}},
        n_parallel_agents=args.n_parallel,
        max_response_length=32768,
        max_prompt_length=4096,
        max_steps=args.max_steps,
    )

    results = asyncio.run(engine.execute_tasks(tasks))
    compute_pass_at_k(results)


if __name__ == "__main__":
    main()

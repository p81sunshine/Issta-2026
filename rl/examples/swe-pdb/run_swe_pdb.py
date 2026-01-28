import asyncio
from pathlib import Path

from transformers import AutoTokenizer

from rllm.agents.swe_agent import SWEAgent
from rllm.engine.agent_execution_engine import AgentExecutionEngine
from rllm.environments.swe.swe import SWEEnv
from rllm.utils import compute_pass_at_k


def load_tasks():
    """Load SWE-bench Verified test split if prepared."""
    from rllm.data.dataset import DatasetRegistry

    if DatasetRegistry.dataset_exists("SWE_Bench_Verified", "test"):
        test_dataset = DatasetRegistry.load_dataset("SWE_Bench_Verified", "test")
        return test_dataset.get_data()
    raise ValueError(
        "SWE_Bench_Verified dataset not found. Please run `python prepare_swe_data.py` to create the dataset."
    )


def main():
    model_name = "agentica-org/DeepSWE-Preview"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    sampling_params = {"temperature": 1, "model": model_name}

    engine = AgentExecutionEngine(
        agent_class=SWEAgent,
        env_class=SWEEnv,
        agent_args={},
        env_args={},
        engine_name="openai",
        tokenizer=tokenizer,
        sampling_params=sampling_params,
        rollout_engine_args={
            "base_url": "http://localhost:30000/v1",
            "api_key": "None",
        },
        n_parallel_agents=1,
        max_response_length=65536,
        max_prompt_length=4096,
    )

    tasks = load_tasks()
    results = asyncio.run(engine.execute_tasks(tasks))
    compute_pass_at_k(results)


if __name__ == "__main__":
    main()

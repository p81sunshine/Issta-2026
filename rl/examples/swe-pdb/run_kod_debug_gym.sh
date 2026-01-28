#!/usr/bin/env bash
set -euo pipefail

# Path to the parquet with KodCode tasks
PARQUET_PATH="/home/jiaxingliu/workspace/swe-pdb/rllm/data/rl_train.parquets"

# OpenAI-compatible vLLM endpoint
BASE_URL="http://localhost:2331/v1"
API_KEY="None"

# Model served by the endpoint
MODEL_NAME="/data/jiaxingliu/checkpoints/qwen3-14b/step300/huggingface"

# Parallelism (set to 1 for debugging)
N_PARALLEL=10

# Max env steps
MAX_STEPS=60

PYTHONUNBUFFERED=1 python examples/swe-pdb/run_kod_debug_gym.py \
  --parquet_path "${PARQUET_PATH}" \
  --model_name "${MODEL_NAME}" \
  --base_url "${BASE_URL}" \
  --api_key "${API_KEY}" \
  --n_parallel "${N_PARALLEL}" \
  --max_problems 10 \
  --max_steps "${MAX_STEPS}"

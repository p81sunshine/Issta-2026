#!/bin/bash

# Debug-Gym PPO训练脚本
# 用于启动Debug-Gym agent的强化学习训练

# 设置环境变量
export DEBUG_GYM_PATH="/home/jiaxingliu/workspace/swe-pdb/debug-gym"
export CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6,7

# 基础配置
MODEL_PATH="~/models/deepseek-llm-7b-chat"  # 或使用 Qwen2.5-7B-Instruct
TRAIN_DATA="~/data/debug_gym/train.parquet"
VAL_DATA="~/data/debug_gym/val.parquet"
OUTPUT_DIR="checkpoints/debug_gym_rl/debug_gym_ppo"
EXPERIMENT_NAME="debug_gym_ppo"

# 训练参数
TOTAL_EPOCHS=20
MAX_STEPS=30
N_GPUS=8

# 工具配置
ENABLE_PDB=true
ENABLE_GREP=true

# 运行训练
python examples/debug_gym/train_debug_gym.py \
    --config rllm/trainer/config/debug_gym_trainer.yaml \
    --model_path "$MODEL_PATH" \
    --train_data "$TRAIN_DATA" \
    --val_data "$VAL_DATA" \
    --output_dir "$OUTPUT_DIR" \
    --experiment_name "$EXPERIMENT_NAME" \
    --total_epochs "$TOTAL_EPOCHS" \
    --n_gpus "$N_GPUS" \
    --max_steps "$MAX_STEPS" \
    --enable_pdb \
    --enable_grep \
    --debug_gym_path "$DEBUG_GYM_PATH"




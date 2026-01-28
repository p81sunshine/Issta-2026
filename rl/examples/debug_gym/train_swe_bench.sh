#!/bin/bash

# SWE-bench Debug-Gym PPO训练脚本

set -e  # 遇到错误立即退出

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}===================================================${NC}"
echo -e "${GREEN}  SWE-bench Debug-Gym训练启动器${NC}"
echo -e "${GREEN}===================================================${NC}"

# 环境变量
export DEBUG_GYM_PATH="${DEBUG_GYM_PATH:-/home/jiaxingliu/workspace/swe-pdb/debug-gym}"

# 配置参数
MODEL_PATH="${MODEL_PATH:-~/models/deepseek-llm-7b-chat}"
OUTPUT_DIR="${OUTPUT_DIR:-checkpoints/swe_bench_debug_gym_rl}"
EXPERIMENT_NAME="${EXPERIMENT_NAME:-swe_bench_ppo}"

# SWE-bench配置
DATASET_ID="${DATASET_ID:-SWE-bench/SWE-bench_Verified}"
SPLIT="${SPLIT:-test}"
INSTANCE_ID="${INSTANCE_ID:-}"  # 留空表示随机选择

# 训练参数
TOTAL_EPOCHS="${TOTAL_EPOCHS:-50}"
MAX_STEPS="${MAX_STEPS:-50}"
N_GPUS="${N_GPUS:-8}"

# 检查Docker
echo -e "\n${YELLOW}检查Docker...${NC}"
if ! command -v docker &> /dev/null; then
    echo -e "${RED}错误: Docker未安装${NC}"
    echo "SWE-bench需要Docker支持"
    exit 1
fi

if ! docker ps &> /dev/null; then
    echo -e "${RED}错误: Docker未运行或无权限${NC}"
    echo "请启动Docker或检查权限"
    exit 1
fi

echo -e "${GREEN}✓ Docker可用${NC}"

# 显示配置
echo -e "\n${GREEN}===================================================${NC}"
echo -e "${GREEN}训练配置:${NC}"
echo -e "${GREEN}===================================================${NC}"
echo "模型路径:        $MODEL_PATH"
echo "输出目录:        $OUTPUT_DIR"
echo "实验名称:        $EXPERIMENT_NAME"
echo ""
echo "数据集:          $DATASET_ID"
echo "分割:            $SPLIT"
echo "任务ID:          ${INSTANCE_ID:-随机选择}"
echo ""
echo "训练轮数:        $TOTAL_EPOCHS"
echo "最大步数:        $MAX_STEPS"
echo "GPU数量:         $N_GPUS"
echo -e "${GREEN}===================================================${NC}"

# 确认启动
read -p "$(echo -e ${YELLOW}是否继续? [y/N]: ${NC})" -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}取消训练${NC}"
    exit 0
fi

# 构建训练命令
TRAIN_CMD="python examples/debug_gym/train_swe_bench.py \
    --config rllm/trainer/config/swe_bench_debug_gym_trainer.yaml \
    --model_path $MODEL_PATH \
    --dataset_id $DATASET_ID \
    --split $SPLIT \
    --output_dir $OUTPUT_DIR \
    --experiment_name $EXPERIMENT_NAME \
    --total_epochs $TOTAL_EPOCHS \
    --max_steps $MAX_STEPS \
    --n_gpus $N_GPUS \
    --enable_pdb"

# 如果指定了instance_id，添加到命令
if [ -n "$INSTANCE_ID" ]; then
    TRAIN_CMD="$TRAIN_CMD --instance_id $INSTANCE_ID"
fi

# 运行训练
echo -e "\n${GREEN}启动训练...${NC}"
eval $TRAIN_CMD

# 检查训练结果
if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}===================================================${NC}"
    echo -e "${GREEN}训练完成！${NC}"
    echo -e "${GREEN}===================================================${NC}"
    echo "输出目录: $OUTPUT_DIR"
else
    echo -e "\n${RED}===================================================${NC}"
    echo -e "${RED}训练失败！${NC}"
    echo -e "${RED}===================================================${NC}"
    exit 1
fi



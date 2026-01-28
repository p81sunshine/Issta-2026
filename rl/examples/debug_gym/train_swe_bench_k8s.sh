#!/bin/bash

# SWE-bench Debug-Gym Kubernetes训练脚本
# 使用Kubernetes集群进行大规模SWE-bench训练

set -e

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================================${NC}"
echo -e "${BLUE}  SWE-bench Debug-Gym Kubernetes训练启动器${NC}"
echo -e "${BLUE}========================================================${NC}"

# 环境变量
export DEBUG_GYM_PATH="${DEBUG_GYM_PATH:-/home/jiaxingliu/workspace/swe-pdb/debug-gym}"
export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/config}"

# 配置参数
MODEL_PATH="${MODEL_PATH:-~/models/deepseek-llm-7b-chat}"
OUTPUT_DIR="${OUTPUT_DIR:-checkpoints/swe_bench_debug_gym_k8s}"
EXPERIMENT_NAME="${EXPERIMENT_NAME:-swe_bench_ppo_k8s}"

# SWE-bench配置
DATASET_ID="${DATASET_ID:-SWE-bench/SWE-bench_Verified}"
SPLIT="${SPLIT:-test}"
INSTANCE_ID="${INSTANCE_ID:-}"  # 留空表示随机选择

# K8s配置
K8S_NAMESPACE="${K8S_NAMESPACE:-debug-gym-swe}"
K8S_KUBECONFIG="${K8S_KUBECONFIG:-}"

# 训练参数
TOTAL_EPOCHS="${TOTAL_EPOCHS:-50}"
MAX_STEPS="${MAX_STEPS:-50}"
NNODES="${NNODES:-1}"
N_GPUS="${N_GPUS:-8}"

echo -e "\n${YELLOW}========== 依赖检查 ==========${NC}"

# 检查kubectl
if ! command -v kubectl &> /dev/null; then
    echo -e "${RED}✗ kubectl未安装${NC}"
    echo "请安装kubectl: https://kubernetes.io/docs/tasks/tools/"
    exit 1
fi
echo -e "${GREEN}✓ kubectl已安装${NC}"

# 检查Python Kubernetes客户端
if ! python -c "import kubernetes" &> /dev/null; then
    echo -e "${RED}✗ Kubernetes Python客户端未安装${NC}"
    echo "请运行: pip install kubernetes"
    exit 1
fi
echo -e "${GREEN}✓ Kubernetes Python客户端已安装${NC}"

# 检查debug-gym
if ! python -c "from debug_gym.gym.envs.swe_bench import SWEBenchEnv" &> /dev/null; then
    echo -e "${RED}✗ Debug-Gym未安装或无法导入${NC}"
    echo "请检查DEBUG_GYM_PATH: $DEBUG_GYM_PATH"
    exit 1
fi
echo -e "${GREEN}✓ Debug-Gym已安装${NC}"

# 检查K8s连接
echo -e "\n${YELLOW}========== Kubernetes集群检查 ==========${NC}"
if ! kubectl cluster-info &> /dev/null; then
    echo -e "${RED}✗ 无法连接到Kubernetes集群${NC}"
    echo "请配置kubeconfig或设置KUBECONFIG环境变量"
    exit 1
fi
echo -e "${GREEN}✓ Kubernetes集群连接正常${NC}"

# 显示集群信息
echo -e "${BLUE}集群信息:${NC}"
kubectl cluster-info | head -n 3

# 检查/创建命名空间
echo -e "\n${YELLOW}========== 命名空间检查 ==========${NC}"
if ! kubectl get namespace "$K8S_NAMESPACE" &> /dev/null; then
    echo -e "${YELLOW}创建命名空间: ${K8S_NAMESPACE}${NC}"
    kubectl create namespace "$K8S_NAMESPACE"
else
    echo -e "${GREEN}✓ 命名空间已存在: ${K8S_NAMESPACE}${NC}"
fi

# 显示配置
echo -e "\n${BLUE}========================================================${NC}"
echo -e "${BLUE}训练配置${NC}"
echo -e "${BLUE}========================================================${NC}"
echo -e "${YELLOW}模型配置:${NC}"
echo "  模型路径:      $MODEL_PATH"
echo "  输出目录:      $OUTPUT_DIR"
echo "  实验名称:      $EXPERIMENT_NAME"
echo ""
echo -e "${YELLOW}数据集配置:${NC}"
echo "  数据集:        $DATASET_ID"
echo "  分割:          $SPLIT"
echo "  任务ID:        ${INSTANCE_ID:-随机选择}"
echo ""
echo -e "${YELLOW}Kubernetes配置:${NC}"
echo "  命名空间:      $K8S_NAMESPACE"
echo "  Kubeconfig:    ${K8S_KUBECONFIG:-默认}"
echo ""
echo -e "${YELLOW}训练参数:${NC}"
echo "  训练轮数:      $TOTAL_EPOCHS"
echo "  最大步数:      $MAX_STEPS"
echo "  节点数:        $NNODES"
echo "  每节点GPU:     $N_GPUS"
echo -e "${BLUE}========================================================${NC}"

# 确认启动
echo ""
read -p "$(echo -e ${YELLOW}是否继续启动K8s训练? [y/N]: ${NC})" -n 1 -r
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

# 添加K8s特定配置
TRAIN_CMD="$TRAIN_CMD --override env.env_args.backend=kubernetes"
TRAIN_CMD="$TRAIN_CMD --override env.env_args.k8s_namespace=$K8S_NAMESPACE"
TRAIN_CMD="$TRAIN_CMD --override trainer.nnodes=$NNODES"

if [ -n "$K8S_KUBECONFIG" ]; then
    TRAIN_CMD="$TRAIN_CMD --override env.env_args.k8s_kubeconfig=$K8S_KUBECONFIG"
fi

# 如果指定了instance_id，添加到命令
if [ -n "$INSTANCE_ID" ]; then
    TRAIN_CMD="$TRAIN_CMD --instance_id $INSTANCE_ID"
fi

# 运行训练
echo -e "\n${GREEN}========== 启动训练 ==========${NC}"
echo -e "${BLUE}执行命令:${NC}"
echo "$TRAIN_CMD"
echo ""

eval $TRAIN_CMD

# 检查训练结果
if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}========================================================${NC}"
    echo -e "${GREEN}训练完成！${NC}"
    echo -e "${GREEN}========================================================${NC}"
    echo "输出目录: $OUTPUT_DIR"
    echo ""
    echo "查看运行的Pods:"
    echo "  kubectl get pods -n $K8S_NAMESPACE"
    echo ""
    echo "查看Pod日志:"
    echo "  kubectl logs -f <pod-name> -n $K8S_NAMESPACE"
    echo ""
    echo "清理Pods:"
    echo "  kubectl delete pods -n $K8S_NAMESPACE -l app=debug-gym"
else
    echo -e "\n${RED}========================================================${NC}"
    echo -e "${RED}训练失败！${NC}"
    echo -e "${RED}========================================================${NC}"
    echo ""
    echo "调试步骤:"
    echo "1. 查看Pods状态:"
    echo "   kubectl get pods -n $K8S_NAMESPACE"
    echo ""
    echo "2. 查看Pod详情:"
    echo "   kubectl describe pod <pod-name> -n $K8S_NAMESPACE"
    echo ""
    echo "3. 查看Pod日志:"
    echo "   kubectl logs <pod-name> -n $K8S_NAMESPACE"
    exit 1
fi



#!/bin/bash

# Debug-Gym Kubernetes训练脚本
# 用于在Kubernetes集群上启动Debug-Gym agent的RL训练

set -e  # 遇到错误立即退出

# 颜色输出
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${GREEN}===================================================${NC}"
echo -e "${GREEN}  Debug-Gym Kubernetes训练启动器${NC}"
echo -e "${GREEN}===================================================${NC}"

# 环境变量
export DEBUG_GYM_PATH="${DEBUG_GYM_PATH:-/home/jiaxingliu/workspace/swe-pdb/debug-gym}"
export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/config}"

# 配置参数
MODEL_PATH="${MODEL_PATH:-~/models/deepseek-llm-7b-chat}"
TRAIN_DATA="${TRAIN_DATA:-~/data/debug_gym/train.parquet}"
VAL_DATA="${VAL_DATA:-~/data/debug_gym/val.parquet}"
OUTPUT_DIR="${OUTPUT_DIR:-checkpoints/debug_gym_k8s}"
EXPERIMENT_NAME="${EXPERIMENT_NAME:-debug_gym_ppo_k8s}"

# K8s配置
K8S_NAMESPACE="${K8S_NAMESPACE:-debug-gym}"
K8S_BASE_IMAGE="${K8S_BASE_IMAGE:-python:3.12}"
K8S_KUBECONFIG="${K8S_KUBECONFIG:-}"

# 训练参数
TOTAL_EPOCHS="${TOTAL_EPOCHS:-30}"
MAX_STEPS="${MAX_STEPS:-30}"
NNODES="${NNODES:-1}"
N_GPUS="${N_GPUS:-8}"

# 检查依赖
echo -e "\n${YELLOW}检查依赖...${NC}"

if ! command -v kubectl &> /dev/null; then
    echo -e "${RED}错误: kubectl未安装${NC}"
    echo "请安装kubectl: https://kubernetes.io/docs/tasks/tools/"
    exit 1
fi

if ! python -c "import kubernetes" &> /dev/null; then
    echo -e "${RED}错误: Kubernetes Python客户端未安装${NC}"
    echo "请运行: pip install kubernetes"
    exit 1
fi

# 检查K8s连接
echo -e "${YELLOW}检查Kubernetes连接...${NC}"
if ! kubectl cluster-info &> /dev/null; then
    echo -e "${RED}错误: 无法连接到Kubernetes集群${NC}"
    echo "请配置kubeconfig或设置KUBECONFIG环境变量"
    exit 1
fi

echo -e "${GREEN}✓ Kubernetes集群连接正常${NC}"

# 检查/创建命名空间
echo -e "\n${YELLOW}检查命名空间: ${K8S_NAMESPACE}${NC}"
if ! kubectl get namespace "$K8S_NAMESPACE" &> /dev/null; then
    echo -e "${YELLOW}创建命名空间: ${K8S_NAMESPACE}${NC}"
    kubectl create namespace "$K8S_NAMESPACE"
else
    echo -e "${GREEN}✓ 命名空间已存在${NC}"
fi

# 显示配置
echo -e "\n${GREEN}===================================================${NC}"
echo -e "${GREEN}训练配置:${NC}"
echo -e "${GREEN}===================================================${NC}"
echo "模型路径:        $MODEL_PATH"
echo "训练数据:        $TRAIN_DATA"
echo "验证数据:        $VAL_DATA"
echo "输出目录:        $OUTPUT_DIR"
echo "实验名称:        $EXPERIMENT_NAME"
echo ""
echo "K8s命名空间:     $K8S_NAMESPACE"
echo "K8s基础镜像:     $K8S_BASE_IMAGE"
echo ""
echo "训练轮数:        $TOTAL_EPOCHS"
echo "最大步数:        $MAX_STEPS"
echo "节点数:          $NNODES"
echo "每节点GPU数:     $N_GPUS"
echo -e "${GREEN}===================================================${NC}"

# 确认启动
read -p "$(echo -e ${YELLOW}是否继续? [y/N]: ${NC})" -n 1 -r
echo
if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo -e "${YELLOW}取消训练${NC}"
    exit 0
fi

# 运行训练
echo -e "\n${GREEN}启动训练...${NC}"

python examples/debug_gym/train_debug_gym.py \
    --config examples/debug_gym/kubernetes_example.yaml \
    --model_path "$MODEL_PATH" \
    --train_data "$TRAIN_DATA" \
    --val_data "$VAL_DATA" \
    --output_dir "$OUTPUT_DIR" \
    --experiment_name "$EXPERIMENT_NAME" \
    --total_epochs "$TOTAL_EPOCHS" \
    --max_steps "$MAX_STEPS" \
    --override env.env_args.backend="kubernetes" \
    --override env.env_args.k8s_namespace="$K8S_NAMESPACE" \
    --override env.env_args.base_image="$K8S_BASE_IMAGE" \
    --override trainer.nnodes="$NNODES" \
    --override trainer.n_gpus_per_node="$N_GPUS"

# 检查训练结果
if [ $? -eq 0 ]; then
    echo -e "\n${GREEN}===================================================${NC}"
    echo -e "${GREEN}训练完成！${NC}"
    echo -e "${GREEN}===================================================${NC}"
    echo "输出目录: $OUTPUT_DIR"
    echo ""
    echo "查看运行的pods:"
    echo "  kubectl get pods -n $K8S_NAMESPACE"
    echo ""
    echo "查看pod日志:"
    echo "  kubectl logs <pod-name> -n $K8S_NAMESPACE"
    echo ""
    echo "清理资源:"
    echo "  kubectl delete pods -n $K8S_NAMESPACE --all"
else
    echo -e "\n${RED}===================================================${NC}"
    echo -e "${RED}训练失败！${NC}"
    echo -e "${RED}===================================================${NC}"
    echo "请检查日志以了解详细错误信息"
    exit 1
fi




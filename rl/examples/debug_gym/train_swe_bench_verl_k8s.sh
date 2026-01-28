#!/bin/bash

# SWE-bench Debug-Gym VERL训练脚本（Kubernetes版本）
# 基于train_deepswe_14b.sh配置，使用官方HF SWE-bench数据集

set -x

# ==================== 环境配置 ====================

# Kubernetes/Docker 配置
export DOCKER_HOST=unix:///run/user/1001/podman/podman.sock
export PYTHONUNBUFFERED=1

# vLLM 配置
export VLLM_ATTENTION_BACKEND=FLASH_ATTN
export PYTORCH_CUDA_ALLOC_CONF="expandable_segments:False"
export VLLM_USE_V1=1
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export VLLM_ENGINE_ITERATION_TIMEOUT_S=100000000000
export VLLM_LOGGING_LEVEL=DEBUG

# Debug-Gym 配置
export DEBUG_GYM_PATH="${DEBUG_GYM_PATH:-/home/jiaxingliu/workspace/swe-pdb/debug-gym}"
export KUBECONFIG="${KUBECONFIG:-$HOME/.kube/config}"

# ==================== 参数配置 ====================

# 模型配置
MODEL_PATH="${MODEL_PATH:-Qwen/Qwen3-14B}"
LOCAL_FILES_ONLY="${LOCAL_FILES_ONLY:-True}"

# 数据集配置（使用官方HF SWE-bench数据集）
DATASET_TRAIN="${DATASET_TRAIN:-princeton-nlp/SWE-bench}"
DATASET_VAL="${DATASET_VAL:-princeton-nlp/SWE-bench_Verified}"
DATASET_SPLIT="${DATASET_SPLIT:-test}"

# 训练配置
TOTAL_EPOCHS="${TOTAL_EPOCHS:-1000}"
TRAIN_BATCH_SIZE="${TRAIN_BATCH_SIZE:-8}"
VAL_BATCH_SIZE="${VAL_BATCH_SIZE:-128}"
MAX_PROMPT_LENGTH="${MAX_PROMPT_LENGTH:-8192}"
MAX_RESPONSE_LENGTH="${MAX_RESPONSE_LENGTH:-32768}"

# K8s 配置
K8S_NAMESPACE="${K8S_NAMESPACE:-debug-gym-swe}"
NNODES="${NNODES:-1}"
N_GPUS="${N_GPUS:-8}"

# Agent 配置
MAX_STEPS="${MAX_STEPS:-50}"
TRAJECTORY_TIMEOUT="${TRAJECTORY_TIMEOUT:-5400}"

# 实验配置
PROJECT_NAME="${PROJECT_NAME:-debuggym-agent}"
EXPERIMENT_NAME="${EXPERIMENT_NAME:-swe-bench-verl-k8s}"
AGENT_NAME="${AGENT_NAME:-debug_gym_agent}" # sweagent or debug_gym_agent
# 根据agent不同，选择不同的环境
if [[ "$AGENT_NAME" == "sweagent" ]]; then
    ENV_NAME="SWEEnv"
elif [[ "$AGENT_NAME" == "debug_gym_agent" ]]; then
    ENV_NAME="swe_bench_debug_gym"
else
    ENV_NAME="SWEEnv"  # 默认环境
fi

export ENV_NAME



# ==================== 显示配置 ====================

echo ""
echo "=========================================="
echo "       SWE-bench VERL K8s训练配置"
echo "=========================================="
echo "模型配置:"
echo "  模型路径:      $MODEL_PATH"
echo "  本地文件:      $LOCAL_FILES_ONLY"
echo ""
echo "数据集配置:"
echo "  训练数据:      $TRAIN_FILES"
echo "  验证数据:      $VAL_FILES"
echo "  批次大小:      训练=$TRAIN_BATCH_SIZE, 验证=$VAL_BATCH_SIZE"
echo "  提示长度:      $MAX_PROMPT_LENGTH"
echo "  响应长度:      $MAX_RESPONSE_LENGTH"
echo ""
echo "训练配置:"
echo "  总轮数:        $TOTAL_EPOCHS"
echo "  节点数:        $NNODES"
echo "  每节点GPU:     $N_GPUS"
echo ""
echo "Agent配置:"
echo "  最大步数:      $MAX_STEPS"
echo "  轨迹超时:      ${TRAJECTORY_TIMEOUT}s"
echo ""
echo "实验配置:"
echo "  项目名称:      $PROJECT_NAME"
echo "  实验名称:      $EXPERIMENT_NAME"
echo "=========================================="
echo ""

# ==================== 启动训练 ====================

echo "========== 启动VERL训练 =========="

python3 -m rllm.trainer.verl.train_agent_ppo \
    algorithm.adv_estimator=loop \
    data.train_files=/home/jiaxingliu/workspace/swe-pdb/rllm/rllm/data/datasets/SWE_Bench_Verified/test_verl.parquet \
    data.val_files=/home/jiaxingliu/workspace/swe-pdb/rllm/rllm/data/datasets/SWE_Bench_Verified/test_verl.parquet \
    data.train_batch_size=8 \
    data.val_batch_size=128 \
    data.max_prompt_length=$MAX_PROMPT_LENGTH \
    data.max_response_length=$MAX_RESPONSE_LENGTH \
    data.filter_overlong_prompts=True \
    data.filter_overlong_prompts_workers=32 \
    actor_rollout_ref.model.path=$MODEL_PATH \
    +actor_rollout_ref.model.local_files_only=True \
    actor_rollout_ref.hybrid_engine=True \
    actor_rollout_ref.actor.optim.lr=1e-6 \
    actor_rollout_ref.model.use_remove_padding=True \
    actor_rollout_ref.actor.loss_agg_mode=seq-mean-token-sum \
    actor_rollout_ref.actor.ppo_mini_batch_size=8 \
    actor_rollout_ref.actor.use_dynamic_bsz=False \
    actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=1 \
    actor_rollout_ref.rollout.log_prob_use_dynamic_bsz=True \
    actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=1 \
    actor_rollout_ref.actor.ppo_max_token_len_per_gpu=20000 \
    actor_rollout_ref.actor.use_kl_loss=False \
    actor_rollout_ref.actor.clip_ratio_high=0.28 \
    actor_rollout_ref.actor.kl_loss_coef=0.001 \
    actor_rollout_ref.actor.kl_loss_type=low_var_kl \
    actor_rollout_ref.actor.ulysses_sequence_parallel_size=8 \
    actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=1 \
    actor_rollout_ref.model.enable_gradient_checkpointing=True \
    actor_rollout_ref.actor.fsdp_config.param_offload=True \
    actor_rollout_ref.actor.fsdp_config.optimizer_offload=True \
    actor_rollout_ref.rollout.tensor_model_parallel_size=2 \
    actor_rollout_ref.rollout.name=vllm \
    actor_rollout_ref.rollout.mode="async" \
    actor_rollout_ref.rollout.chat_scheduler=verl.schedulers.completions_scheduler.CompletionsScheduler \
    actor_rollout_ref.rollout.enforce_eager=False \
    actor_rollout_ref.rollout.temperature=1.0 \
    actor_rollout_ref.rollout.gpu_memory_utilization=0.8 \
    actor_rollout_ref.rollout.max_num_batched_tokens=32768 \
    actor_rollout_ref.rollout.max_num_seqs=4096 \
    actor_rollout_ref.rollout.n=8 \
    actor_rollout_ref.rollout.val_kwargs.n=1 \
    actor_rollout_ref.rollout.val_kwargs.temperature=0 \
    actor_rollout_ref.rollout.disable_log_stats=False \
    actor_rollout_ref.ref.fsdp_config.param_offload=True \
    actor_rollout_ref.actor.entropy_coeff=0.0 \
    algorithm.kl_ctrl.kl_coef=0.001 \
    algorithm.mask_truncated_samples=False \
    algorithm.clip_advantages=False \
    trainer.critic_warmup=0 \
    trainer.logger=['console','wandb'] \
    trainer.project_name=$PROJECT_NAME \
    trainer.experiment_name=$EXPERIMENT_NAME \
    trainer.val_before_train=False \
    trainer.n_gpus_per_node=8 \
    trainer.nnodes=1 \
    trainer.save_freq=10 \
    trainer.test_freq=30 \
    trainer.max_actor_ckpt_to_keep=2 \
    trainer.max_critic_ckpt_to_keep=1 \
    trainer.default_hdfs_dir=null \
    trainer.total_epochs=$TOTAL_EPOCHS \
    env.name=$ENV_NAME \
    +env.env_args.step_timeout=10 \
    +env.env_args.verbose=True \
    +env.env_args.backend=kubernetes \
    agent.name=$AGENT_NAME \
    +agent.agent_args.use_fn_calling=False \
    agent.max_steps=$MAX_STEPS \
    agent.overlong_filter=True \
    agent.trajectory_timeout=$TRAJECTORY_TIMEOUT \
    agent.async_engine=True

# ==================== 训练结果 ====================

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "✅ 训练完成！"
    echo "=========================================="
    echo ""
    echo "查看Kubernetes Pods:"
    echo "  kubectl get pods -n $K8S_NAMESPACE"
    echo ""
    echo "查看Pod日志:"
    echo "  kubectl logs -f <pod-name> -n $K8S_NAMESPACE"
    echo ""
    echo "清理资源:"
    echo "  kubectl delete pods -n $K8S_NAMESPACE -l app=debug-gym"
else
    echo ""
    echo "=========================================="
    echo "❌ 训练失败！"
    echo "=========================================="
    echo ""
    echo "调试步骤:"
    echo "1. 检查Python环境和依赖"
    echo "2. 检查数据集路径是否正确"
    echo "3. 检查GPU资源是否充足"
    echo "4. 查看日志获取详细错误信息"
    exit 1
fi



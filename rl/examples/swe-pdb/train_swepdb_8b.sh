set -euo pipefail
set -x

# Podman 兼容 Docker API
export DOCKER_HOST=unix:///run/user/1001/podman/podman.sock
export PYTHONUNBUFFERED=1

export VLLM_ATTENTION_BACKEND=FLASH_ATTN
export PYTORCH_CUDA_ALLOC_CONF="expandable_segments:False"
export VLLM_USE_V1=1
export VLLM_ALLOW_LONG_MAX_MODEL_LEN=1
export VLLM_ENGINE_ITERATION_TIMEOUT_S=100000000000

# 启用vLLM详细日志
export VLLM_LOGGING_LEVEL=DEBUG
export CUDA_VISIBLE_DEVICES=4,5,6,7



# ==================================== Train Config ========================
PROJECT_NAME="swepdb-rl"
EXPERIMENT_NAME="swepdb-qwen3-8b-1224-pure"
ENV_NAME="kodcode_debug_gym"
AGENT_NAME="debug_gym_agent"

# Model configuration - set via environment variable or modify here
# Option 1: Use environment variable (recommended)
# export SWE_PDB_MODEL_PATH="/path/to/your/model"
# MODEL_PATH="${SWE_PDB_MODEL_PATH:-/path/to/default/model}"

# Option 2: Directly set the path (modify this line)
MODEL_PATH="${SWE_PDB_MODEL_PATH:-Qwen/Qwen3-8B}"  # Or your local checkpoint path

N_PARALLEL=8
MAX_STEPS=80

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../../.." && pwd)"

TRAIN_DATA_FILES="${PROJECT_ROOT}/data/rl_train.parquets"
VAL_DATA_FILES="${PROJECT_ROOT}/data/rl_test.parquet"
KODCODE_DATA_PATH="${PROJECT_ROOT}/data"

# Checkpoint and rollout paths
# Use environment variable or default to /data/jiaxingliu/checkpoints
SWE_PDB_CHECKPOINT_BASE="${SWE_PDB_CHECKPOINT_BASE:-/data/jiaxingliu/checkpoints}"
CHECKPOINT_DIR="${SWE_PDB_CHECKPOINT_BASE}/${PROJECT_NAME}/${EXPERIMENT_NAME}"
ROLLOUT_DATA_DIR="${PROJECT_ROOT}/train_trajectories/rollout/${PROJECT_NAME}/${EXPERIMENT_NAME}"
VALIDATION_DATA_DIR="${PROJECT_ROOT}/train_trajectories/val/${PROJECT_NAME}/${EXPERIMENT_NAME}"


# Find the directory where rllm package is located
RLLM_DIR=$(python3 -c "import rllm; import os; print(os.path.dirname(os.path.dirname(rllm.__file__)))")

    # data.train_files=${RLLM_DIR}/data/swe/R2E_Gym_Subset.parquet \
    # data.val_files=${RLLM_DIR}/data/swe/SWE_Bench_Verified.parquet \
python3 -m rllm.trainer.verl.train_agent_ppo \
    +ray_init.num_cpus=64 \
    algorithm.adv_estimator=grpo \
    data.train_files=$TRAIN_DATA_FILES \
    data.val_files=$VAL_DATA_FILES \
    data.train_batch_size=32 \
    data.val_batch_size=128 \
    data.max_prompt_length=4096 \
    data.max_response_length=24000 \
    data.filter_overlong_prompts=True \
    data.filter_overlong_prompts_workers=64 \
    actor_rollout_ref.model.path=$MODEL_PATH \
    +actor_rollout_ref.model.local_files_only=True \
    actor_rollout_ref.hybrid_engine=True \
    actor_rollout_ref.actor.optim.lr=1e-6 \
    actor_rollout_ref.model.use_remove_padding=True \
    actor_rollout_ref.actor.loss_agg_mode=seq-mean-token-sum \
    actor_rollout_ref.actor.ppo_mini_batch_size=32 \
    actor_rollout_ref.actor.use_dynamic_bsz=False \
    actor_rollout_ref.actor.ppo_micro_batch_size_per_gpu=1 \
    actor_rollout_ref.rollout.log_prob_use_dynamic_bsz=True \
    actor_rollout_ref.rollout.log_prob_micro_batch_size_per_gpu=1 \
    actor_rollout_ref.actor.ppo_max_token_len_per_gpu=20000 \
    actor_rollout_ref.actor.use_kl_loss=False \
    actor_rollout_ref.actor.clip_ratio_high=0.28 \
    actor_rollout_ref.actor.kl_loss_coef=0.001 \
    actor_rollout_ref.actor.kl_loss_type=low_var_kl \
    actor_rollout_ref.actor.ulysses_sequence_parallel_size=2 \
    actor_rollout_ref.model.enable_gradient_checkpointing=True \
    actor_rollout_ref.actor.fsdp_config.param_offload=True \
    actor_rollout_ref.actor.fsdp_config.optimizer_offload=True \
    actor_rollout_ref.rollout.tensor_model_parallel_size=2 \
    actor_rollout_ref.rollout.name=vllm \
    actor_rollout_ref.rollout.mode="async" \
    actor_rollout_ref.rollout.enforce_eager=False \
    actor_rollout_ref.rollout.temperature=1.0 \
    actor_rollout_ref.rollout.gpu_memory_utilization=0.7 \
    actor_rollout_ref.rollout.max_num_batched_tokens=32768 \
    actor_rollout_ref.rollout.max_num_seqs=2048 \
    actor_rollout_ref.rollout.n=$N_PARALLEL \
    actor_rollout_ref.rollout.val_kwargs.n=1 \
    actor_rollout_ref.rollout.val_kwargs.temperature=1 \
    actor_rollout_ref.rollout.disable_log_stats=False \
    actor_rollout_ref.ref.fsdp_config.param_offload=True \
    actor_rollout_ref.actor.entropy_coeff=0.0 \
    algorithm.kl_ctrl.kl_coef=0.001 \
    rllm.mask_truncated_samples=False \
    rllm.disable_thinking=True \
    trainer.critic_warmup=0 \
    trainer.logger=['console','wandb'] \
    trainer.project_name=$PROJECT_NAME \
    trainer.experiment_name=$EXPERIMENT_NAME \
    trainer.val_before_train=False \
    trainer.n_gpus_per_node=4 \
    trainer.nnodes=1 \
    trainer.save_freq=20 \
    trainer.test_freq=5 \
    trainer.max_actor_ckpt_to_keep=1 \
    trainer.max_critic_ckpt_to_keep=1 \
    trainer.default_local_dir=$CHECKPOINT_DIR \
    trainer.default_hdfs_dir=null \
    trainer.rollout_data_dir=$ROLLOUT_DATA_DIR \
    trainer.validation_data_dir=$VALIDATION_DATA_DIR \
    rllm.env.name=$ENV_NAME \
    +rllm.env.env_args.backend=local \
    +rllm.env.env_args.show_directory_tree=True \
    +rllm.env.env_args.persistent_breakpoints=True \
    +rllm.env.env_args.show_current_breakpoints=False \
    +rllm.env.env_args.auto_eval_on_rewrite=False \
    +rllm.env.env_args.enable_pdb=True \
    +rllm.env.env_args.enable_grep=True \
    +rllm.env.env_args.enable_bash=False \
    +rllm.env.env_args.data_path=$KODCODE_DATA_PATH \
    rllm.agent.name=$AGENT_NAME \
    +rllm.agent.agent_args.use_tool_call_format=True \
    rllm.agent.max_steps=$MAX_STEPS \
    rllm.agent.overlong_filter=True \
    rllm.agent.trajectory_timeout=5400 \
    trainer.total_epochs=5 \
    +rllm.agent.engine_args.n_parallel_agents=32 \
    +rllm.agent.engine_args.max_workers=128 \

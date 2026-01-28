#!/bin/bash
set -x

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PROJECT_ROOT="$(cd "$SCRIPT_DIR" && pwd )"

# Fixed configuration
nproc_per_node=4
PROJECT_NAME=swe-pdb-sft
EXP_NAME=swe-pdb-qwen3-14b-1213

# Checkpoint path - use environment variable or default
SWE_PDB_CHECKPOINT_BASE="${SWE_PDB_CHECKPOINT_BASE:-/data/jiaxingliu/checkpoints}"
save_path=${SWE_PDB_CHECKPOINT_BASE}/${PROJECT_NAME}/${EXP_NAME}

export CUDA_VISIBLE_DEVICES=4,5,6,7

torchrun \
    --nnodes=1 \
    --nproc_per_node=$nproc_per_node \
    --rdzv_backend=c10d \
    --rdzv_endpoint=localhost:29505 \
     -m verl.trainer.fsdp_sft_trainer \
    data.train_files=${PROJECT_ROOT}/data/train.parquet \
    data.val_files=${PROJECT_ROOT}/data/test.parquet \
    data.train_batch_size=8 \
    data.micro_batch_size_per_gpu=1 \
    data.max_length=23000 \
    data.multiturn.enable=true \
    data.multiturn.messages_key=messages \
    data.multiturn.enable_thinking_key=enable_thinking \
    data.truncation=right \
    optim.lr=1e-5 \
    model.partial_pretrain=Qwen/Qwen3-14B \
    model.use_liger=true \
    trainer.default_local_dir=$save_path \
    trainer.project_name=${PROJECT_NAME} \
    trainer.experiment_name=${EXP_NAME} \
    trainer.logger='["console","wandb"]' \
    trainer.total_epochs=2 \
    trainer.n_gpus_per_node=4 \
    trainer.save_freq=100 \
    trainer.test_freq=50 \
    ulysses_sequence_parallel_size=4 \
    use_remove_padding=true

    # +data.apply_chat_template_kwargs.enable_thinking=false \

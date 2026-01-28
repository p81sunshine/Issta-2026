# SWE-PDB SFT Training

Supervised Fine-Tuning (SFT) training scripts for SWE-PDB models using verl framework.

## Requirements

- Python >= 3.10
- CUDA-capable GPUs (2-8 GPUs depending on model size)
- PyTorch with FSDP support
- verl training framework

## Installation

> **Note:** For complete environment setup and LLM configuration, please refer to the [swe-pdb-agent README](../swe-pdb-agent/README.md).

```bash
# Option 1: Use the r2llm conda environment (recommended)
conda activate r2llm

# Option 2: Create new environment
conda create -n swe-pdb-sft python=3.10
conda activate swe-pdb-sft

# Install dependencies (if needed)
pip install verl
```

See [swe-pdb-agent README](../swe-pdb-agent/README.md) for:
- Detailed conda environment setup from `environment.yml`
- Alternative installation methods (requirements.txt)
- LLM configuration (API keys, endpoints)

## Project Structure

```
sft/
├── run_qwen3_4b.sh         # 4B model training script
├── run_qwen3_8b.sh         # 8B model training script
├── run_qwen3_14b.sh        # 14B model training script
├── run_qwen3_14b_lora.sh   # 14B model with LoRA
├── run_qwen3_8b_ray.sh     # 8B model with Ray backend
├── data/                   # Training data
│   ├── train.parquet       # Training data (46MB)
│   └── test.parquet        # Validation data (2.4MB)
└── scripts/                # Additional scripts
```

## Usage

### Quick Start

```bash
cd /path/to/sft

# Set checkpoint directory (optional, uses env var or default)
export SWE_PDB_CHECKPOINT_BASE="/path/to/checkpoints"

# Run training
bash run_qwen3_4b.sh
```

### Training Scripts

#### 1. 4B Model Training

```bash
bash run_qwen3_4b.sh
```

Configuration:
- Model: Qwen/Qwen3-4B
- GPUs: 2 (CUDA devices 2,3)
- Batch size: 8
- Max length: 23,000 tokens
- Sequence parallel: 2
- Checkpoint frequency: 500 steps

#### 2. 8B Model Training

```bash
bash run_qwen3_8b.sh
```

Configuration:
- Model: Qwen/Qwen3-8B
- GPUs: 4 (CUDA devices 0,1,2,3)
- Batch size: 8
- Max length: 23,000 tokens
- Sequence parallel: 2
- Checkpoint frequency: 500 steps

#### 3. 14B Model Training

```bash
bash run_qwen3_14b.sh
```

Configuration:
- Model: Qwen/Qwen3-14B
- GPUs: 4 (CUDA devices 4,5,6,7)
- Batch size: 8
- Max length: 23,000 tokens
- Sequence parallel: 4
- Checkpoint frequency: 100 steps

#### 4. 14B Model with LoRA

```bash
bash run_qwen3_14b_lora.sh
```

Training with Low-Rank Adaptation for memory efficiency.

#### 5. 8B Model with Ray Backend

```bash
bash run_qwen3_8b_ray.sh
```

Training using Ray for distributed training.

## Configuration

### Environment Variables

```bash
# Set checkpoint base directory (optional)
export SWE_PDB_CHECKPOINT_BASE="/data/jiaxingliu/checkpoints"

# If not set, defaults to: /data/jiaxingliu/checkpoints
```

### Edit Scripts Directly

Each script can be customized by editing these variables:

```bash
# Project and experiment names
PROJECT_NAME="swe-pdb-sft"
EXP_NAME="swe-pdb-qwen3-4b-1213"

# Checkpoint path
save_path=${SWE_PDB_CHECKPOINT_BASE}/${PROJECT_NAME}/${EXP_NAME}

# GPU configuration
export CUDA_VISIBLE_DEVICES=0,1,2,3

# Training parameters
nproc_per_node=4  # Number of processes
data.train_batch_size=8
data.max_length=23000
optim.lr=1e-5
trainer.total_epochs=2
```

### GPU Configuration

Edit the `CUDA_VISIBLE_DEVICES` line in each script:

```bash
export CUDA_VISIBLE_DEVICES=0,1,2,3  # Use GPUs 0-3
```

## Training Parameters

### Data Configuration
- `train_files`: Path to training parquet (relative to project root)
- `val_files`: Path to validation parquet (relative to project root)
- `train_batch_size`: Global training batch size (default: 8)
- `micro_batch_size_per_gpu`: Per-GPU micro batch size (default: 1)
- `max_length`: Maximum sequence length (23,000 tokens)

### Model Configuration
- `partial_pretrain`: Base model path (e.g., Qwen/Qwen3-4B)
- `use_liger`: Enable Liger kernel for efficiency
- `use_remove_padding`: Remove padding for efficiency

### Training Configuration
- `lr`: Learning rate (1e-5)
- `total_epochs`: Number of training epochs (2)
- `save_freq`: Checkpoint saving frequency
- `test_freq`: Validation frequency
- `max_ckpt_to_keep`: Maximum checkpoints to keep

### Sequence Parallel
- `ulysses_sequence_parallel_size`: Sequence parallel size
  - 4B model: 2
  - 8B model: 2
  - 14B model: 4

## Output

Training outputs are saved to:
- **Checkpoints**: `$save_path/global_step_*/huggingface/`
- **Logs**: Console output + WandB (if enabled)
- **Project**: `$PROJECT_NAME`
- **Experiment**: `$EXP_NAME`

Example structure:
```
/data/jiaxingliu/checkpoints/swe-pdb-sft/swe-pdb-qwen3-4b-1213/
├── global_step_500/
│   └── huggingface/
│       ├── config.json
│       ├── model.safetensors
│       └── ...
├── global_step_1000/
└── ...
```

## Data Format

The training data uses parquet format with the following structure:
- `messages`: List of message dictionaries
- `enable_thinking`: Boolean flag for thinking mode

## Monitoring

Training progress can be monitored via:
1. **Console output**: Real-time training metrics
2. **WandB**: Dashboard with detailed metrics (if enabled)
3. **Checkpoint files**: Model checkpoints saved periodically

## Troubleshooting

### CUDA Out of Memory
- Reduce `data.train_batch_size`
- Reduce `ulysses_sequence_parallel_size`
- Use gradient accumulation

### Slow Training
- Increase `ulysses_sequence_parallel_size`
- Use multiple GPUs
- Enable `use_liger` kernel

### Checkpoint Loading Issues
- Ensure checkpoint path is correct
- Check model configuration matches checkpoint

## Advanced Usage

### Custom Data

To use custom training data:

1. Prepare parquet files with the correct format
2. Copy to `data/` directory
3. Update data paths in training scripts:
```bash
data.train_files=${PROJECT_ROOT}/data/your_data/train.parquet
data.val_files=${PROJECT_ROOT}/data/your_data/test.parquet
```

### Multi-Node Training

For multi-node training, modify the torchrun parameters:
```bash
torchrun \
    --nnodes=2 \
    --nproc_per_node=4 \
    --rdzv_backend=c10d \
    --rdzv_endpoint=<master_node>:29505 \
    ...
```

## Related Projects

This repository is part of the SWE-PDB project. See also:

- **[SWE-PDB Agent](../swe-pdb-agent/README.md)** - Interactive debugging framework for evaluation
- **[RL Training](../rl/README.md)** - Reinforcement learning training code

All three components share the same `r2llm` conda environment.

## License

This project follows the license of the verl framework.

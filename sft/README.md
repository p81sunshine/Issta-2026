# SWE-PDB SFT Training

Supervised Fine-Tuning (SFT) training scripts for SWE-PDB models using verl framework.

## Requirements

- Python >= 3.10
- CUDA-capable GPUs (2-4 GPUs depending on model size)
- PyTorch with FSDP support
- verl training framework

## Installation

> **Note:** For complete environment setup and LLM configuration, please refer to the [swe-pdb-agent README](../swe-pdb-agent/README.md).

```bash
# Use the r2llm conda environment (recommended)
conda activate r2llm
```

## Reproduction Guide

### Quick Start

```bash
cd sft

# Set checkpoint directory (optional)
export SWE_PDB_CHECKPOINT_BASE="/path/to/checkpoints"

# Run training
bash run_qwen3_4b.sh
```

### Training Scripts

#### 1. 4B Model Training

```bash
bash run_qwen3_4b.sh
```

**Configuration:**
- Model: Qwen/Qwen3-4B
- GPUs: 2 (CUDA devices 2,3)
- Training data: `data/train.parquet` (46MB)
- Validation data: `data/test.parquet` (2.4MB)
- Batch size: 8
- Max length: 23,000 tokens
- Learning rate: 1e-5
- Epochs: 2

#### 2. 8B Model Training

```bash
bash run_qwen3_8b.sh
```

**Configuration:**
- Model: Qwen/Qwen3-8B
- GPUs: 4 (CUDA devices 0,1,2,3)
- Training data: `data/train.parquet` (46MB)
- Validation data: `data/test.parquet` (2.4MB)
- Batch size: 8
- Max length: 23,000 tokens
- Learning rate: 1e-5
- Epochs: 2

#### 3. 14B Model Training

```bash
bash run_qwen3_14b.sh
```

**Configuration:**
- Model: Qwen/Qwen3-14B
- GPUs: 4 (CUDA devices 4,5,6,7)
- Training data: `data/train.parquet` (46MB)
- Validation data: `data/test.parquet` (2.4MB)
- Batch size: 8
- Max length: 23,000 tokens
- Learning rate: 1e-5
- Epochs: 2

## Configuration

### Environment Variables

```bash
# Set checkpoint base directory
export SWE_PDB_CHECKPOINT_BASE="/path/to/checkpoints"

# If not set, defaults to: /data/jiaxingliu/checkpoints
```

### GPU Configuration

Edit the `CUDA_VISIBLE_DEVICES` line in each script:

```bash
export CUDA_VISIBLE_DEVICES=0,1,2,3  # Use GPUs 0-3
```

## Output

Training outputs are saved to:
```
${SWE_PDB_CHECKPOINT_BASE}/swe-pdb-sft/${EXP_NAME}/
├── global_step_500/
│   └── huggingface/
│       ├── config.json
│       ├── model.safetensors
│       └── ...
├── global_step_1000/
└── ...
```

## Troubleshooting

### CUDA Out of Memory
- Reduce `data.train_batch_size` in the script
- Use fewer GPUs or smaller model

### Slow Training
- Increase `ulysses_sequence_parallel_size`
- Use multiple GPUs
- Enable `use_liger` kernel (already enabled by default)

### Checkpoint Loading Issues
- Ensure checkpoint path is correct
- Check model configuration matches checkpoint

## Related Projects

This repository is part of the SWE-PDB project. See also:

- **[SWE-PDB Agent](../swe-pdb-agent/README.md)** - Interactive debugging framework for evaluation
- **[RL Training](../rl/README.md)** - Reinforcement learning training code

All three components share the same `r2llm` conda environment.

## License

This project follows the license of the verl framework.

# SWE-PDB RL Training

Reinforcement Learning training code for SWE-PDB agent, based on RLLM framework.

## Requirements

- Python >= 3.10
- CUDA-capable GPUs (recommend 4+ GPUs for 14B models)
- Ray for distributed training
- vLLM for model inference

## Installation

> **Note:** For complete environment setup and LLM configuration, please refer to the [swe-pdb-agent README](../swe-pdb-agent/README.md).

```bash
# Option 1: Use the r2llm conda environment (recommended)
conda activate r2llm

# Option 2: Create new environment
conda create -n swe-pdb-rl python=3.10
conda activate swe-pdb-rl

# Install RLLM framework
pip install -e .
```

See [swe-pdb-agent README](../swe-pdb-agent/README.md) for:
- Detailed conda environment setup from `environment.yml`
- Alternative installation methods (requirements.txt)
- LLM configuration (API keys, endpoints)

## Project Structure

```
rl/
├── examples/swe-pdb/     # Main training scripts and configs
│   ├── train_swepdb_4b.sh       # 4B model training script
│   ├── train_swepdb_8b.sh       # 8B model training script
│   ├── train_swepdb_14b.sh      # 14B model training script
│   ├── train_swepdb_14b_rewrite.sh  # 14B rewrite-only variant
│   ├── train_swepdb_wrapper.sh  # Wrapper for distributed training
│   ├── run_kod_debug_gym.py     # Run KodCode environment evaluation
│   └── run_swe_pdb.py           # Run SWE-PDB evaluation
├── data/               # Training data
│   ├── rl_train.parquets            # Training trajectories
│   └── rl_test.parquet               # Validation data
├── rllm/              # RLLM framework code
│   ├── agents/       # Agent implementations
│   ├── environments/ # Environment wrappers
│   ├── engine/       # Training engine
│   └── trainer/      # Training algorithms (PPO, etc.)
└── train_trajectories/ # Output directory for rollouts (not included)
```

## Usage

### Training Scripts

#### 1. 4B Model Training

```bash
cd examples/swe-pdb
bash train_swepdb_4b.sh
```

Configuration:
- Model: Qwen3-4B (SFT checkpoint)
- Parallel environments: 8
- Max steps: 80
- GPU requirement: 4 GPUs (CUDA devices 4,5,6,7)

#### 2. 8B Model Training

```bash
cd examples/swe-pdb
bash train_swepdb_8b.sh
```

#### 3. 14B Model Training

```bash
cd examples/swe-pdb
bash train_swepdb_14b.sh
```

#### 4. 14B Rewrite-Only Training (Ablation)

```bash
cd examples/swe-pdb
bash train_swepdb_14b_rewrite.sh
```

### Configuration

The training scripts use environment variables for flexible configuration:

#### Method 1: Using Environment Variables (Recommended)

```bash
# Set model path
export SWE_PDB_MODEL_PATH="/path/to/your/sft/checkpoint"

# Set checkpoint base directory
export SWE_PDB_CHECKPOINT_BASE="/path/to/checkpoints"

# Run training
cd examples/swe-pdb
bash train_swepdb_4b.sh
```

#### Method 2: Edit Scripts Directly

Edit the following variables in the training scripts:

```bash
# Project and experiment names
PROJECT_NAME="swepdb-rl"
EXPERIMENT_NAME="swepdb-qwen3-4b-0115"

# Model path - modify this line
MODEL_PATH="${SWE_PDB_MODEL_PATH:-Qwen/Qwen3-4B}"  # Or your local checkpoint

# Training data paths (automatically set relative to project root)
TRAIN_DATA_FILES="${PROJECT_ROOT}/data/rl_train.parquets"
VAL_DATA_FILES="${PROJECT_ROOT}/data/rl_test.parquet"

# Environment data path (relative to project root)
KODCODE_DATA_PATH="${PROJECT_ROOT}/data"

# Checkpoint directory (uses env var or default)
SWE_PDB_CHECKPOINT_BASE="${SWE_PDB_CHECKPOINT_BASE:-./data/checkpoints}"
CHECKPOINT_DIR="${SWE_PDB_CHECKPOINT_BASE}/${PROJECT_NAME}/${EXPERIMENT_NAME}"

# Rollout output directory (relative to project root)
ROLLOUT_DATA_DIR="${PROJECT_ROOT}/train_trajectories/rollout/${PROJECT_NAME}/${EXPERIMENT_NAME}"

# Training hyperparameters
N_PARALLEL=8          # Number of parallel environments
MAX_STEPS=80          # Maximum environment steps per episode
```

#### GPU Configuration

Edit the `CUDA_VISIBLE_DEVICES` line in each script to specify which GPUs to use:

```bash
export CUDA_VISIBLE_DEVICES=0,1,2,3  # Use first 4 GPUs
```

### Running Evaluation

#### Run KodCode Environment

```bash
cd examples/swe-pdb
python run_kod_debug_gym.py \
    --parquet_path ../data/rl_train.parquets \
    --model_name /path/to/model \
    --base_url http://localhost:2331/v1 \
    --n_parallel 8 \
    --max_steps 60
```

## Training Algorithm

The training uses Proximal Policy Optimization (PPO) with:
- GRPO Advantage Estimator
- Hybrid Engine: FSDP training + vLLM inference
- Sequence Parallel for long sequences
- Multi-GPU distributed training

## Output

Training outputs:
- **Checkpoints**: `$CHECKPOINT_DIR/`
- **Rollouts**: `$ROLLOUT_DATA_DIR/`
- **Validation**: `$VALIDATION_DATA_DIR/`
- **Logs**: WandB dashboard

## Related Projects

This repository is part of the SWE-PDB project. See also:

- **[SWE-PDB Agent](../swe-pdb-agent/README.md)** - Interactive debugging framework for evaluation
- **[SFT Training](../sft/README.md)** - Supervised fine-tuning scripts for training models

All three components share the same `r2llm` conda environment.

## License

This project follows the license of the RLLM framework.

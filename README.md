# SWE-PDB: Training LLMs to Leverage Debugging Tools

This repository contains the complete codebase for the SWE-PDB project (under review at ISSTA 2026), which focuses on training Large Language Models to effectively leverage Python debugger (PDB) as an interactive tool for software debugging and repair.

## 📁 Project Structure

This repository consists of three main components:

### 1. swe-pdb-agent/
**Interactive Debugging Framework**

An evaluation framework built on top of [debug-gym](https://github.com/microsoft/debug-gym), focusing on debugging tasks using the PDB debugger.

**Key Features:**
- Interactive debugging environment with PDB tool support
- Multiple evaluation datasets (1,600+ debugging problems)
- Support for various agents (debug_agent, rewrite_agent)
- Complete result collection and summarization

**Datasets Included:**
- CaniEdit (106 problems)
- DebugBench (1,128 problems)
- HumanEval Buggy (136 problems)
- MBPP Buggy (255 problems)
- Mini Nightmare (12 problems)
- Synthetic Debug (102 problems)

**Quick Start:**
```bash
cd swe-pdb-agent
conda activate r2llm
python scripts/run.py scripts/config_edit.yaml --agent debug_agent
```

### 2. sft/
**Supervised Fine-Tuning (SFT) Training**

Supervised fine-tuning scripts for training SWE-PDB models using the verl framework.

**Key Features:**
- Training scripts for Qwen3-4B, 8B, and 14B models
- FSDP-based distributed training
- Sequence parallel support for long contexts
- Complete training data included

**Training Data:**
- `train.parquet` (46MB) - Training dataset
- `test.parquet` (2.4MB) - Validation dataset

**Quick Start:**
```bash
cd sft
conda activate r2llm
bash run_qwen3_4b.sh
```

### 3. rl/
**Reinforcement Learning Training**

RL training code for SWE-PDB agents using the RLLM framework with PPO algorithm.

**Key Features:**
- PPO-based RL training with GRPO advantage estimation
- Hybrid engine: FSDP training + vLLM inference
- Support for distributed training across multiple GPUs
- Complete training infrastructure included

**Training Data:**
- `rl_train.parquets` (13MB) - 14,470 training trajectories
- `rl_test.parquet` (133KB) - Validation dataset

**Quick Start:**
```bash
cd rl/examples/swe-pdb
conda activate r2llm
bash train_swepdb_4b.sh
```

## 🚀 Quick Start Guide

### Environment Setup

All three components share the same `r2llm` conda environment. Set it up once:

```bash
# From the repository root
cd swe-pdb-agent

# Create conda environment from environment file
conda env create -f environment.yml
conda activate r2llm

# Install the project
pip install -e .
```

**Alternative methods** are available. See [swe-pdb-agent README](swe-pdb-agent/README.md) for details.

### LLM Configuration

Configure your LLM API credentials:

```bash
python -m debug_gym.llms.configure
```

This creates a configuration file at `$HOME/.config/debug_gym/llm.yaml`.

## 📖 Reproduction Guide

### Step 1: Evaluate Pre-trained Models

Use the evaluation framework to test existing models:

```bash
cd swe-pdb-agent

# Run on a single dataset
python scripts/run.py scripts/config_edit.yaml --agent debug_agent

# Run with a specific LLM
python scripts/run.py scripts/config_edit.yaml --agent debug_agent \
    -p base.llm_name="gpt-4o"
```

### Step 2: Train Your Own Model (SFT)

Fine-tune a base model on debugging data:

```bash
cd sft

# Set model checkpoint path (optional)
export SWE_PDB_CHECKPOINT_BASE="/path/to/checkpoints"

# Train 4B model (2 GPUs)
bash run_qwen3_4b.sh

# Train 8B model (4 GPUs)
bash run_qwen3_8b.sh

# Train 14B model (4 GPUs)
bash run_qwen3_14b.sh
```

**Expected Output:**
- Checkpoints saved to: `$CHECKPOINT_DIR/global_step_*/huggingface/`
- Training logs in console and WandB

### Step 3: RL Training (Optional)

Further improve your SFT model with reinforcement learning:

```bash
cd rl/examples/swe-pdb

# Set paths
export SWE_PDB_MODEL_PATH="/path/to/your/sft/checkpoint"
export SWE_PDB_CHECKPOINT_BASE="/path/to/checkpoints"

# Train 4B model with RL
bash train_swepdb_4b.sh

# Train 14B model with RL
bash train_swepdb_14b.sh
```

**Key Parameters:**
- `N_PARALLEL=8` - Number of parallel environments
- `MAX_STEPS=80` - Maximum environment steps per episode
- Training uses PPO with GRPO advantage estimation

### Step 4: Evaluate RL-trained Models

After RL training, evaluate your model:

```bash
cd rl/examples/swe-pdb

# Run evaluation
python run_kod_debug_gym.py \
    --parquet_path ../../data/rl_train.parquets \
    --model_name /path/to/your/rl/checkpoint \
    --base_url http://localhost:2331/v1 \
    --n_parallel 8 \
    --max_steps 60
```

## 🔧 Configuration

### Using Environment Variables

All components support flexible configuration via environment variables:

```bash
# Set model path
export SWE_PDB_MODEL_PATH="/path/to/your/model"

# Set checkpoint directory
export SWE_PDB_CHECKPOINT_BASE="/path/to/checkpoints"

# Run any script
bash train_swepdb_4b.sh  # Will use the environment variables
```

### GPU Configuration

Edit the `CUDA_VISIBLE_DEVICES` line in training scripts:

```bash
# Use specific GPUs
export CUDA_VISIBLE_DEVICES=0,1,2,3

# Or in the script files
# sft/run_qwen3_4b.sh: CUDA_VISIBLE_DEVICES=2,3
# sft/run_qwen3_8b.sh: CUDA_VISIBLE_DEVICES=0,1,2,3
# rl/examples/swe-pdb/train_swepdb_4b.sh: CUDA_VISIBLE_DEVICES=4,5,6,7
```

## 📊 Workflow Overview

```
1. Environment Setup (r2llm conda environment)
         ↓
2. SFT Training (sft/)
   - Train on debugging data
   - Produces SFT checkpoints
         ↓
3. RL Training (rl/) [Optional]
   - Improve SFT model with PPO
   - Produces RL checkpoints
         ↓
4. Evaluation (swe-pdb-agent/)
   - Test on multiple datasets
   - Generate results and metrics
```

## 📦 Complete Pipeline Example

```bash
# 1. Setup environment
cd swe-pdb-agent
conda env create -f environment.yml
conda activate r2llm
pip install -e .

# 2. Train SFT model
cd ../sft
export SWE_PDB_CHECKPOINT_BASE="./checkpoints"
bash run_qwen3_4b.sh

# 3. Train RL model (using SFT checkpoint)
cd ../rl/examples/swe-pdb
export SWE_PDB_MODEL_PATH="/path/to/sft/checkpoint"
bash train_swepdb_4b.sh

# 4. Evaluate final model
cd ../../swe-pdb-agent
python scripts/run.py scripts/config_edit.yaml \
    --agent debug_agent \
    -p base.llm_name="/path/to/rl/checkpoint"
```

## 📚 Detailed Documentation

For more detailed information, see:

- **[swe-pdb-agent README](swe-pdb-agent/README.md)** - Evaluation framework details
- **[sft README](sft/README.md)** - SFT training guide
- **[rl README](rl/README.md)** - RL training guide

## 💡 Tips

1. **Start Small**: Begin with 4B models and small datasets for testing
2. **Monitor Training**: Use WandB (configured in scripts) to track training progress
3. **GPU Requirements**:
   - SFT 4B: 2 GPUs
   - SFT 8B/14B: 4 GPUs
   - RL 4B: 4 GPUs
   - RL 14B: 4+ GPUs
4. **Checkpoint Regularly**: Scripts automatically save checkpoints during training
5. **Data Paths**: All data paths are relative - just run from the component directory

## 🐛 Troubleshooting

### CUDA Out of Memory
- Reduce batch size in training scripts
- Use smaller model variants
- Reduce `n_parallel` in RL training

### Import Errors
- Ensure `r2llm` environment is activated
- Reinstall packages: `pip install -e .`

### Data Not Found
- Ensure you're running scripts from their respective directories
- Check that data files exist in the `data/` folders


## 📄 License

This project follows the licenses of the underlying frameworks:
- [debug-gym](https://github.com/microsoft/debug-gym) - MIT License
- [verl](https://github.com/volcengine/verl) - Apache 2.0 License
- [RLLM](https://github.com/volcengine/verl) - Apache 2.0 License

## 🙏 Acknowledgments

This project is built on top of excellent open-source frameworks:
- [Microsoft debug-gym](https://github.com/microsoft/debug-gym) - Interactive debugging environment
- [verl](https://github.com/volcengine/verl) - Verl framework for RL training
- [Qwen](https://github.com/QwenLM/Qwen) - Qwen language models

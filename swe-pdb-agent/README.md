# SWE-PDB-Agent

An interactive debugging framework built on top of [debug-gym](https://github.com/microsoft/debug-gym), focusing on debugging tasks using the PDB debugger.

## Requirements

- Python >= 3.10 (tested with 3.10.18)
- Linux system (PDB tool is fully supported only on Linux)

## Installation

> **Note:** The `r2llm` conda environment created here is also used for [SFT training](../sft/README.md) and [RL training](../rl/README.md). You only need to set up the environment once.

### Option 1: Using conda environment file (Recommended)

```bash
# Create conda environment from environment.yml
conda env create -f environment.yml
conda activate r2llm

# Install the project in development mode
cd swe-pdb-agent
pip install -e .
```

### Option 2: Using pip with requirements.txt

```bash
# Create conda environment
conda create -n swe-pdb-agent python=3.10
conda activate swe-pdb-agent

# Install dependencies
pip install -r requirements.txt

# Install the project in development mode
cd swe-pdb-agent
pip install -e .
```

### Option 3: Manual installation

```bash
# Create conda environment
conda create -n swe-pdb-agent python=3.10
conda activate swe-pdb-agent

# Install dependencies
cd swe-pdb-agent
pip install -e .
```

## LLM Configuration

Create LLM configuration file:

```bash
python -m debug_gym.llms.configure
```

The default configuration file is located at `$HOME/.config/debug_gym/llm.yaml`. Edit this file to add your API credentials.

## Project Structure

```
swe-pdb-agent/
├── scripts/           # Configuration files and launch scripts
│   ├── run.py        # Main entry script
│   └── config_*.yaml # Configuration files for each dataset
├── data/             # Data directory
│   ├── canitedit/           # CaniEdit dataset
│   ├── debugbench/          # DebugBench dataset
│   ├── humaneval_buggy/     # HumanEval Buggy dataset
│   ├── mbpp_buggy/          # MBPP Buggy dataset
│   └── test_set_kod50_ace50_1122/  # Test set
└── debug_gym/        # debug-gym core code
    ├── agents/       # Agent implementations
    ├── gym/          # Environments, tools, terminals
    └── llms/         # LLM backends
```

## Usage

### Basic Usage

```bash
# Run with configuration file
python scripts/run.py scripts/config_<benchmark>.yaml --agent <agent_name>

# Example: run debug_agent on canitedit dataset
python scripts/run.py scripts/config_edit.yaml --agent debug_agent
```

### Available Configuration Files

| Config File | Dataset | Description |
|-------------|---------|-------------|
| `config_edit.yaml` | CaniEdit | Code editing tasks |
| `config_debug_bench.yaml` | DebugBench | Debugging benchmark |
| `config_humaneval_buggy.yaml` | HumanEval Buggy | Buggy HumanEval problems |
| `config_mbpp_buggy.yaml` | MBPP Buggy | Buggy MBPP problems |
| `config_syndebug.yaml` | Test Set | Test set |
| `config_mini_nightmare.yaml` | Mini Nightmare | Small debugging test suite |

### Available Agents

| Agent | Tools | Description |
|-------|-------|-------------|
| `debug_agent` | pdb, grep, rewrite, view, eval | Full debugging agent with PDB debugger |
| `rewrite_agent` | rewrite, view, eval | Rewrite-only agent without debugging |

### Command Line Arguments

```bash
# Specify LLM
python scripts/run.py config.yaml --agent debug_agent -p base.llm_name="gpt-4o"

# Run first N problems
python scripts/run.py config.yaml --agent debug_agent --max-problems 10

# Debug mode
python scripts/run.py config.yaml --agent debug_agent --debug

# Verbose output
python scripts/run.py config.yaml --agent debug_agent -v
```

### Human Mode

Set `llm_name: "human"` in the configuration file to enable human mode for manual debugging control.

## Configuration File Explanation

```yaml
base:
    output_path: "exps/canitedit"     # Output directory
    benchmark: "canitedit"              # Dataset name
    problems: "all"                     # Run all problems
    env_kwargs: {
        "data_path": "data/canitedit",  # Data path (relative)
        "dir_tree_depth": 1,
        "run_timeout": 30,
        "auto_eval_on_rewrite": False,
        "show_current_breakpoints": False,
        "show_directory_tree": True,
        "persistent_breakpoints": True,
        "auto_list": False,
    }
    terminal: {
        type: "local",                  # Terminal type: local, docker, kubernetes
    }

    llm_name: "human"                   # LLM name

    random_seed: 42
    max_steps: 80
    max_rewrite_steps: 30
    memory_size: 80
    save_patch: True

# Agent-specific configuration
debug_agent:
    tools: ["grep", "pdb", "view", "rewrite", "eval"]
```

## Tool Description

| Tool | Description |
|------|-------------|
| `view` | View file contents |
| `grep` | Search for patterns in codebase |
| `pdb` | Python interactive debugger |
| `rewrite` | Rewrite code |
| `eval` | Run tests |

## Output

Experimental results are saved in `exps/<benchmark>/<uuid>/` directory:

```
exps/canitedit/20250128_120000_human/
├── problem_1/
│   ├── debug_gym.log    # Run log
│   ├── trajectory.jsonl # Trajectory
│   └── status.json      # Status
├── summary.txt          # Experiment summary
└── experiment_info.jsonl # Experiment info
```

## Development

This project is developed based on [Microsoft debug-gym](https://github.com/microsoft/debug-gym). Main modifications:

- Support for multiple Chinese datasets (CaniEdit, DebugBench, etc.)
- Added result collection and summary functionality
- Optimized configuration file and data path management
- Support for relative path configuration

## Related Projects

This repository is part of the SWE-PDB project. See also:

- **[SFT Training](../sft/README.md)** - Supervised fine-tuning scripts for training SWE-PDB models
- **[RL Training](../rl/README.md)** - Reinforcement learning training code for SWE-PDB agents

All three components share the same `r2llm` conda environment created above.

## License

This project inherits the MIT License from the original debug-gym project.

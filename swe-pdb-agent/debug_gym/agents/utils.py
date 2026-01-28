import argparse
import logging
import os

import yaml

logger = logging.getLogger(__name__)


def load_config():
    parser = argparse.ArgumentParser()
    parser.add_argument("config_file", help="path to config file")
    parser.add_argument(
        "--agent",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Break before sending action to the environment.",
    )
    parser.add_argument(
        "-n",
        "--num-workers",
        type=int,
        default=None,
        help=(
            "Number of workers to use, default is 1 (no parallelism). "
            "Can be set via DEBUG_GYM_WORKERS environment variable."
        ),
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List available agents and problems.",
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-v",
        "--verbose",
        dest="logging_level",
        action="store_const",
        const=logging.INFO,
        help="Verbose mode",
        default=logging.WARNING,
    )
    group.add_argument(
        "-vv",
        "--very-verbose",
        dest="logging_level",
        action="store_const",
        const=logging.DEBUG,
        help="Verbose mode",
        default=logging.WARNING,
    )
    group.add_argument(
        "--logging-level",
        dest="logging_level",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set logging level",
    )
    parser.add_argument(
        "--force-all",
        action="store_true",
        help="Force running all problems even if they are already done.",
    )
    parser.add_argument(
        "--force-failed",
        action="store_true",
        help="Force running only problems that have failed.",
    )
    parser.add_argument(
        "-t",
        "--timeout",
        type=int,
        default=0,
        help="Timeout in seconds for each problem. Default: 0 seconds (no timeout).",
    )
    parser.add_argument(
        "--keep-completed-tasks",
        action="store_true",
        help="Keep displaying completed tasks in the workers panel.",
    )
    parser.add_argument(
        "--no-live-display",
        action="store_true",
        help="Disable rich live progress display.",
    )
    parser.add_argument(
        "--max-display",
        type=int,
        default=20,
        help="Maximum number of tasks to display in the progress bar.",
    )
    parser.add_argument(
        "--max-problems",
        type=int,
        default=None,
        help="只运行前 N 个问题。",
    )
    parser.add_argument(
        "-p",
        "--params",
        nargs="+",
        action="extend",
        metavar="my.setting=value",
        default=[],
        help="override params of the config file,"
        " e.g. -p 'rewrite_only.random_seed=123'",
    )
    parser.add_argument(
        "--llm-name",
        type=str,
        default=None,
        help="Override llm_name from config file.",
    )
    parser.add_argument(
        "--llm-config-file-path",
        type=str,
        default=None,
        help="Override llm_config_file_path from config file.",
    )
    parser.add_argument(
        "--max-rewrite-steps",
        type=int,
        default=None,
        help="Override max_rewrite_steps from config file.",
    )
    args = parser.parse_args()
    assert os.path.exists(args.config_file), "Invalid config file"
    with open(args.config_file) as reader:
        config = yaml.safe_load(reader)

    # Parse overriden params.
    for param in args.params:
        fqn_key, value = param.split("=")
        entry_to_change = config
        keys = fqn_key.split(".")
        for k in keys[:-1]:
            entry_to_change = entry_to_change[k]
        entry_to_change[keys[-1]] = yaml.safe_load(value)

    available_agents = [item for item in list(config.keys()) if item != "base"]

    if not args.agent:
        # pick first agent
        args.agent = available_agents[0]
    elif args.agent not in available_agents:
        raise ValueError(
            f"Invalid agent: {args.agent}. Available agents: {available_agents}"
        )

    if "base" in config:
        # base config is specified (shared across agents)
        return_config = config["base"]
        agent_specific_config = config[args.agent]
        for key in agent_specific_config:
            # override base config with agent specific config
            return_config[key] = agent_specific_config[key]
    else:
        # base config is not specified
        return_config = config[args.agent]

    # assume agent type is the key if not specified by the user
    if not return_config.get("agent_type"):
        return_config["agent_type"] = args.agent

    # Override llm_name if provided via command line
    if args.llm_name is not None:
        return_config["llm_name"] = args.llm_name

    # Override llm_config_file_path if provided via command line
    if args.llm_config_file_path is not None:
        return_config["llm_config_file_path"] = args.llm_config_file_path

    # Override max_rewrite_steps if provided via command line
    if args.max_rewrite_steps is not None:
        logger.info(f"命令行覆盖 max_rewrite_steps: {args.max_rewrite_steps} (原值: {return_config.get('max_rewrite_steps', '未设置')})")
        print(f"命令行覆盖 max_rewrite_steps: {args.max_rewrite_steps} (原值: {return_config.get('max_rewrite_steps', '未设置')})")
        return_config["max_rewrite_steps"] = args.max_rewrite_steps
    # Ensure max_rewrite_steps exists in config (set default if missing)
    elif "max_rewrite_steps" not in return_config:
        logger.info(f"配置文件中未设置 max_rewrite_steps，使用默认值: 10")
        print(f"配置文件中未设置 max_rewrite_steps，使用默认值: 10")
        return_config["max_rewrite_steps"] = 10  # Default value

    return return_config, args

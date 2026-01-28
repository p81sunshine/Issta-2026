import datetime
import json
import os
import signal
import subprocess
import traceback
import uuid
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

from debug_gym import version as dg_version
from debug_gym.agents.base_agent import AGENT_REGISTRY, create_agent
from debug_gym.agents.utils import load_config
from debug_gym.gym.envs import select_env
from debug_gym.gym.terminals import select_terminal
from debug_gym.gym.tools.toolbox import Toolbox
from debug_gym.llms.base import LLM
from debug_gym.llms.human import Human
from debug_gym.logger import DebugGymLogger, load_previous_run_status, status_json_path


class AgentTimeoutException(BaseException):
    """Custom exception to handle timeouts in agent
    execution. Inherits from BaseException to ensure
    it is not caught by agent exception handling."""

    pass


def set_signal(timeout_seconds):
    """Set a signal handler for timeouts.
    Only works on Unix-like systems."""

    def timeout_handler(signum, frame):
        """Signal handler for timeout."""
        raise AgentTimeoutException

    if timeout_seconds > 0:
        signal.signal(signal.SIGALRM, timeout_handler)
        signal.alarm(timeout_seconds)


def run_agent(args, problem, config):
    set_signal(args.timeout)
    success = True
    env = None
    agent = None
    trajectory_saved = False  # Flag to track if trajectory has been saved

    # Flag to not report errors from the agent, since they report
    # errors themselves and we want to avoid double reporting.
    report_progress_error = True

    exp_path = Path(config["output_path"]) / config["uuid"]
    problem_path = exp_path / problem

    task_logger = DebugGymLogger(
        problem,
        log_dir=problem_path,
        level=args.logging_level,
        mode="w" if args.force_all else "a",
    )
    try:
        previous_run = load_previous_run_status(problem_path, problem)
        if (
            not args.force_all
            and previous_run is not None
            and previous_run.status in ["resolved", "unresolved"]
        ):
            task_logger.debug(f"Previous run found: {problem_path}")
            success = previous_run.status == "resolved"
            task_logger.debug(f"Previous run status: {previous_run.status}")
            if not args.force_failed or success:
                status = "skip-resolved" if success else "skip-unresolved"
                task_logger.report_progress(
                    problem_id=previous_run.problem_id,
                    step=previous_run.step,
                    total_steps=previous_run.total_steps,
                    score=previous_run.score,
                    max_score=previous_run.max_score,
                    status=status,
                )
                task_logger.debug(f"Skipping {problem}, already done.")
                return success

        task_logger.report_progress(
            problem_id=problem,
            step=0,
            total_steps=1,
            score=0,
            max_score=None,
            status="running",
        )

        env = create_env(config, task_logger)
        add_tools(env, config, task_logger)

        llm = LLM.instantiate(
            llm_name=config["llm_name"],
            llm_config_file_path=config.get("llm_config_file_path"),
            logger=task_logger,
        )

        agent = create_agent(
            config["agent_type"],
            config=config,
            env=env,
            llm=llm,
            logger=task_logger,
        )

        try:
            success = agent.run(task_name=problem, debug=args.debug)
        except KeyboardInterrupt:
            task_logger.error("Agent run was interrupted by user.")
            task_logger.report_progress(
                problem_id=problem,
                step=1,
                total_steps=1,
                score=0,
                max_score=None,
                status="error",
            )
            success = False
            raise
        except AgentTimeoutException:
            task_logger.error(
                f"Timeout: Problem `{problem}` exceeded "
                f"the time limit of {args.timeout} seconds."
            )
            task_logger.report_progress(
                problem_id=problem,
                step=1,
                total_steps=1,
                score=0,
                max_score=None,
                status="error",
            )
            success = False
            raise
        except:
            report_progress_error = False
            raise

        # save trajectory
        agent.save_trajectory(task_name=problem)
        trajectory_saved = True

        # optionally apply patch
        if config["save_patch"]:
            agent.save_patch(task_name=problem)

    except Exception as e:
        task_logger.error(
            f"Task Error: {problem} - {e!r}. Run with --very-verbose "
            f"or check {task_logger.log_file} for more information."
        )
        task_logger.debug(
            f"Task {problem} generated an exception: {e!r}. Traceback: {traceback.format_exc()}"
        )
        if report_progress_error:
            task_logger.report_progress(
                problem_id=problem,
                step=1,
                total_steps=1,
                score=0,
                max_score=None,
                status="error",
            )
        if args.debug:
            raise e

        success = False
    finally:
        # Save trajectory even if there was an error, as long as agent was created
        # and trajectory hasn't been saved yet
        if agent is not None and not trajectory_saved:
            try:
                # Check if agent has history before saving
                if hasattr(agent, 'history') and agent.history is not None:
                    agent.save_trajectory(task_name=problem)
                    task_logger.debug(f"Saved trajectory for {problem} even though status is error")
            except Exception as save_error:
                # Don't let trajectory saving errors affect the main flow
                task_logger.debug(f"Failed to save trajectory for {problem}: {save_error!r}")
        
        # Close env and cancel any pending alarm
        signal.alarm(0)
        if env:
            env.close()
    return success


def create_env(config: dict, logger: DebugGymLogger):
    terminal = select_terminal(config.get("terminal"), logger, uuid=config["uuid"])
    env_class = select_env(config.get("benchmark"))
    env = env_class(
        **config["env_kwargs"],
        problems=config.get("problems", ["custom"]),
        terminal=terminal,
        logger=logger,
    )
    return env


def add_tools(env, config: dict, logger: DebugGymLogger):
    """Add tools to the environment"""
    for tool in config["tools"]:
        tool_config = {}
        if isinstance(tool, dict):
            assert len(tool) == 1, "Tool dict must have exactly one key"
            tool, tool_config = list(tool.items())[0]

        tool_instantiated = Toolbox.get_tool(tool, **tool_config)
        env.add_tool(tool_instantiated)
        logger.debug(f"Adding tool to toolbox: {tool_instantiated.__class__.__name__}")


def dump_experiment_info(config: dict, args: dict):
    """Dump experiment information to a JSONL file.
    Each line is one experiment run with its metadata."""

    try:  # Get git commit hash
        git_hash = (
            subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=os.path.dirname(__file__)
            )
            .decode()
            .strip()
        )
    except Exception:
        git_hash = ""

    try:  # Get git diff
        git_diff = subprocess.check_output(
            ["git", "diff"], cwd=os.path.dirname(__file__)
        ).decode()
    except Exception:
        git_diff = ""

    version_info = {
        "debug_gym_version": dg_version.__version__,
        "datetime": datetime.datetime.now().isoformat(),
        "git_hash": git_hash,
        "git_diff": git_diff,
        "config": config,
        "args": vars(args),
        "python_version": os.sys.version,
    }

    file = Path(config["output_path"]) / config["uuid"] / "experiment_info.jsonl"
    with open(file, "a") as f:
        f.write(f"{json.dumps(version_info)}\n")


def collect_experiment_results(exp_output_path: Path, logger: DebugGymLogger):
    """收集实验结果并输出到文件。
    
    收集所有问题的状态，按照resolved、unresolved、error分类，
    并输出到实验目录下的summary.txt文件。
    """
    resolved = []
    unresolved = []
    error = []
    
    # 遍历实验目录下的所有问题目录
    if not exp_output_path.exists():
        logger.warning(f"实验目录不存在: {exp_output_path}")
        return
    
    for problem_dir in sorted(exp_output_path.iterdir()):
        if not problem_dir.is_dir():
            continue
        
        problem_id = problem_dir.name
        status_path = status_json_path(problem_dir, problem_id)
        
        if not status_path.exists():
            # 如果没有状态文件，可能是未完成的问题
            continue
        
        try:
            with open(status_path, "r") as f:
                status_data = json.load(f)
                status = status_data.get("status", "").strip()
        except (json.JSONDecodeError, IOError) as e:
            logger.debug(f"无法读取状态文件 {status_path}: {e}")
            continue
        
        # 根据状态分类
        if status in ["resolved", "skip-resolved"]:
            resolved.append(problem_id)
        elif status in ["unresolved", "skip-unresolved"]:
            unresolved.append(problem_id)
        elif status == "error":
            error.append(problem_id)
        # 其他状态（如running、pending）不包含在总结中
    
    # 计算准确率
    num_resolved = len(resolved)
    num_unresolved = len(unresolved)
    num_error = len(error)
    total = num_resolved + num_unresolved + num_error
    if total > 0:
        accuracy = 100.0 * float(num_resolved) / total
        accuracy_str = f"{accuracy:.2f}%"
    else:
        accuracy_str = "N/A"
    
    # 输出到文件，格式与终端输出一致
    summary_file = exp_output_path / "summary.txt"
    with open(summary_file, "w", encoding="utf-8") as f:
        f.write(f"resolved: {resolved}\n")
        f.write(f"unresolved: {unresolved}\n")
        f.write(f"error: {error}\n")
        f.write(f"num_resolved: {num_resolved}\n")
        f.write(f"num_unresolved: {num_unresolved}\n")
        f.write(f"num_error: {num_error}\n")
        f.write(f"acc: {accuracy_str}\n")
    
    logger.info(f"实验结果总结已保存到: {summary_file}")
    logger.info(f"resolved: {num_resolved}, unresolved: {num_unresolved}, error: {num_error}, acc: {accuracy_str}")


def main():
    config, args = load_config()
    # Use timestamp as UUID if not provided, format: YYYYMMDD_HHMMSS
    if "uuid" not in config or config["uuid"] is None:
        if config["llm_name"] is not None:
            config["uuid"] = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")+ "_" + config["llm_name"]
        else:
            config["uuid"] = datetime.datetime.now().strftime("%Y%m%d_%H%M%S") + "_no_llm"
    exp_output_path = Path(config["output_path"]) / config["uuid"] 
    exp_output_path.mkdir(parents=True, exist_ok=True)
    logger = DebugGymLogger("debug-gym", level=args.logging_level)
    logger.info(f"Experiment log path: {exp_output_path}")
    dump_experiment_info(config, args)

    # Create the environment to get the list of problems to run.
    env = create_env(config, logger=logger)
    # problems = sorted(env.dataset)
    problems = list(env.dataset)

    import random
    random.shuffle(problems)

    # 统一在这里处理 excluded_ids：为其写入 error 的 status 文件，并从待运行列表中移除
    # 现在从 config 顶层读取，而不是 env_kwargs 里
    excluded_ids = config.get("excluded_ids", [])
    if excluded_ids:
        logger.info(f"发现 {len(excluded_ids)} 个被排除的问题，将标记为 error 并跳过运行: {excluded_ids}")
        for excluded_problem in excluded_ids:
            assert excluded_problem in problems, f"excluded_problem {excluded_problem} not in problems {problems}"
            problem_path = exp_output_path / excluded_problem
            problem_path.mkdir(parents=True, exist_ok=True)

            # 手动写一个 debug_gym.log，说明该问题被排除且未实际运行
            log_file = problem_path / "debug_gym.log"
            with open(log_file, "a", encoding="utf-8") as lf:
                lf.write(
                    f"{datetime.datetime.now().isoformat()} INFO "
                    f"Problem `{excluded_problem}` is in excluded_ids; "
                    f"it is marked as error and skipped without running.\n"
                )

            # 手动写入与 TaskProgress 兼容的 status JSON，便于后续 load_previous_run_status 使用
            status_path = status_json_path(problem_path, excluded_problem)
            task_status = {
                "problem_id": excluded_problem,
                "step": 1,
                "total_steps": 1,
                "score": 0,
                "max_score": None,
                "status": "error",
                "logdir": str(problem_path),
            }
            with open(status_path, "w") as f:
                json.dump(task_status, f)
            logger.info(f"已将 {excluded_problem} 标记为 error（已排除），状态写入: {status_path}")

        # 从待运行 problems 列表中移除这些问题
        excluded_set = set(excluded_ids)
        problems = [p for p in problems if p not in excluded_set]

    if args.max_problems is not None:
        logger.info(f"只运行前 {args.max_problems} 个问题")
        problems = problems[: args.max_problems]

    if args.list:
        print(f"\n# Available problems in {config.get('benchmark', 'config')}:")
        for problem in problems:
            print(f" - {problem}")

        # list agent
        print("\n# Available agents:")
        for agent in AGENT_REGISTRY:
            print(f" - {agent}")

        return

    llm = LLM.instantiate(
        llm_name=config["llm_name"],
        llm_config_file_path=config.get("llm_config_file_path"),
        logger=logger,
    )

    # Stop live progress display if --no-live-display is set
    # or in Human mode (avoid conflicts with prompt_toolkit)
    if args.no_live_display or isinstance(llm, Human) or args.debug:
        logger.set_no_live()

    num_workers = args.num_workers or int(os.environ.get("DEBUG_GYM_WORKERS", 1))
    if args.debug:
        logger.warning("Running in debug mode, num_workers set to 1")
        num_workers = 1
    # make sure number of workers is in range [1, len(problems)]
    num_workers = min(max(1, num_workers), len(problems))
    logger.info(f"Running with {num_workers} workers")

    with logger.rich_progress(problems, max_display=args.max_display):
        if num_workers == 1:  # run sequentially for easier debugging
            for problem in problems:
                try:
                    success = run_agent(args, problem, config)
                except AgentTimeoutException:
                    pass  # Handleled in run_agent, just continue
                except (KeyboardInterrupt, Exception) as e:
                    raise e
        else:
            with ProcessPoolExecutor(
                num_workers, initializer=DebugGymLogger.set_as_worker
            ) as executor:
                futures = {
                    executor.submit(run_agent, args, problem, config): problem
                    for problem in problems
                }
                for future in as_completed(futures):
                    if future.cancelled():
                        continue
                    try:
                        problem = futures[future]
                        success = future.result()
                    except AgentTimeoutException:
                        pass  # Handled in run_agent, just continue
                    except (KeyboardInterrupt, Exception) as e:
                        executor.shutdown(wait=True, cancel_futures=True)
                        raise e
    
    # 收集并输出实验结果总结
    collect_experiment_results(exp_output_path, logger)


if __name__ == "__main__":
    main()

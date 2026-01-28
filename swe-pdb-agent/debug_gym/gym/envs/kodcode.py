import tempfile
from pathlib import Path

import debug_gym.gym.utils as utils
from debug_gym.gym.entities import EvalOutput
from debug_gym.gym.envs.env import RepoEnv
from debug_gym.gym.terminals.docker import DockerTerminal
from debug_gym.gym.terminals.terminal import Terminal

DOCKER_KODCODE_IMAGE_NAME = "debug-gym:kodcode"


def build_docker_image(logger):
    """
    Build a Docker image for the KodCode environment.
    """
    # Check if Docker image is built.
    import docker

    docker_client = docker.from_env(timeout=600)
    try:
        docker_client.images.get(DOCKER_KODCODE_IMAGE_NAME)
        return
    except docker.errors.ImageNotFound:
        pass

    logger.info(
        f"Docker image {DOCKER_KODCODE_IMAGE_NAME} not found. Building it..."
    )

    # Starts from the official Python 3.12 slim image
    base_image = "python:3.12-slim"
    # Create a temporary Dockerfile
    with tempfile.TemporaryDirectory() as build_dir:
        dockerfile_path = Path(build_dir) / "Dockerfile"
        with open(dockerfile_path, "w") as dockerfile:
            dockerfile.write(f"FROM {base_image}\n")
            # Configure apt to use ZJU mirror
            dockerfile.write("RUN sed -i 's/deb.debian.org/mirrors.zju.edu.cn/g' /etc/apt/sources.list.d/debian.sources\n")
            # Update apt and install system packages
            dockerfile.write("RUN apt update && apt install -y git tree\n")
            # Configure pip to use ZJU mirror
            dockerfile.write("RUN pip config set global.index-url https://mirrors.zju.edu.cn/pypi/web/simple\n")
            # Install Python packages
            dockerfile.write("RUN pip install pytest\n")

        # Build the Docker image using docker client API for streaming logs
        logger.info("Starting Docker image build...")
        
        # Use the low-level API to get streaming logs
        build_logs_generator = docker_client.api.build(
            path=str(build_dir),
            dockerfile="Dockerfile",
            tag=DOCKER_KODCODE_IMAGE_NAME,
            rm=True,
            decode=True,
        )
        
        # Stream build logs to show progress
        image_id = None
        for log_line in build_logs_generator:
            if log_line:
                if "stream" in log_line:
                    stream_msg = log_line["stream"].strip()
                    if stream_msg:
                        logger.info(stream_msg)
                elif "status" in log_line:
                    status = log_line["status"]
                    if "id" in log_line:
                        status = f"[{log_line['id']}] {status}"
                    logger.info(status)
                elif "aux" in log_line and "ID" in log_line["aux"]:
                    image_id = log_line["aux"]["ID"]
                elif "error" in log_line:
                    error_msg = log_line["error"]
                    logger.error(f"Build error: {error_msg}")
                    raise Exception(f"Docker build failed: {error_msg}")
        
        # Get the built image
        if image_id:
            image = docker_client.images.get(image_id)
        else:
            image = docker_client.images.get(DOCKER_KODCODE_IMAGE_NAME)

    logger.info(f"Docker image {DOCKER_KODCODE_IMAGE_NAME} built successfully.")


class KodCodeEnv(RepoEnv):
    # 默认数据目录路径
    DEFAULT_DATA_PATH = Path(__file__).parent.parent.parent.parent / "data_collection" / "test_space" / "debug_gym"

    def __init__(
        self,
        entrypoint: str = "python -m pytest --tb=no -s test.py",
        terminal: Terminal | None = None,
        data_path: str | Path | None = None,
        **kwargs,
    ):
        terminal = terminal or DockerTerminal(
            base_image=DOCKER_KODCODE_IMAGE_NAME,
            logger=kwargs.get("logger"),
        )
        if hasattr(terminal, "base_image") and terminal.base_image is None:
            terminal.base_image = DOCKER_KODCODE_IMAGE_NAME

        # 设置数据路径：优先使用参数，否则使用默认路径
        if data_path is not None:
            self.data_path = Path(data_path).resolve()
        else:
            self.data_path = self.DEFAULT_DATA_PATH

        super().__init__(entrypoint=entrypoint, terminal=terminal, **kwargs)
        self._cached_max_score: int | None = None

    @property
    def instructions(self) -> str:
        # # 尝试从 question.txt 读取说明，否则返回默认说明
        # if hasattr(self, "current_task") and self.current_task:
        #     codebase_path = self.current_task.get("codebase")
        #     if codebase_path:
        #         question_file = Path(codebase_path) / "question.txt"
        #         if question_file.exists():
        #             try:
        #                 return question_file.read_text(encoding="utf-8").strip()
        #             except Exception:
        #                 pass
        
        return (
            "The program doesn't behave as intended. "
            "Investigate the repository, figure out the root cause, then rewrite the code to fix the issue. "
            "You should not rewrite the whole file, you should debug the code to fix the issue. "
            "Make sure all tests pass."
        )

    def calculate_max_score(self, eval_output: EvalOutput) -> int:
        if self._cached_max_score is not None:
            return self._cached_max_score

        success, output = self.terminal.run("python -m pytest --collect-only test.py", timeout=self.run_timeout)
        self._cached_max_score = utils.extract_max_score_from_pytest_output(
            output
        )
        return self._cached_max_score

    def calculate_score(self, eval_output: EvalOutput) -> int:
        return utils.extract_reward_from_pytest_output(eval_output.output)

    def eval(self, **kwargs) -> EvalOutput:
        success, output = self.terminal.run(self.entrypoint, timeout=self.run_timeout)
        output = utils.cleanup_pytest_output(output)
        output = utils.summarize_pytest_traceback(output)
        self.last_eval = EvalOutput(success, output)
        return self.last_eval

    def setup_task(self, task_name: str, options: dict = None):
        if task_name not in self.dataset:
            raise ValueError(f"Task {task_name} not found in the dataset.")
        self.current_task = self.dataset[task_name]
        self._cached_max_score = None

    def setup_workspace(self):
        self.workspace.reset()

        self.logger.info("Copying files..")
        self.workspace.copy_content(
            src=self.current_task["codebase"], target=self.workspace.working_dir
        )
        self.workspace.setup_file_filters()  # Use codebase's .debugignore and .debugreadonly.

    def setup_terminal(self):
        self.logger.info(f"Configuring {self.terminal}...")

        self.terminal.run("git init")
        self.terminal.run("git config user.name 'debug-gym'")
        self.terminal.run("git config user.email '<>'")

        # KodCode tasks may have Python files and potentially other files
        self.terminal.run("git add *.py *.txt *.md 2>/dev/null || git add *.py")
        self.terminal.run("git commit -am 'Init'")

        # Add debug-gym files if they exist
        self.terminal.run(
            "git add .debugignore .debugreadonly 2>/dev/null || true"
        )
        self.terminal.run("git commit -am 'Add debug-gym ignore and read-only files' || true")

    def load_dataset(self, problems: str | list[str] | None = None):
        if isinstance(self.terminal, DockerTerminal):
            build_docker_image(self.logger)

        if not self.data_path.exists():
            raise ValueError(
                f"KodCode dataset not found at {self.data_path}. "
                f"Please ensure the data directory exists. "
                f"You can specify it using the 'data_path' parameter in env_kwargs."
            )

        # 自动扫描数据目录下的所有问题
        dataset = {}
        task_dirs = [d for d in self.data_path.iterdir() if d.is_dir()]
        
        for task_dir in sorted(task_dirs):
            task_name = task_dir.name
            
            # 检查必要的文件
            test_file = task_dir / "test.py"
            # 查找代码文件（可能是 task_name_code.py 或其他 .py 文件）
            code_files = list(task_dir.glob("*_code.py"))
            if not code_files:
                # 如果没有找到 _code.py，查找所有 .py 文件（排除 test.py）
                code_files = [f for f in task_dir.glob("*.py") if f.name != "test.py"]
            
            if not test_file.exists():
                self.logger.warning(
                    f"Skipping {task_name}: test.py not found in {task_dir}"
                )
                continue
            
            if not code_files:
                self.logger.warning(
                    f"Skipping {task_name}: no code file found in {task_dir}"
                )
                continue
            
            # 使用第一个找到的代码文件
            code_file = code_files[0]
            
            # 检查是否有 .debugignore 和 .debugreadonly（可选）
            debugignore = task_dir / ".debugignore"
            debugreadonly = task_dir / ".debugreadonly"
            
            if not debugignore.exists():
                self.logger.debug(f"No .debugignore found in {task_name}, will use defaults")
            if not debugreadonly.exists():
                self.logger.debug(f"No .debugreadonly found in {task_name}, will use defaults")

            dataset[task_name] = {
                "codebase": task_dir,
                "filename": code_file.name,
            }
            
            self.logger.debug(f"Loaded task: {task_name} (code: {code_file.name})")

        if not dataset:
            raise ValueError(
                f"No valid tasks found in {self.data_path}. "
                "Each task directory should contain at least test.py and a code file."
            )

        problems = utils.filter_problems(dataset, problems)
        dataset = {id: i for id, i in dataset.items() if id in problems}
        
        self.logger.info(f"Loaded {len(dataset)} tasks from {self.data_path}")
        return dataset


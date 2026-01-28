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


class SyntheticEnv(RepoEnv):
    # 默认数据目录路径
    DEFAULT_DATA_PATH = Path(__file__).parent.parent.parent.parent / "data_collection" / "test_space" / "debug_gym"

    def __init__(
        self,
        entrypoint: str = "python -m pytest --tb=no -s test.py",
        terminal: Terminal | None = None,
        data_path: str | Path | None = None,
        solution_path: str | Path | None = None,
        solution_filename: str = "original_code.py",
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
            data_path_obj = Path(data_path)
            # 如果是相对路径，相对于项目根目录（debug-gym 目录）
            if not data_path_obj.is_absolute():
                # 项目根目录是 kodcode.py 的上4级目录
                project_root = Path(__file__).parent.parent.parent.parent
                self.data_path = (project_root / data_path_obj).resolve()
            else:
                self.data_path = data_path_obj.resolve()
        else:
            self.data_path = self.DEFAULT_DATA_PATH

        # 设置正确答案路径
        if solution_path is not None:
            solution_path_obj = Path(solution_path)
            if not solution_path_obj.is_absolute():
                project_root = Path(__file__).parent.parent.parent.parent
                self.solution_path = (project_root / solution_path_obj).resolve()
            else:
                self.solution_path = solution_path_obj.resolve()
        else:
            self.solution_path = None
        
        self.solution_filename = solution_filename
        self.current_solution = None  # 存储当前任务的正确答案

        super().__init__(entrypoint=entrypoint, terminal=terminal, **kwargs)

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
        
        # return (
        #     "The program doesn't behave as intended. "
        #     "Investigate the repository, figure out the root cause, then rewrite the code to fix the issue. "
        #     "You should not rewrite the whole file, you should debug the code to fix the issue. "
        #     "Make sure all tests pass."
        # )
        
        # 基础指令
        base_instructions = (
            "You are provided with the correct code. Please generate a synthetic debugging trace using pdb. "
            "In the working directory, you will find the corresponding buggy code file and the test file. "
            "Strictly follow this structured workflow to create a complete debugging trace:\n\n"
            "1. **Code Inspection**: First, inspect the codebase to understand its structure and identify potential problem areas.\n"
            "2. **Run Tests**: Execute the test suite to identify failing tests and error messages.\n"
            "3. **Start PDB Debugging**:\n"
            "   - If a test file exists, start pdb with pytest using the format: `runner:pytest file:filename.py:test_function_name`\n"
            "   - For non-test files, use: `runner:python file:filename.py`\n"
            "4. **Set Breakpoints**:\n"
            "   - Set breakpoints ONLY on executable lines (not on comments, blank lines, or function definition lines)\n"
            "   - Never set breakpoints on the function definition line.\n"
            "5. **Continue Execution**: Use `c` to run until the next breakpoint is hit.\n"
            "6. **Explore Code**: Use pdb commands (`p`, `n`, `s`, `l`, `bt`) to:\n"
            "   - Print variable values\n"
            "   - Step through code execution\n"
            "   - Examine stack traces\n"
            "7. (Optional) **Move to Next Point**:\n"
            "   - When ready to move to a new location, set a new breakpoint and use `c` to continue\n"
            "8. **Identify and Fix Bug**:\n"
            "   - Once the bug is identified, propose a minimal code change using the rewrite tool\n"
            "9. **Test Fix**: Run tests again to verify the fix\n"
            "10. **Iterate**: If tests fail, repeat from step 3\n\n"
            "Important Notes:\n"
            "- Always set breakpoints on executable statements within function bodies.\n"
            "- When using pdb, only provide the runnerand fileparameters if the command is start. For all other commands, do not include these two parameters"
            # "- Compare with the correct code to learn how to fix the bug.\n"
            # "- **Leverage the Correct Code as a Guide**:\n"
            # "  - Use the correct code to help spot where the buggy code might go wrong.\n"
            # "  - Compare with the correct code to learn how to fix the bug.\n"
            # "  - Consider setting breakpoints at lines that are different between the two versions or where you suspect the bug may be. The breakpoint should be set inside the function body, not on the function definition line.\n"
            # "  - This approach will help you debug more quickly and effectively.\n"
            "- Focus on efficient debugging, not exhaustive code exploration\n"
            "\n Things to Avoid"
            "- Never set breakpoints on the function definition line. This is because the function definition line is not executable. So this breakpoitn will not be hit."

        )
        
        # 添加调试示例
        examples_section = ""
        # 如果有正确答案，添加到指令中
        solution_section = ""
        if self.current_solution:
            solution_section = f"\n\n**Here is the correct solution code which you can ref to learn how to fix the bug:**\n```python\n{self.current_solution}\n```"
        
        file_tree = self.workspace.display_files(self.dir_tree_depth)
        return base_instructions + examples_section + solution_section + file_tree

    def calculate_max_score(self, eval_output: EvalOutput) -> int:
        return utils.extract_max_score_from_pytest_output(eval_output.output)

    def calculate_score(self, eval_output: EvalOutput) -> int:
        return utils.extract_reward_from_pytest_output(eval_output.output)

    def eval(self, **kwargs) -> EvalOutput:
        success, output = self.terminal.run(self.entrypoint, timeout=self.run_timeout)
        output = utils.cleanup_pytest_output(output)
        self.last_eval = EvalOutput(success, output)
        return self.last_eval

    def setup_task(self, task_name: str, options: dict = None):
        if task_name not in self.dataset:
            raise ValueError(f"Task {task_name} not found in the dataset.")
        self.current_task = self.dataset[task_name]
        
        # 加载当前任务的正确答案
        self.current_solution = self._load_solution(task_name)
        if self.current_solution:
            self.logger.debug(
                f"Loaded solution for task: {task_name} "
                f"({len(self.current_solution)} characters)"
            )
        else:
            self.logger.debug(f"No solution found for task: {task_name}")
    
    def _load_solution(self, task_name: str) -> str | None:
        """加载指定任务的正确答案文件。
        
        Args:
            task_name: 任务名称，用于定位正确答案文件
            
        Returns:
            正确答案文件内容，如果文件不存在则返回 None
        """
        if not self.solution_path:
            return None
        
        try:
            # 构建正确答案文件路径: solution_path/task_name/solution_filename
            solution_file = self.solution_path / task_name / self.solution_filename
            
            if not solution_file.exists():
                self.logger.debug(
                    f"Solution file not found: {solution_file}. "
                    f"Task: {task_name}"
                )
                return None
            
            solution_content = solution_file.read_text(encoding="utf-8")
            return solution_content
            
        except Exception as e:
            self.logger.warning(
                f"Failed to load solution for task {task_name}: {e}"
            )
            return None

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


import tempfile
from pathlib import Path

import debug_gym.gym.utils as utils
from debug_gym.constants import DEBUG_GYM_CACHE_DIR, DEBUG_GYM_DATA_DIR
from debug_gym.gym.entities import EvalOutput
from debug_gym.gym.envs.env import RepoEnv
from debug_gym.gym.terminals.docker import DockerTerminal
from debug_gym.gym.terminals.terminal import Terminal

DOCKER_PDB_BETTER_IMAGE_NAME = "debug-gym:pdb-better"


def build_docker_image(logger):
    """
    Build a Docker image for the PDB-Better environment.
    """
    # Check if Docker image is built.
    import docker

    docker_client = docker.from_env(timeout=600)
    try:
        docker_client.images.get(DOCKER_PDB_BETTER_IMAGE_NAME)
        return
    except docker.errors.ImageNotFound:
        pass

    logger.info(
        f"Docker image {DOCKER_PDB_BETTER_IMAGE_NAME} not found. Building it..."
    )

    # Starts from the official Python 3.12 slim image
    base_image = "python:3.12-slim"
    # Then install git and the required Python packages
    setup_commands = [
        "apt update",
        "apt install -y git tree",
        "pip install pytest",
    ]
    # Create a temporary Dockerfile
    with tempfile.TemporaryDirectory() as build_dir:
        dockerfile_path = Path(build_dir) / "Dockerfile"
        with open(dockerfile_path, "w") as dockerfile:
            dockerfile.write(f"FROM {base_image}\n")
            for command in setup_commands:
                dockerfile.write(f"RUN {command}\n")

        # Build the Docker image using docker client
        image, build_logs = docker_client.images.build(
            path=str(build_dir),
            dockerfile="Dockerfile",
            tag=DOCKER_PDB_BETTER_IMAGE_NAME,
            rm=True,
        )

    logger.info(f"Docker image {DOCKER_PDB_BETTER_IMAGE_NAME} built successfully.")


class PdbBetterEnv(RepoEnv):
    DATA_PATH = DEBUG_GYM_DATA_DIR / "pdb-better"
    TASK_NAMES = [
        "iterator_exhaustion",
        "reference_confusion",
        "float_accumulation",
        "closure_binding",
        "loop_variable_leak",
    ]

    def __init__(
        self,
        entrypoint: str = "python -m pytest --tb=no -s test.py",
        terminal: Terminal | None = None,
        **kwargs,
    ):
        terminal = terminal or DockerTerminal(
            base_image=DOCKER_PDB_BETTER_IMAGE_NAME,
            logger=kwargs.get("logger"),
        )
        if hasattr(terminal, "base_image") and terminal.base_image is None:
            terminal.base_image = DOCKER_PDB_BETTER_IMAGE_NAME

        super().__init__(entrypoint=entrypoint, terminal=terminal, **kwargs)

    @property
    def instructions(self) -> str:
        return (
            "The program doesn't behave as intended."
            " Investigate the repository, figure out the root cause, then rewrite the code to fix the issue."
            " These bugs are particularly subtle and may require runtime debugging to understand."
            " Consider using pdb to inspect variable states and execution flow."
        )

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

        self.terminal.run(
            "git add *.py"
        )  # PDB-Better tasks only have Python files.
        self.terminal.run("git commit -am 'Init'")

        self.terminal.run(
            "git add .debugignore .debugreadonly"
        )  # PDB-Better tasks come with those.
        self.terminal.run("git commit -am 'Add debug-gym ignore and read-only files'")

    def load_dataset(self, problems: str | list[str] | None = None):
        if isinstance(self.terminal, DockerTerminal):
            build_docker_image(self.logger)

        if not self.DATA_PATH.exists():
            raise ValueError(
                f"PDB-Better dataset not found at {self.DATA_PATH}. "
                "Please ensure the data/pdb-better directory exists in your debug-gym installation."
            )

        dataset = {}
        for task_name in self.TASK_NAMES:
            task_path = self.DATA_PATH / task_name
            assert (task_path / "test.py").exists(), f"test.py not found in {task_path}"
            assert (task_path / f"{task_name}_code.py").exists(), f"{task_name}_code.py not found in {task_path}"
            assert (task_path / ".debugignore").exists(), f".debugignore not found in {task_path}"
            assert (task_path / ".debugreadonly").exists(), f".debugreadonly not found in {task_path}"

            dataset[task_name] = {
                "codebase": task_path,
                "filename": task_name + "_code.py",
            }

        problems = utils.filter_problems(dataset, problems)
        dataset = {id: i for id, i in dataset.items() if id in problems}
        return dataset


import json
import logging

import datasets
import docker
import requests
from swebench.harness.constants import MAP_REPO_VERSION_TO_SPECS, TestStatus
from swebench.harness.log_parsers import MAP_REPO_TO_PARSER
from swebench.harness.test_spec.python import get_test_directives
from swebench.harness.test_spec.test_spec import make_test_spec
from tenacity import (
    retry,
    retry_if_exception_type,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
    before_sleep_log,
)

logger = logging.getLogger(__name__)

from debug_gym.constants import DEBUG_GYM_CACHE_DIR
from debug_gym.gym.entities import EvalOutput
from debug_gym.gym.envs.env import RepoEnv
from debug_gym.gym.terminals.docker import DockerTerminal
from debug_gym.gym.terminals.kubernetes import KubernetesTerminal
from debug_gym.gym.terminals.terminal import Terminal
from debug_gym.gym.utils import filter_problems


def _is_network_error(exception):
    """Check if an exception is a network-related error that should be retried."""
    # Check for requests exceptions
    if isinstance(
        exception,
        (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.RequestException,
        ),
    ):
        return True
    # Check for urllib3 exceptions (used by requests)
    exception_type_name = type(exception).__name__.lower()
    if any(
        keyword in exception_type_name
        for keyword in ["connection", "timeout", "network", "remote", "protocol"]
    ):
        return True
    # Check exception message for network-related keywords
    exception_str = str(exception).lower()
    if any(
        keyword in exception_str
        for keyword in [
            "connection",
            "timeout",
            "network",
            "remote end closed",
            "connection aborted",
        ]
    ):
        return True
    return False


@retry(
    retry=retry_if_exception_type(
        (
            requests.exceptions.ConnectionError,
            requests.exceptions.Timeout,
            requests.exceptions.RequestException,
        )
    )
    | retry_if_exception(_is_network_error),
    stop=stop_after_attempt(5),
    wait=wait_exponential(multiplier=1, min=2, max=30),
    before_sleep=before_sleep_log(logger, logging.WARNING),
    reraise=True,
)
def _make_test_spec_with_retry(ds_row):
    """Wrapper for make_test_spec with retry logic for network errors.
    
    This function will retry up to 5 times with exponential backoff (2-30 seconds)
    when network-related errors occur during test spec creation.
    """
    return make_test_spec(ds_row)


class SWEBenchEnv(RepoEnv):
    CACHE = DEBUG_GYM_CACHE_DIR / "swe-bench"

    def __init__(
        self,
        dataset_id: str = "SWE-bench/SWE-bench_Verified",
        dataset_revision: str = "99450355ca8c611021187a57ffac304b66666738",
        split: str = "test",
        terminal: Terminal | None = None,
        **kwargs,
    ):
        terminal = terminal or DockerTerminal(logger=kwargs.get("logger"))
        if not isinstance(terminal, (DockerTerminal, KubernetesTerminal)):
            raise ValueError(
                f"{self.__class__.__name__} only supports DockerTerminal and KubernetesTerminal."
            )

        self.dataset_id = dataset_id
        self.dataset_revision = dataset_revision
        self.split = split
        self.test_directives = []

        super().__init__(terminal=terminal, **kwargs)

    @property
    def instructions(self) -> str:
        return self.ds_row["problem_statement"]
        # return (
        #     "The program doesn't behave as intended. "
        #     "Investigate the repository, figure out the root cause, then rewrite the code to fix the issue. "
        #     "You should not rewrite the whole file, you should debug the code to fix the issue. "
        #     "Make sure all tests pass."
        #     "You should first call eval tool to get the error messages, then use the error messages to debug the code. ."
        # )
        # Make sure you pass the correct file path to tools (You can use view to check files under directory)

    def load_dataset(self, problems: str | list[str] | None = None):
        self.ds = datasets.load_dataset(
            self.dataset_id, revision=self.dataset_revision
        )[self.split]
        dataset = {id: i for i, id in enumerate(self.ds["instance_id"])}
        problems = filter_problems(dataset, problems)
        dataset = {id: i for id, i in dataset.items() if id in problems}

        instance_ids = [self.ds[dataset[id]]["instance_id"] for id in dataset]
        image_names = set(
            f"sweb.eval.x86_64.{id.replace('__', '_1776_')}" for id in instance_ids
        )

        if not isinstance(self.terminal, KubernetesTerminal):
            # Download all images needed for SWE-Bench.
            client = docker.from_env()
            tagged_image_names = set(f"swebench/{name}:latest" for name in image_names)

            existing_images = set(
                tag for image in client.images.list() for tag in image.tags
            )
            missing_images = tagged_image_names - existing_images
            if missing_images:
                self.logger.info(f"Found {len(missing_images)} missing Docker images.")
                for i, image_name in enumerate(missing_images):
                    self.logger.info(
                        f"Pulling Docker images {i + 1}/{len(missing_images)}: `{image_name}`."
                    )
                    client.images.pull(image_name)

        return dataset

    def _ensure_pytest_tb_no(self, command: str) -> str:
        """Ensure all pytest commands in the command string use --tb=no.
        
        Args:
            command: The command string that may contain pytest
            
        Returns:
            The command string with --tb=no ensured for all pytest commands
        """
        import re
        
        # Check if command contains pytest
        if "pytest" not in command:
            return command
        
        # First, replace any existing --tb=* with --tb=no
        tb_pattern = r"--tb\s*=\s*\w+"
        command = re.sub(tb_pattern, "--tb=no", command)
        
        # Then, directly replace pytest with pytest --tb=no
        # Handle "python -m pytest" case first
        if "python -m pytest" in command:
            command = command.replace("python -m pytest", "python -m pytest --tb=no", 1)
        else:
            command = command.replace("pytest", "pytest --tb=no", 1)
        
        return command

    def setup_task(self, task_name: str, options: dict = None):
        if task_name not in self.dataset:
            raise ValueError(
                f"Task `{task_name}` was not found in dataset. The available tasks are: {sorted(self.dataset)}.\n"
                "Please provide a valid task or initialize the environment without problems to load all tasks."
            )

        self.task_name = task_name
        self.ds_row = self.ds[self.dataset[self.task_name]]
        self.repo = self.ds_row["repo"]
        self.package_name = self.repo.split("/")[1]
        self.version = self.ds_row["version"]
        self.install_configs = MAP_REPO_VERSION_TO_SPECS[self.repo][self.version]
        self.gold_patch = self.ds_row["patch"]
        # Use retry wrapper for network requests when creating test spec
        self.test_spec = _make_test_spec_with_retry(self.ds_row)
        self.base_image = f"swebench/{self.test_spec.instance_image_key}".replace(
            "__", "_1776_"
        )
        self.base_commit = self.ds_row["base_commit"]
        self.test_patch = self.ds_row["test_patch"]
        self.fail_to_pass = json.loads(self.ds_row["FAIL_TO_PASS"])
        self.pass_to_pass = json.loads(self.ds_row["PASS_TO_PASS"])
        self.test_cmd = self.install_configs["test_cmd"]
        self.test_directives = get_test_directives(self.ds_row)

        self.entrypoint = " ".join([self.test_cmd, *self.test_directives])

        if self.package_name == "sphinx" or self.package_name == "sympy":

            if self.entrypoint.startswith("PYTHONWARNINGS"):
                # Move PYTHONWARNINGS from the entrypoint to the session commands
                export, remaining = self.entrypoint.split(" ", 1)
                self.terminal.session_commands.append(f"export {export}")
                self.entrypoint = remaining

        if self.package_name == "django":
            self.terminal.env_vars["LANG"] = "en_US.UTF-8"
            self.terminal.env_vars["LANGUAGE"] = "en_US:en"
            self.terminal.env_vars["LC_ALL"] = "en_US.UTF-8"
            self.terminal.setup_commands += self.install_configs.get(
                "eval_commands", []
            )
        elif self.package_name == "requests":
            self.terminal.env_vars["CURL_CA_BUNDLE"] = ""

        # -s (capture=no) with pytest allows for debugging with pdb
        # -q (quiet) with pytest avoids long pytest output
        if self.package_name == "django":
            # Django uses ./tests/runtests.py as the test entry point, not pytest
            # The test directives are the specific test modules to run
            # Example: python -m pdb ./tests/runtests.py --verbosity 2 --settings=test_sqlite --parallel 1 model_inheritance_regress.tests
            self.debug_entrypoint = f"python -m pdb {self.test_cmd} {' '.join(self.test_directives)}"
        else:
            self.debug_entrypoint = self.entrypoint.replace("pytest", "pytest -sq")

        if self.package_name == "sphinx" or self.package_name == "sympy":
            expression = " ".join(self.test_directives)
            self.debug_entrypoint = f"python -m pytest {expression}"
        # Ensure all pytest commands use --tb=no
        self.entrypoint = self.entrypoint.replace("--tb=no", "--tb=short")
        # self.entrypoint = self._ensure_pytest_tb_no(self.entrypoint)
        # self.debug_entrypoint = self._ensure_pytest_tb_no(self.debug_entrypoint)

        self.git_apply_cmd = f"git apply -"

    def setup_workspace(self):
        self.terminal.task_name = self.task_name
        self.terminal.base_image = self.base_image
        # Ignore hidden files (dotfiles) and any contents under hidden directories
        self.workspace.reset(
            ignore_patterns=["**/.*"], readonly_patterns=self.test_directives
        )
        self.set_entrypoints(self.entrypoint, self.debug_entrypoint)

    def setup_terminal(self):
        self.logger.debug(f"Configuring {self.terminal}...")

        # Configure pip mirror
        self.terminal.run("pip config set global.index-url https://mirrors.zju.edu.cn/pypi/web/simple")
        
        # # Check system version (for debugging)
        # self.terminal.run("sed -i 's@//.*archive.ubuntu.com@//mirrors.zju.edu.cn@g' /etc/apt/sources.list.d/ubuntu.sources 2>/dev/null || true")
        
        # # Configure apt mirror for older Ubuntu versions
        self.terminal.run("sed -i 's@//.*archive.ubuntu.com@//mirrors.zju.edu.cn@g' /etc/apt/sources.list 2>/dev/null || true")

        # # Install tree for listdir.
        self.terminal.run("apt update && apt install -y tree")

        self.terminal.session_commands.append("source /opt/miniconda3/bin/activate")
        self.terminal.session_commands.append("conda activate testbed")

        if self.package_name == "astropy":
            self.terminal.run("sed -i '/^addopts = -p no:warnings/s/^/# /' setup.cfg")
        elif self.package_name == "requests":
            # To avoid using httpbin.org which is unresponsive at time.
            self.terminal.run(
                "pip install httpbin[mainapp]==0.10.2 pytest-httpbin==2.1.0"
            )
            # Use bash -c with nohup and disown to properly detach background processes
            # This prevents bash from waiting for the background job to complete
            self.terminal.run("bash -c 'nohup gunicorn -b 127.0.0.1:80 -k gevent httpbin:app > /dev/null 2>&1 & disown'")
            self.terminal.run(
                "bash -c 'nohup gunicorn -b 127.0.0.1:443 --certfile=/opt/miniconda3/envs/testbed/lib/python3.9/site-packages/pytest_httpbin/certs/server.pem --keyfile=/opt/miniconda3/envs/testbed/lib/python3.9/site-packages/pytest_httpbin/certs/server.key -k gevent httpbin:app > /dev/null 2>&1 & disown'"
            )
            self.terminal.run('echo "127.0.0.1    httpbin.org" >> /etc/hosts')
            self.terminal.run('export SSL_CERT_FILE=/opt/miniconda3/envs/testbed/lib/python3.9/site-packages/pytest_httpbin/certs/server.pem')
            # Wait for gunicorn services to be ready
            self.terminal.run("for i in {1..30}; do curl -s http://127.0.0.1:80/get > /dev/null 2>&1 && break || sleep 0.5; done")
        elif self.task_name == "pylint-dev__pylint-4661":
            self.terminal.run("pip install appdirs==1.4.4")
        elif self.package_name == "sphinx" or self.package_name == "sympy":
            self.terminal.run("pip install pytest")

        # Check and upgrade pytest if version is less than 4.0.0
        # Add version check and upgrade command to session_commands to ensure it runs after conda activation
        pytest_check_cmd = (
            "python -c '"
            "import sys\n"
            "import re\n"
            "try:\n"
            "    import pytest\n"
            "    version_str = pytest.__version__\n"
            "    match = re.match(r\"(\\d+)\\.(\\d+)\\.(\\d+)\", version_str)\n"
            "    if match:\n"
            "        major, minor, patch = map(int, match.groups())\n"
            "        if (major, minor, patch) < (4, 0, 0):\n"
            "            import subprocess\n"
            "            subprocess.check_call([sys.executable, \"-m\", \"pip\", \"install\", \"pytest==4.0.0\"])\n"
            "            print(\"Upgraded pytest from \" + version_str + \" to 4.0.0\")\n"
            "        else:\n"
            "            print(\"pytest version \" + version_str + \" is already 4.0.0\")\n"
            "    else:\n"
            "        import subprocess\n"
            "        subprocess.check_call([sys.executable, \"-m\", \"pip\", \"install\", \"pytest==4.0.0\"])\n"
            "        print(\"Could not parse pytest version, upgrading to 4.0.0\")\n"
            "except ImportError:\n"
            "    import subprocess\n"
            "    subprocess.check_call([sys.executable, \"-m\", \"pip\", \"install\", \"pytest==4.0.0\"])\n"
            "    print(\"pytest not found, installed pytest 4.0.0\")\n"
            "except Exception as e:\n"
            "    print(\"Error checking pytest version: \" + str(e))\n"
            "    import subprocess\n"
            "    subprocess.check_call([sys.executable, \"-m\", \"pip\", \"install\", \"pytest==4.0.0\"])\n"
            "    print(\"Installed pytest 4.0.0 as fallback\")\n"
            "'"
        )
        # self.terminal.run(pytest_check_cmd)

        # Apply any changes needed to the install commands.
        self.terminal.run("git config user.name 'debug-gym'")
        self.terminal.run("git config user.email '<>'")
        self.terminal.run(f"git commit -am 'Setting up {self.task_name}'")

        # Remove the remote so the agent won't see newer commits.
        # Use || true to ignore error if origin doesn't exist
        self.terminal.run("git remote remove origin || true")

    def apply_gold_patch(self):
        self.logger.debug(f"Applying gold patch to {self.working_dir}.")
        command = self.git_apply_cmd + f" <<'EOF'\n{self.gold_patch}\nEOF"
        self.terminal.run(command, raises=True)
        self.logger.debug("Patch applied successfully.")

    def eval(self, **kwargs) -> EvalOutput:
        # We need to apply the test patch before running any evaluation.
        # Reset any changes made to test_directives files.
        self.terminal.run(f"git checkout -- {' '.join(self.test_directives)}")

        # Apply official test patch (hidden until now)
        self.terminal.run(f"git apply - <<'EOF'\n{self.test_patch}\nEOF")

        success, output = self.terminal.run(self.entrypoint, timeout=self.run_timeout)
        self.last_eval = EvalOutput(success, output)

        # Reset any changes made to test_directives files.
        self.terminal.run(f"git checkout -- {' '.join(self.test_directives)}")

        return self.last_eval

    def calculate_max_score(self, eval_output: EvalOutput) -> int:
        return len(self.fail_to_pass)

    def calculate_score(self, eval_output: EvalOutput) -> int:
        test_status_map = MAP_REPO_TO_PARSER[self.repo](
            eval_output.output, self.test_spec
        )
        self.logger.debug(f"fail_to_pass: {self.fail_to_pass}")
        self.logger.debug(f"Test status map: {test_status_map}")
        score = sum(
            1
            for test in self.fail_to_pass
            # *Do not* assume silent success for now as done in SWE-Bench grading.py
            if test_status_map.get(test, TestStatus.ERROR.value)
            in (TestStatus.PASSED.value, TestStatus.XFAIL.value)
        )
        assert score <= self.max_score
        return score

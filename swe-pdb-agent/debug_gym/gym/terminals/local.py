import os
import shlex
import subprocess
from pathlib import Path

from debug_gym.gym.terminals.shell_session import ShellSession
from debug_gym.gym.terminals.terminal import Terminal
from debug_gym.logger import DebugGymLogger


class LocalTerminal(Terminal):

    def __init__(
        self,
        working_dir: str | None = None,
        session_commands: list[str] | None = None,
        env_vars: dict[str, str] | None = None,
        logger: DebugGymLogger | None = None,
        # Local-specific parameters
        include_os_env_vars: bool = True,
        **kwargs,
    ):
        env_vars = env_vars or {}
        if include_os_env_vars:
            env_vars = env_vars | dict(os.environ)

        super().__init__(
            working_dir=working_dir,
            session_commands=session_commands,
            env_vars=env_vars,
            logger=logger,
            **kwargs,
        )

    @property
    def working_dir(self):
        """Lazy initialization of the working directory."""
        return super().working_dir

    @working_dir.setter
    def working_dir(self, value):
        self._working_dir = value

    def prepare_command(self, entrypoint: str | list[str]) -> list[str]:
        """Prepares a shell command by combining session commands and entrypoint commands.
        Then wraps the command in a shell (self.default_shell_command) call."""
        if isinstance(entrypoint, str):
            entrypoint = [entrypoint]
        if self.session_commands:
            entrypoint = self.session_commands + entrypoint
        entrypoint = " && ".join(entrypoint)
        command = shlex.split(self.default_shell_command) + ["-c", entrypoint]
        return command

    def run(
        self,
        entrypoint: str | list[str],
        timeout: int = None,
        raises: bool = False,
        strip_output: bool = True,
    ) -> tuple[bool, str]:
        """Run a list of commands in the terminal. Return command status and output."""
        command = self.prepare_command(entrypoint)
        self.logger.debug(f"Running command in terminal: {command}")
        # Set a large COLUMNS value to prevent pytest from truncating error messages
        # in "short test summary info". pytest uses COLUMNS to determine terminal width.
        env = dict(self.env_vars)
        if "COLUMNS" not in env:
            env["COLUMNS"] = "200"  # Set a large width to prevent truncation
        process = subprocess.Popen(
            command,
            env=env,
            cwd=self.working_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        stdout, stderr = "", ""
        success = False
        try:
            stdout, stderr = process.communicate(timeout=timeout)
            success = process.returncode == 0
        except subprocess.TimeoutExpired:
            # Kill the process and wait for it to terminate
            process.kill()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                # Process didn't terminate, force kill (shouldn't happen but be safe)
                pass
            timeout_msg = (
                f"Timeout expired after {timeout} seconds. "
                "The command took too long to execute. "
                "Please check your code for infinite loops, long-running operations, or other performance issues."
            ) if timeout else "Timeout expired. The command took too long to execute. Please check your code and try again!"
            stdout, stderr = "", timeout_msg
            success = False
        except Exception as e:
            # Ensure process is cleaned up even if other exceptions occur
            try:
                process.terminate()
                try:
                    process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=5)
            except Exception:
                pass
            raise
        finally:
            # Ensure process is fully cleaned up
            # communicate() should have already waited, but be explicit
            if process.poll() is None:
                # Process is still running (shouldn't happen after communicate, but be safe)
                try:
                    process.terminate()
                    process.wait(timeout=5)
                except (subprocess.TimeoutExpired, ProcessLookupError):
                    try:
                        process.kill()
                        process.wait(timeout=5)
                    except (subprocess.TimeoutExpired, ProcessLookupError):
                        pass

        if raises and not success:
            # Command includes the entrypoint + session commands
            self.logger.debug(f"Failed to run command: {command}")
            raise ValueError(f"Failed to run command: {entrypoint}")

        output = stdout + stderr
        if strip_output:
            output = output.strip("\r\n").strip("\n")

        self.logger.debug(
            f"Output from terminal with status {process.returncode}:\n{output}"
        )
        return success, output

    @property
    def default_shell_command(self) -> str:
        """Starts a new bash session exporting the current python executable as 'python'.
        Flags --noprofile and --norc are used to avoid loading any bash profile or rc file,
        which could interfere with the terminal setup (clean outputs).
        Flag --noediting disables readline editing features including bracketed paste mode.
        """
        return "/bin/bash --noprofile --norc --noediting"

    def new_shell_session(self):
        session = ShellSession(
            shell_command=self.default_shell_command,
            session_commands=self.session_commands,
            working_dir=self.working_dir,
            env_vars=self.env_vars,
            logger=self.logger,
        )
        self.sessions.append(session)
        return session

    def close_shell_session(self, session):
        session.close()
        self.sessions.remove(session)

    def close(self):
        for session in self.sessions:
            self.close_shell_session(session)

    def __str__(self):
        return f"LocalTerminal[{self.working_dir}]"

    def copy_content(self, src: str | Path, target: str | Path | None = None) -> None:
        """Copy files contained in src on the host to target on the host."""
        src = str(src)
        target = str(target or self.working_dir)

        if not os.path.isdir(src):
            raise ValueError(f"Source {src} must be a directory.")

        self.logger.debug(f"[{self}] Copying {src} to {target}.")
        # Use cp to copy files, including hidden files (dotfiles)
        self.run(f"cp -r {src}/. {target}", raises=True)

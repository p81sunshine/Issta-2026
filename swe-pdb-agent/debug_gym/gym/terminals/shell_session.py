import atexit
import errno
import fcntl
import os
import pty
import shlex
import subprocess
import termios
import time
import uuid

from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_random_exponential,
)

from debug_gym.logger import DebugGymLogger

DEFAULT_TIMEOUT = 300
DEFAULT_PS1 = "DEBUG_GYM_PS1"


class ProcessNotRunningError(Exception):
    """Raised when the shell process is not running after initialization."""

    def __init__(self, command: str, output: str):
        self.output = output
        self.command = command
        super().__init__(
            f"Process not running after command: {self.command}\nOutput:\n{self.output}"
        )


class ShellSession:

    def __init__(
        self,
        shell_command: str,
        working_dir: str,
        session_commands: list[str] | None = None,
        env_vars: dict[str, str] | None = None,
        logger: DebugGymLogger | None = None,
    ):
        self._session_id = str(uuid.uuid4()).split("-")[0]
        self.shell_command = shell_command
        self.working_dir = working_dir
        self.session_commands = list(session_commands or [])
        self.env_vars = dict(env_vars or {})
        self.logger = logger or DebugGymLogger("debug-gym")
        self.filedescriptor = None
        self.process = None

        # Make sure session can read the output until the given sentinel or PS1
        if not self.env_vars.get("PS1"):
            self.env_vars["PS1"] = DEFAULT_PS1

        self.default_read_until = self.env_vars["PS1"]

        # Register cleanup on exit, but only if not already registered
        # This prevents duplicate registrations if close() is called explicitly
        self._atexit_registered = False
        atexit.register(self._atexit_close)

    @property
    def is_running(self):
        return self.process is not None and self.process.poll() is None

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_random_exponential(multiplier=0.1, min=0.1, max=2.0),
        retry=retry_if_exception_type(ProcessNotRunningError),
        reraise=True,
    )
    def start(self, command=None, read_until=None):
        self.close()  # Close any existing session

        # Prepare entrypoint, combining session commands and command if provided
        # For example: `bin/bash -c "session_command1 && session_command2 && pdb"`
        if command:
            command = " && ".join(self.session_commands + [command])
            # Build command list: split shell_command, then add ["-c", command]
            # Keep the command string intact so constructs like $(which ...) reach the target shell
            cmd_list = shlex.split(self.shell_command) + ["-c", command]
            entrypoint = f"{self.shell_command} -c {command!r}"
        else:
            cmd_list = shlex.split(self.shell_command)
            entrypoint = self.shell_command

        self.logger.debug(f"Starting {self} with entrypoint: {entrypoint}")

        # Prepare the file descriptor
        _server, _client = pty.openpty()
        self.filedescriptor = _server

        # set_fd_nonblocking
        flags = fcntl.fcntl(_server, fcntl.F_GETFL)
        fcntl.fcntl(_server, fcntl.F_SETFL, flags | os.O_NONBLOCK)

        # Turn off ECHO on the _client side
        attrs = termios.tcgetattr(_client)
        attrs[3] = attrs[3] & ~termios.ECHO  # lflags
        termios.tcsetattr(_client, termios.TCSANOW, attrs)

        self.process = subprocess.Popen(
            cmd_list,
            env=self.env_vars,
            cwd=self.working_dir,
            stdin=_client,
            stdout=_client,
            stderr=_client,
            text=True,
            close_fds=True,
            start_new_session=True,
        )

        # close _client, end in the parent process
        os.close(_client)

        # Read the output until the sentinel or PS1
        output = self.read(read_until=read_until)

        if not self.is_running:
            self.close()
            self.logger.debug(f"{self} failed to start {entrypoint}. stderr:\n{output}")
            raise ProcessNotRunningError(command=command, output=output)

        # Run session commands after starting the session if command was not provided
        if not command and self.session_commands:
            command = " && ".join(self.session_commands)
            output += self.run(command, read_until)

        return output

    def _atexit_close(self):
        """Wrapper for atexit registration to prevent duplicate calls."""
        if not self._atexit_registered:
            self._atexit_registered = True
            self.close()

    def close(self):
        if self.filedescriptor is not None:
            self.logger.debug(f"Closing {self}.")
            try:
                os.close(self.filedescriptor)
            except OSError:
                pass  # File descriptor may already be closed
            self.filedescriptor = None

        if self.process:
            try:
                # Terminate the process gracefully
                self.process.terminate()
                # Wait for process to terminate (with timeout to avoid hanging)
                try:
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    # Process didn't terminate, force kill
                    try:
                        self.process.kill()
                        self.process.wait(timeout=5)
                    except (subprocess.TimeoutExpired, ProcessLookupError):
                        # Process may have already terminated
                        pass
            except ProcessLookupError:
                # Process already terminated
                pass
            except Exception as e:
                # Log but don't fail on cleanup errors
                self.logger.debug(f"Error during process cleanup: {e}")
            finally:
                self.process = None
        
        # Mark as closed to prevent duplicate cleanup
        self._atexit_registered = True

    def read(
        self,
        read_until: str | None = None,
        timeout: int | None = None,
        read_length: int = 1024,
        strip_output: bool = True,
        early_exit_patterns: list[str] | None = None,
    ) -> str:
        """Read from this Shell session until read_until is found, timeout is reached
        
        Args:
            read_until: String to wait for before returning
            timeout: Maximum time to wait in seconds
            read_length: Number of bytes to read per iteration
            strip_output: Whether to strip output
            early_exit_patterns: List of patterns that indicate program has finished.
                                 If any pattern is found in output, return immediately
                                 even if read_until is not found.
        """
        read_until = read_until or self.default_read_until
        timeout = timeout or DEFAULT_TIMEOUT
        early_exit_patterns = early_exit_patterns or []

        output = ""
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                raise TimeoutError(
                    f"{self}: Read timeout after {timeout} secs. Read so far: {output!r}"
                )

            try:
                data = os.read(self.filedescriptor, read_length).decode(
                    "utf-8", errors="ignore"
                )
                if data:
                    output += data
                    if read_until and read_until in output:
                        break
                    # Check for early exit patterns (e.g., program finished)
                    if early_exit_patterns and any(
                        pattern in output for pattern in early_exit_patterns
                    ):
                        # Program has finished, return even without read_until
                        break
                else:
                    time.sleep(0.01)
            except BlockingIOError:
                time.sleep(0.1)
                continue
            except OSError as e:
                if e.errno == errno.EIO:
                    self.is_closed = True
                    self.logger.debug("End of file reached while reading from PTY.")
                    break
                if e.errno != errno.EAGAIN:
                    raise

        output = output.replace(read_until, "").strip()
        if strip_output:
            output = output.strip("\r\n").strip("\n")
        return output

    def run(
        self,
        command: str,
        read_until: str | None = None,
        timeout: int | None = None,
        early_exit_patterns: list[str] | None = None,
    ):
        """Run a command in the Shell session and return the output."""
        output = ""
        if not self.is_running:
            output += self.start()
            self.logger.debug(f"{self}: Initial output: {output!r}")

        self.logger.debug(f"{self}: Running {command!r}")
        os.write(self.filedescriptor, command.encode("utf-8") + b"\n")

        try:
            output += self.read(
                read_until=read_until,
                timeout=timeout,
                early_exit_patterns=early_exit_patterns,
            )
        except TimeoutError as e:
            self.close()
            self.logger.debug(f"{e!r}")
            raise

        self.logger.debug(f"{self}: Output: {output!r}")
        return output

    def __str__(self):
        return f"Shell[{self._session_id}]"

    def __del__(self):
        self.close()

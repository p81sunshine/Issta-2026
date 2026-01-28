import copy
import re

from debug_gym.gym.entities import Observation
from debug_gym.gym.terminals.shell_session import ProcessNotRunningError, ShellSession
from debug_gym.gym.tools.tool import EnvironmentTool
from debug_gym.gym.tools.toolbox import Toolbox


@Toolbox.register()
class PDBTool(EnvironmentTool):
    name: str = "pdb"
    examples = [
        """pdb(command="start", runner="python", file="src/app.py") to start debugging a Python script.""",
        """pdb(command="start", runner="pytest", file="tests/test_foo.py") to debug pytest tests.""",
        """pdb(command="start", runner="pytest", file="tests/test_foo.py::test_specific") to debug a specific test function.""",
        """pdb(command="b mttl/models/modifiers/mlp.py:42") to set a breakpoint at line 42 in the file 'mttl/models/modifiers/mlp.py'.""",
        """pdb(command="c") to continue the execution until the next breakpoint.""",
        """pdb(command="p x") to print the value of the variable x in the current context.""",
        """pdb(command="n") to execute the current line and move to the next line.""",
        """pdb(command="s") to step into a function call.""",
        """pdb(command="l") to list the source code around the current line.""",
        """pdb(command="cl src/code.py:26") to clear the breakpoint at line 26 in the file 'src/code.py'.""",
    ]
    description = (
        "An interface to the Python debugger PDB. Send a command to the PDB terminal."
        + "\n\n**Starting PDB:**"
        + "\n  Use command='start' with BOTH runner and file parameters (both are REQUIRED):"
        + "\n  - For regular Python scripts: runner='python', file='src/app.py'"
        + "\n  - For pytest tests: runner='pytest', file='tests/test_foo.py'"
        + "\n  - For specific pytest test: runner='pytest', file='tests/test_foo.py::test_name'"
        + "\n\n**Other PDB Commands:**"
        + "\n  After starting PDB, use standard PDB commands:"
        + "\n  - b <file:line>: Set breakpoint. (Breakpoints should be set inside the body of a function, not on the function definition line.)"
        + "\n  - c: Continue execution"
        + "\n  - n: Next line"
        + "\n  - s: Step into function"
        + "\n  - p <var>: Print variable"
        + "\n  - l: List source code"
        + "\n  When using breakpoint commands (b, break, cl, clear), specify: file_path:line_number"
        + "\n\n**Note:** PDB sessions restart automatically after code rewrites. Breakpoints are persistent and restored automatically."
        + "\n\n**Examples** (adjust the tool calling format according to your specific syntax):\n"
        + "\n".join(examples)
    )
    arguments = {
        "command": {
            "type": ["string"],
            "description": "The PDB command to execute. Use 'start' to start/restart a PDB session, or any valid PDB command (e.g., 'b', 'c', 'p', 'n', 's', 'l', etc.). See https://docs.python.org/3/library/pdb.html for more information.",
        },
        "runner": {
            "type": ["string", "null"],
            "description": (
                "The test runner to use. REQUIRED with command='start'. Options:\n"
                "  - 'python': Run with 'python -m pdb <file>' (for regular Python scripts)\n"
                "  - 'pytest': Run with 'python -m pdb -m pytest <file>' (for pytest tests)\n"
                # "  - 'pytest': Run with 'python -m pytest --pdb <file>' (for pytest tests)\n"
                "Must be provided when using command='start'."
            ),
        },
        "file": {
            "type": ["string", "null"],
            "description": (
                "The Python file to debug. REQUIRED with command='start'.\n"
                "For pytest, can include specific test: 'tests/test_foo.py::test_function'\n"
                "Example: 'src/app.py' or 'tests/test_foo.py'"
            ),
        },
    }

    def __init__(self):
        super().__init__()
        self.current_frame_file = None
        self._session: ShellSession = None
        self.entrypoint = None
        self.current_runner = None  # Track current runner (python/pytest)
        self.current_file = None  # Track current file being debugged
        self.django_auto_breakpoint = None  # Store the breakpoint info for Django tests

    def __getstate__(self):
        """Handles serialisation of the PDBTool instance (for pickle) without un-picklable attributes"""
        state = self.__dict__.copy()
        for k in ["_session", "current_frame_file"]:
            del state[k]
        return state

    def __setstate__(self, state):
        """Handles de-serialisation of the PDBTool instance (for pickle) without un-picklable attributes"""
        self.__dict__.update(state)
        self.current_frame_file = None
        self._session = None

    def __deepcopy__(self, memo):
        """Create a deep copy of the PDBTool instance with _session set to None."""
        result = type(self).__new__(self.__class__)
        memo[id(self)] = result
        # Copy all attributes except _session
        for k, v in self.__dict__.items():
            # drop the session which is not serializable
            if k == "_session":
                setattr(result, k, None)
            # drop the current_frame_file which is None at the beginning
            # and will be set when the PDB session starts
            elif k == "current_frame_file":
                setattr(result, k, None)
            else:
                setattr(result, k, copy.deepcopy(v, memo))
        return result

    @property
    def pdb_is_running(self):
        return self._session is not None and self._session.is_running

    def interact_with_pdb(self, command: str, timeout: int | None = None) -> str:
        # Only detect early exit for pytest with specific test (file contains "::")
        # When pytest runs a specific test and finishes, it won't return to (Pdb) prompt
        early_exit_patterns = None
        if (
            self.current_runner
            and self.current_runner.lower() == "pytest"
            and self.current_file
            and "::" in self.current_file
        ):
            # For pytest with specific test, detect "short test summary info" to exit early
            early_exit_patterns = ["short test summary info"]
        
        try:
            output = self._session.run(
                command,
                read_until="(Pdb)",
                timeout=timeout,
                early_exit_patterns=early_exit_patterns,
            )
        except TimeoutError as e:
            output = f"The command `{command}` has timed out. {e!r}"

        return output.replace("(Pdb)", "").strip()  # remove the prompt

    def stop_pdb(self):
        self.current_frame_file = None
        self.current_runner = None
        self.current_file = None
        if self._session is not None:
            self._session.close()

    def start_pdb(self, environment) -> str:
        self._session = environment.terminal.new_shell_session()
        # init pdb and wait for the prompt
        self.entrypoint = self.entrypoint or environment.debug_entrypoint
        initial_output = self._session.start(self.entrypoint, read_until="(Pdb)")

        if "The program finished and will be restarted" in initial_output:
            self.stop_pdb()

        if self.pdb_is_running:
            if environment.persistent_breakpoints:
                # restore persistent breakpoints
                for _, _command in environment.current_breakpoints_state.items():
                    self.interact_with_pdb(_command, environment.run_timeout)
                if len(environment.current_breakpoints_state) > 0:
                    initial_output = "\n".join(
                        [initial_output, "Breakpoints have been restored."]
                    )

            self.set_current_frame_file(environment)

        return initial_output

    def on_env_reset(self, environment, **kwargs) -> Observation:
        super().on_env_reset(environment, **kwargs)
        obs = self.start_pdb(environment)
        return Observation(self.name, obs)

    def on_rewrite_success(
        self, environment, file, head, tail, length, **kwargs
    ) -> Observation:
        self.breakpoint_modify(environment, file, head, tail, length)
        # obs = self.restart_pdb(environment)
        # obs = "\nDebugging terminal started:\n" f"{obs}\n"
        obs = "Breakpoint modified successfully after rewrite. Restart the pdb session to apply the changes."
        return Observation(self.name, obs)

    def restart_pdb(self, environment) -> str:
        """Restart the pdb session and restore the breakpoints."""
        self.stop_pdb()
        return self.start_pdb(environment)

    def _extract_pdb_output(self, output: str) -> str:
        """
        Extract only the PDB-relevant part from output, removing Django test setup noise.
        
        For Django tests, the output contains a lot of test setup information like:
        - Database creation messages
        - Migration messages  
        - Test execution messages
        
        We want to extract only the final PDB prompt showing where we stopped.
        
        Args:
            output: The raw output from PDB continue command
            
        Returns:
            Cleaned output with only the PDB-relevant part
        """
        import re
        
        # Split by lines, but first look for the PDB location pattern in the full text
        # Pattern: "> /path/file.py(line)function()" followed by "-> code"
        # This is more reliable than line-by-line parsing
        
        # Remove ANSI escape codes for easier pattern matching
        cleaned_output = re.sub(r'\x1b\[[0-9;]*m', '', output)
        cleaned_output = re.sub(r'\x1b\[\?[0-9]+[hl]', '', cleaned_output)
        
        # Look for the last occurrence of the PDB breakpoint pattern
        # Pattern: ... > /path/file.py(line)function()\r\n-> code_line
        pattern = r'(> [^\r\n]+\([0-9]+\)[^\r\n]+\(\)[^\r\n]*[\r\n]+-> [^\r\n]+)'
        
        matches = list(re.finditer(pattern, cleaned_output))
        
        if matches:
            # Get the last match (the final breakpoint location)
            last_match = matches[-1]
            pdb_part = last_match.group(1)
            
            # Clean up carriage returns and extra whitespace
            pdb_part = pdb_part.replace('\r\n', '\n').replace('\r', '\n')
            
            return pdb_part.strip()
        
        # Fallback: try line-by-line extraction
        lines = output.split('\n')
        
        # Find the last line that starts with "> " (PDB location indicator)
        pdb_start_idx = -1
        for i in range(len(lines) - 1, -1, -1):
            line = lines[i]
            stripped = line.replace('\r', '').strip()
            stripped = re.sub(r'\x1b\[[0-9;]*m', '', stripped)
            stripped = re.sub(r'\x1b\[\?[0-9]+[hl]', '', stripped)
            
            if stripped.startswith('> ') and '(' in stripped and ')' in stripped:
                pdb_start_idx = i
                break
        
        if pdb_start_idx == -1:
            return '\n'.join(lines[-10:]).strip()
        
        # Extract the location line and the code line
        pdb_lines = []
        for i in range(pdb_start_idx, min(pdb_start_idx + 2, len(lines))):
            line = lines[i]
            cleaned = line.replace('\r', '')
            cleaned = re.sub(r'\x1b\[[0-9;]*m', '', cleaned)
            cleaned = re.sub(r'\x1b\[\?[0-9]+[hl]', '', cleaned)
            
            if cleaned.strip():
                pdb_lines.append(cleaned)
        
        return '\n'.join(pdb_lines).strip()
    
    def _find_test_function_line(
        self,
        environment,
        file_path: str,
        class_name: str,
        test_name: str,
    ) -> tuple[str, int] | None:
        try:
            if not environment.workspace.has_file(file_path):
                return None

            file_content = environment.workspace.read_file(file_path)
            lines = file_content.splitlines()

            in_target_class = False
            for i, line in enumerate(lines):
                stripped = line.strip()

                # 进入目标 class
                if not in_target_class and stripped.startswith(f"class {class_name}"):
                    in_target_class = True
                    continue

                if not in_target_class:
                    continue

                # 找到 test 方法
                if stripped.startswith(f"def {test_name}("):
                    bracket_depth = 0
                    in_multiline_assignment = False

                    for j in range(i + 1, len(lines)):
                        current = lines[j].strip()

                        # 跳过空行、注释、docstring
                        if not current or current.startswith("#"):
                            continue
                        if current.startswith('"""') or current.startswith("'''"):
                            continue

                        # 如果正在处理多行赋值，继续追踪括号
                        if in_multiline_assignment:
                            bracket_depth += current.count("(") + current.count("[") + current.count("{")
                            bracket_depth -= current.count(")") + current.count("]") + current.count("}")

                            if bracket_depth == 0:
                                in_multiline_assignment = False
                            continue

                        # 判断是否是多行赋值起始
                        # 检查是否包含赋值且赋值后存在未闭合的括号/列表/字典
                        if "=" in current:
                            # 找到 = 的位置
                            eq_idx = current.find("=")
                            after_eq = current[eq_idx + 1:].strip()
                            # 移除行尾注释
                            if "#" in after_eq:
                                comment_idx = after_eq.find("#")
                                # 检查注释是否在字符串内
                                before_comment = after_eq[:comment_idx]
                                if before_comment.count('"') % 2 == 0 and before_comment.count("'") % 2 == 0:
                                    after_eq = before_comment
                            
                            # 计算括号深度
                            open_brackets = after_eq.count("(") + after_eq.count("[") + after_eq.count("{")
                            close_brackets = after_eq.count(")") + after_eq.count("]") + after_eq.count("}")
                            
                            # 如果有未闭合的括号，说明是多行赋值
                            if open_brackets > close_brackets:
                                in_multiline_assignment = True
                                bracket_depth = open_brackets - close_brackets
                                continue

                        # 第一个真正可执行语句
                        return (file_path, j + 1)

                    # 兜底：函数体为空
                    return (file_path, i + 2)

            return None

        except Exception as e:
            environment.logger.warning(f"Failed to find test function line: {e}")
            return None

    
    def _build_entrypoint(
        self, runner: str, file: str, environment
    ) -> str | None:
        """
        Build the entrypoint command based on runner and file parameters.
        
        Args:
            runner: 'python' or 'pytest' (required)
            file: The file path to debug (required)
            environment: The environment instance
            
        Returns:
            The complete entrypoint command, or None if runner is invalid
        """
        if not file or not runner:
            return None
        
        # Check if this is a Django repository and pytest runner is used
        package_name = getattr(environment, 'package_name', None)
        if package_name == 'django' and runner.lower() == 'pytest':
            # For Django, use the debug_entrypoint which is configured to use runtests.py
            # We'll handle the breakpoint setting separately in the start logic
            debug_entrypoint = getattr(environment, 'debug_entrypoint', None)
            if debug_entrypoint:
                return debug_entrypoint
        
        # Build the command based on runner
        if runner.lower() == 'python':
            return f"python -m pdb {file}"
        elif runner.lower() == 'pytest':
            if "::" in file:
                # Use --trace for specific test, add -s to disable output capture
                return f"python -m pytest -sq {file} --trace  --tb=short"
            else:
                # Use python -m pdb -m pytest, add -s to disable output capture
                # The -s flag is needed so PDB can read from stdin
                return f"python -m pdb -m pytest -sq {file}"
        else:
            return None

    def use(
        self,
        environment,
        command: str,
        runner: str | None = None,
        file: str | None = None,
    ) -> Observation:
        if command == "":
            return Observation(
                self.name, "Failure calling pdb:\nEmpty commands are not allowed."
            )

        # Handle 'start' command explicitly
        if command.lower() in ["start"]:
            # Check required parameters
            if not file:
                return Observation(
                    self.name,
                    "Failure calling pdb:\nThe 'file' parameter is REQUIRED with command='start'.\n"
                    "Examples:\n"
                    "  - pdb(command='start', runner='python', file='src/app.py')\n"
                    "  - pdb(command='start', runner='pytest', file='tests/test.py')",
                )
            
            if not runner:
                return Observation(
                    self.name,
                    "Failure calling pdb:\nThe 'runner' parameter is REQUIRED with command='start'.\n"
                    "Please specify the runner type:\n"
                    "  - runner='python' for regular Python scripts\n"
                    "  - runner='pytest' for pytest tests\n"
                    "Examples:\n"
                    "  - pdb(command='start', runner='python', file='src/app.py')\n"
                    "  - pdb(command='start', runner='pytest', file='tests/test.py')",
                )
            
            # Build entrypoint from runner and file
            new_entrypoint = self._build_entrypoint(runner, file, environment)
            if new_entrypoint is None:
                return Observation(
                    self.name,
                    f"Failure calling pdb:\nInvalid runner '{runner}'. "
                    f"Runner must be 'python' or 'pytest'.",
                )
            
            # Start or restart the PDB session
            try:
                self.entrypoint = new_entrypoint
                self.current_runner = runner
                self.current_file = file
                
                # For Django with pytest runner, parse the file to find breakpoint location
                package_name = getattr(environment, 'package_name', None)
                if package_name == 'django' and runner.lower() == 'pytest' and '::' in file:
                    # Parse pytest format: tests/queries/test_qs_combinators.py::TestQuerySetSetOperationTests::test_union_with_values_list_and_order
                    parts = file.split('::')
                    if len(parts) >= 3:
                        file_path = parts[0]
                        class_name = parts[1]
                        test_name = parts[2]
                        
                        # Find the test function line
                        breakpoint_info = self._find_test_function_line(environment, file_path, class_name, test_name)
                        if breakpoint_info:
                            self.django_auto_breakpoint = breakpoint_info
                        else:
                            environment.logger.warning(f"Djgango!! Could not find test function {test_name} in {file_path}")
                
                output = self.restart_pdb(environment)
                
                # After starting, if we have a Django auto breakpoint, set it and continue
                if self.django_auto_breakpoint and self.pdb_is_running:
                    bp_file, bp_line = self.django_auto_breakpoint
                    # Set the breakpoint
                    bp_cmd = f"b {bp_file}:{bp_line}"
                    bp_output = self.interact_with_pdb(bp_cmd, environment.run_timeout)
                    
                    # Update breakpoints state
                    self.update_breakpoints(environment)
                    
                    # Continue to the breakpoint - this becomes the main output
                    c_output = self.interact_with_pdb("c", environment.run_timeout)
                    # Extract only the PDB part from the output (remove Django test setup noise)
                    output = self._extract_pdb_output(c_output)
                
                # After starting, show all breakpoints and context around the current frame
                extra_sections = []
                if self.pdb_is_running:
                    # Update and show breakpoints
                    self.update_breakpoints(environment)
                    try:
                        breakpoints_text = environment.current_breakpoints()
                        if breakpoints_text:
                            extra_sections.append(f"Breakpoints:\n{breakpoints_text}")
                    except Exception:
                        # Fallback to raw 'b' output if environment helper not available
                        b_out = self.interact_with_pdb("b", environment.run_timeout)
                        if b_out:
                            extra_sections.append(f"Breakpoints:\n{b_out}")
                    # Set current frame and show context
                    self.set_current_frame_file(environment)
                    list_output = self.interact_with_pdb("l .", environment.run_timeout)
                    if list_output:
                        indented_output = self._indent_first_line(list_output)
                        extra_sections.append(
                            f"Context around the current frame:\n{indented_output}"
                        )
                extra = ("\n" + "\n\n".join(extra_sections)) if extra_sections else ""
                return Observation(
                    self.name,
                    f"PDB session started with: {new_entrypoint}\n{output}{extra}",
                )
            except ProcessNotRunningError as e:
                return Observation(
                    self.name,
                    f"Failed to start PDB session with '{new_entrypoint}':\n{e.output}",
                )

        _warning = ""
        # if print, it's OK to have ";" or "\n" in the command
        # otherwise, only the first command will be executed
        if not (command.split()[0] in ["p", "pp"] or command.startswith("print(")):
            splits = re.split("\n|;", command)
            if len(splits) > 1:
                command = splits[0].strip()
                _warning += "Multiple commands are not supported. Only the first command will be executed."

        success, output = True, ""
        if not self.pdb_is_running:
            # PDB 未运行，需要先启动
            # 检查是否有默认 entrypoint 可以使用
            # if hasattr(environment, 'debug_entrypoint') and environment.debug_entrypoint:
            #     # 有默认 entrypoint，自动启动
            #     self.entrypoint = environment.debug_entrypoint
            #     output += self.start_pdb(environment)
            # else:
            # 没有默认 entrypoint，返回友好的错误提示
            return Observation(
                self.name,
                "Failure calling pdb:\nPDB session is not running. Please start it first using command='start'.\n"
                "Examples:\n"
                "  - pdb(command='start', runner='python', file='app.py')\n"
                "  - pdb(command='start', runner='pytest', file='tests/test.py')"
            )

        if not self.pdb_is_running:
            # pdb 启动失败
            return Observation(self.name, f"Failure calling pdb:\n{output}")

        if command in ["b", "break"]:
            # list all breakpoints
            success, output = (
                True,
                f"Breakpoints:\n{environment.current_breakpoints()}\n",
            )
        elif command in ["cl", "clear"]:
            # clear all breakpoints
            environment.current_breakpoints_state = {}
            self.restart_pdb(environment)
            success, output = True, "All breakpoints have been cleared."
        elif command.split()[0] in ["b", "break"] and len(command.split()) > 1:
            # Setting a breakpoint - check if it's on a function definition line
            breakpoint_cmd = command.split()[1]  # e.g., "file.py:42"
            if ":" in breakpoint_cmd:
                file_path, line_str = breakpoint_cmd.rsplit(":", 1)
                try:
                    line_num = int(line_str)
                    # Check if the line is a function/class definition
                    validation_result = self._validate_breakpoint_line(
                        environment, file_path, line_num
                    )
                    if not validation_result["valid"]:
                        # Breakpoint is on a definition line or invalid
                        success = False
                        # Extract suggested line number from message if available
                        suggested_line = None
                        message = validation_result["message"]
                        if "Try line" in message:
                            # Extract line number from "Try line X instead"
                            match = re.search(r"Try line (\d+) instead", message)
                            if match:
                                suggested_line = int(match.group(1))
                        
                        suggestion_text = ""
                        if suggested_line:
                            suggestion_text = (
                                f"\n\n**Suggested fix:**\n"
                                f"  ❌ Wrong: b {file_path}:{line_num}  (function definition line)\n"
                                f"  ✅ Correct: b {file_path}:{suggested_line}  (first executable line inside function)"
                            )
                        else:
                            suggestion_text = (
                                f"\n\n**Please set the breakpoint on an executable line inside the function body, "
                                f"not on the function definition line.**\n"
                                f"  ❌ Wrong: b {file_path}:{line_num}  (function definition line)\n"
                                f"  ✅ Correct: b {file_path}:{line_num + 1}  (try the next line, or first executable line inside function)"
                            )
                        
                        output = (
                            f"❌ BREAKPOINT SETTING FAILED:\n"
                            f"{message}{suggestion_text}"
                        )
                    else:
                        # Valid breakpoint, proceed with setting it
                        try:
                            pdb_out = self.interact_with_pdb(command, environment.run_timeout)
                            if pdb_out in (
                                "End of file",
                                "Blank or comment",
                                "*** Blank or comment",
                            ):
                                success = False
                                output = f"Invalid line number: {pdb_out}."
                            else:
                                success = True
                                output = f"Pdb command output:\n{pdb_out}"
                                if self.pdb_is_running:
                                    self.update_breakpoints(environment)
                                    # output += f"\n\n pdb {command} executed successfully."
                                else:
                                    output += "\n\nPdb quit."
                        except Exception:
                            success = False
                            output = f"Failed to set breakpoint: {command}"
                except ValueError:
                    # Invalid line number format
                    success = False
                    output = f"Invalid breakpoint format: {breakpoint_cmd}. Expected format: file.py:line_number"
            else:
                # No file:line format, let PDB handle it (might be just line number)
                try:
                    pdb_out = self.interact_with_pdb(command, environment.run_timeout)
                    if pdb_out in (
                        "End of file",
                        "Blank or comment",
                        "*** Blank or comment",
                    ):
                        success = False
                        output = f"Invalid line number: {pdb_out}."
                    else:
                        success = True
                        output = f"Pdb command output:\n{pdb_out}"
                        if self.pdb_is_running:
                            self.update_breakpoints(environment)
                            # output += f"\n\n pdb {command} executed successfully."
                        else:
                            output += "\n\nPdb quit."
                except Exception:
                    success = False
                    output = f"Failed to set breakpoint: {command}"
        else:  # other pdb commands, send directly
            try:
                pdb_out = self.interact_with_pdb(command, environment.run_timeout)
                if pdb_out in (
                    "End of file",
                    "Blank or comment",
                    "*** Blank or comment",
                ):
                    # if out of bounds, pdb will return "End of file"
                    # https://github.com/python/cpython/blob/main/Lib/pdb.py#L1464-L1485
                    success = False
                    output = f"Invalid line number: {pdb_out}."
                else:
                    output += f"Pdb command output:\n{pdb_out}"
                if self.pdb_is_running:
                    self.update_breakpoints(environment)
                    # output += f"\n\n pdb {command} executed successfully."
                else:
                    output += "\n\nPdb quit."
            except Exception:
                success = False

        if not success:
            if _warning:  # prevend additional \n
                obs = f"Invalid pdb command: {command}\n{_warning}\n{output.strip()}"
            else:
                obs = f"Invalid pdb command: {command}\n{output.strip()}"
            return Observation(self.name, obs)

        # sometimes it will run into the end of the program
        # we need to put the stdout before:
        # The program exited via sys.exit().
        # into self.last_eval_output, and remove them from the output
        if "The program exited via sys.exit()." in output:
            # end index is the last occurrence of the program exited (from the \n after)
            start_index = output.rfind("The program exited via sys.exit().")
            end_index = output.find("\n", start_index) + 1

            # Raw test output before PDB's \"program exited\" message.
            pre_exit_output = output[:start_index]

            # If we're in a SWEBench-style debug environment, simplify the test
            # output in the same way as SWEBenchDebugEnv.eval() does.
            # To avoid circular imports, we use duck-typing instead of importing
            # SWEBenchDebugEnv directly.
            repo = getattr(environment, "repo", None)
            if repo is not None and hasattr(environment, "_extract_failed_tests_and_summary"):
                simplified_output = pre_exit_output
                try:
                    if repo == "django/django" and hasattr(
                        environment, "_extract_django_test_output"
                    ):
                        simplified_output = environment._extract_django_test_output(
                            pre_exit_output
                        )
                    elif repo == "sympy/sympy" and hasattr(
                        environment, "_extract_sympy_test_output"
                    ):
                        simplified_output = environment._extract_sympy_test_output(
                            pre_exit_output
                        )
                    else:
                        simplified_output = environment._extract_failed_tests_and_summary(
                            pre_exit_output
                        )
                except Exception:
                    # Fall back silently to the raw output if anything goes wrong.
                    simplified_output = pre_exit_output

                pre_exit_output = simplified_output

            output = (
                pre_exit_output
                + "\nReached the end of the program. Restarting the debugging session.\n"
                + output[end_index:]
            )
        if _warning:
            obs = f"{_warning}\n{output.strip()}\n"
        else:
            obs = f"{output.strip()}\n"

        # Add the current frame information to the observation.
        if self.pdb_is_running:
            # read the current frame info to determine the current file
            previous_frame_file = self.current_frame_file
            current_frame = self.set_current_frame_file(environment)

            # free 'list' to provide context around the current frame
            list_output = ""
            # Only show context for 'start' and 'c' and 'b'. 'start' is handled in the start branch above.
            if environment.auto_list and command.split()[0] in ["c"]:
                list_output = self.interact_with_pdb("l .", environment.run_timeout)
            
            if command.split()[0] in ["b"] and len(command.split()) > 1:
                all_breakpoints = self.interact_with_pdb("b", environment.run_timeout)
                if all_breakpoints:
                    obs += f"\nAll breakpoints:\n{all_breakpoints}\n"

            # only show current frame when it changes
            if current_frame and current_frame != previous_frame_file:
                obs += f"\nCurrent frame:\n{current_frame}\n"
            if list_output:
                indented_output = self._indent_first_line(list_output)
                obs += f"\nContext around the current frame:\n{indented_output}\n"

        return Observation(self.name, obs)

    def _validate_breakpoint_line(
        self, environment, file_path: str, line_num: int
    ) -> dict:
        """
        Validate if a breakpoint line is valid (not on function/class definition).
        
        Returns:
            dict with keys:
                - 'valid': bool, True if breakpoint can be set
                - 'message': str, error message if invalid
        """
        try:
            # Get the workspace path
            workspace_path = environment.workspace.working_dir
            full_path = workspace_path / file_path
            
            if not environment.workspace.has_file(file_path):
                return {
                    "valid": True,  # Let PDB handle file not found errors
                    "message": "",
                }
            # Read the file
            file_content = environment.workspace.read_file(file_path)
            lines = file_content.splitlines()
            
            if line_num < 1 or line_num > len(lines):
                return {
                    "valid": False,
                    "message": f"Line {line_num} is out of range (file has {len(lines)} lines).",
                }
            
            # Get the target line (0-indexed)
            target_line = lines[line_num - 1].strip()
            
            # Check if it's a function definition
            # Pattern: def function_name(...):
            # Pattern: async def function_name(...):
            # Pattern: def function_name(...) -> type:
            def_pattern = re.compile(
                r"^\s*(async\s+)?def\s+\w+\s*\([^)]*\)\s*(->\s*[^:]+)?\s*:"
            )
            
            # Check if it's a class definition
            # Pattern: class ClassName(...):
            class_pattern = re.compile(r"^\s*class\s+\w+.*:\s*$")
            
            # Check if it's a blank line or comment
            if not target_line or target_line.startswith("#"):
                return {
                    "valid": False,
                    "message": f"Line {line_num} is a blank line or comment: '{target_line}'",
                }
            
            # Check for function definition
            if def_pattern.match(target_line):
                # Find the next executable line
                next_executable_line = None
                for i in range(line_num, min(line_num + 5, len(lines) + 1)):
                    if i > len(lines):
                        break
                    next_line = lines[i - 1].strip()
                    if next_line and not next_line.startswith("#"):
                        # Check if it's not another definition
                        if not def_pattern.match(next_line) and not class_pattern.match(
                            next_line
                        ):
                            next_executable_line = i
                            break
                
                suggestion = ""
                if next_executable_line:
                    suggestion = f" Try line {next_executable_line} instead (first executable line inside the function)."
                
                return {
                    "valid": False,
                    "message": (
                        f"Line {line_num} is a function definition line: '{target_line}'\n"
                        f"Breakpoints on function definition lines will NEVER be hit because "
                        f"Python doesn't execute the 'def' statement itself, only the function body.{suggestion}"
                    ),
                }
            
            # Check for class definition
            if class_pattern.match(target_line):
                return {
                    "valid": False,
                    "message": (
                        f"Line {line_num} is a class definition line: '{target_line}'\n"
                        f"Breakpoints on class definition lines will NEVER be hit. "
                        f"Set breakpoints inside class methods instead."
                    ),
                }
            
            # Valid line
            return {"valid": True, "message": ""}
            
        except Exception as e:
            # If validation fails for any reason, let PDB handle it
            # (e.g., file read errors, encoding issues)
            return {
                "valid": True,
                "message": f"Could not validate line (error: {e}). Proceeding with breakpoint setting.",
            }

    def _indent_first_line(self, list_output: str) -> str:
        """Add indentation to the first line of the list output to match the
        indentation of the other lines, based on the second line's indentation."""

        lines = list_output.splitlines()
        # Check if we have enough lines to process
        if len(lines) <= 1:
            return list_output

        # Get the first two lines for comparison
        first_line = lines[0]
        second_line = lines[1]

        # Find the spaces at the beginning of both lines
        first_line_match = re.match(r"^(\s*)(\d+)", first_line)
        second_line_match = re.match(r"^(\s*)(\d+)", second_line)

        if first_line_match and second_line_match:
            first_spaces = first_line_match.group(1)
            second_spaces = second_line_match.group(1)

            # If first line has fewer spaces, add the difference
            if len(first_spaces) < len(second_spaces):
                spaces_to_add = second_spaces[len(first_spaces) :]
                return spaces_to_add + list_output

        # If no adjustment needed, return original
        return list_output

    def breakpoint_modify(
        self, environment, rewrite_file, rewrite_head, rewrite_tail, new_code_length
    ):
        # handle breakpoints line number changes caused by rewriting
        # this is a wrapper that manages the self.breakpoints_state, which does not reset at each pseudo terminal start
        # self.breakpoints_state is a dict, the keys are "|||".join([file_path, str(line_number)]) and values are breakpoint_command
        if len(environment.current_breakpoints_state) == 0:
            return
        current_breakpoints_state_copy = copy.deepcopy(
            environment.current_breakpoints_state
        )
        rewrite_file = environment.workspace.resolve_path(rewrite_file)
        for _key in environment.current_breakpoints_state.keys():
            _file_path, _line_number = _key.split("|||")
            _file_path = environment.workspace.resolve_path(_file_path)
            if _file_path != rewrite_file:
                # the breakpoints are not in the current file, no need to modify
                continue
            _line_number = int(_line_number)
            if rewrite_head is None:
                # no line number is provided, rewrite the whole code
                # we remove all breakpoints in the current file
                del current_breakpoints_state_copy[_key]
            else:
                # if a breakpoint was set in between the rewritten code, we need to remove it
                if rewrite_head <= _line_number <= rewrite_tail:
                    del current_breakpoints_state_copy[_key]
                # if a breakpoint was set after the rewritten code, we need to move it
                elif _line_number > rewrite_tail:
                    new_line_number = (
                        _line_number
                        + new_code_length
                        - (rewrite_tail - rewrite_head + 1)
                    )
                    new_key = "|||".join([str(_file_path), str(new_line_number)])
                    _new_value = environment.current_breakpoints_state[_key].split(":")
                    _new_value[1] = " ".join(
                        [str(new_line_number), " ".join(_new_value[1].split()[1:])]
                    )
                    current_breakpoints_state_copy[new_key] = ":".join(
                        _new_value
                    ).strip()
                    del current_breakpoints_state_copy[_key]
                # if a breakpoint was set before the rewritten code, we don't need to do anything
                else:
                    pass
        environment.current_breakpoints_state = current_breakpoints_state_copy

    def update_breakpoints(self, environment):
        """Updates the environment's current_breakpoints_state by
        parsing the output of the PDB 'b' (breakpoints) command.

        The new_breakpoints dictionary keys are in the format "file_path|||line_number",
        and the values are the corresponding PDB breakpoint commands.

        environment.current_breakpoints_state = {
            "path/to/file.py|||line_number": "b path/to/file.py:line_number",
            ...
        }"""

        command = "b"  # list all breakpoints
        output = self.interact_with_pdb(command, environment.run_timeout)
        # parse the output to update the current_breakpoints_state
        # example output:
        # Num Type         Disp Enb   Where
        # 1   breakpoint   keep yes   at /tmp/RepoEnv-_ha8r7_2/constants.py:6
        # 2   breakpoint   keep yes   at /tmp/RepoEnv-_ha8r7_2/constants.py:10
        # 3   breakpoint   keep yes   at /tmp/RepoEnv-_ha8r7_2/constants.py:14
        # -> ACTION_TO_INDEX = {
        new_breakpoints = {}
        breakpoint_pattern = re.compile(
            r"^\s*\d+\s+breakpoint\s+keep\s+yes\s+at\s+(.+):(\d+)$"
        )
        for line in output.splitlines():
            match = breakpoint_pattern.match(line)
            if match:
                # extract the file path and line number from the regex match
                file_path, line_number = match.groups()
                key = "|||".join([file_path, line_number])
                new_breakpoints[key] = f"b {file_path}:{line_number}"
        environment.current_breakpoints_state = new_breakpoints

    def set_current_frame_file(self, environment) -> str | None:
        """A free 'where' to obtain the current frame (line number), hidden from the agent."""
        command = "where"
        output = self.interact_with_pdb(command, environment.run_timeout)
        # parse the output to get the current frame
        # example output:
        #    /home/eryua/venvs/pdb/lib/python3.12/bdb.py(606)run()
        # -> exec(cmd, globals, locals)
        #    <string>(1)<module>()
        # > /tmp/RepoEnv-_ha8r7_2/constants.py(6)<module>()
        # -> ACTION_TO_INDEX = {
        sep = "> "
        file_path = None
        for line in output.splitlines():
            # find the line that starts with "> "
            if line.startswith(sep):
                # extract the file path from the line,
                # remove the leading "> ", the trailing "(line_number)<module>()", and working_dir
                # constants.py(6)<module>()
                # -> ACTION_TO_INDEX = {
                file_path = line[len(sep) :].split("(")[0]
                break
        if self.current_frame_file != file_path:
            self.current_frame_file = file_path
        return file_path

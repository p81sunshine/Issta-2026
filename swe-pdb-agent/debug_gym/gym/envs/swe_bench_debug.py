import re

from debug_gym.gym.entities import EvalOutput
from debug_gym.gym.envs.swe_bench import SWEBenchEnv

from swebench.harness.constants import TestStatus
from swebench.harness.log_parsers import MAP_REPO_TO_PARSER


class SWEBenchDebugEnv(SWEBenchEnv):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store raw output for score calculation
        self._raw_eval_output = None

    def setup_terminal(self):
        super().setup_terminal()

        # Apply official test patch since this is a debugging task.
        self.terminal.run(f"git apply - <<'EOF'\n{self.test_patch}\nEOF")
        self.terminal.run(f"git commit -am 'Applying test patch for {self.task_name}'")


    def _extract_django_test_output(self,output: str) -> str:
        """Parse Django test output and reformat it to pytest-like output."""

        ansi_escape = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

        def _clean(line: str) -> str:
            return ansi_escape.sub("", line)

        lines = output.split("\n")

        failed_tests = []
        failures = 0
        errors = 0
        duration = None

        # Parse FAIL / ERROR cases
        for line in lines:
            stripped = _clean(line).strip()

            # FAIL / ERROR lines
            # Example:
            #   FAIL: test_add (app.tests.test_math.MathTestCase)
            #   ERROR: test_divide (app.tests.test_math.MathTestCase)
            m = re.match(
                r"^(FAIL|ERROR):\s+(\w+)\s+\(([\w\.]+)\)",
                stripped,
            )
            if m:
                status, test_name, full_class = m.groups()
                failures += status == "FAIL"
                errors += status == "ERROR"

                # Convert module path to file path
                parts = full_class.split(".")
                module_path = "/".join(parts[:-1]) + ".py"
                # maybe bug
                module_path = f"tests/{module_path}"
                class_name = parts[-1]

                pytest_line = (
                    f"{module_path}::{class_name}::{test_name} "
                    f"{'FAILED' if status == 'FAIL' else 'ERROR'}"
                )
                failed_tests.append(pytest_line)

            # Duration line
            # Ran 5 tests in 0.012s
            if stripped.startswith("Ran ") and " in " in stripped:
                m = re.search(r"in\s+([\d\.]+)s", stripped)
                if m:
                    duration = m.group(1)

        # Build pytest-style summary
        summary_parts = []
        if failures:
            summary_parts.append(f"{failures} failed")
        if errors:
            summary_parts.append(f"{errors} error")

        summary = ""
        if summary_parts:
            time_part = f"in {duration}s" if duration else ""
            summary = (
                "=" * 17
                + " "
                + ", ".join(summary_parts)
                + (f" {time_part}" if time_part else "")
                + " "
                + "=" * 17
            )

        # Assemble output
        result_lines = []
        result_lines.extend(failed_tests)
        if summary:
            if result_lines:
                result_lines.append("")
            result_lines.append(summary)

        return "\n".join(result_lines) if result_lines else output

    def _extract_sympy_test_output(self, output: str) -> str:
        """Parse Sympy test output and reformat it to pytest-like output.
        
        Sympy test format:
        - Test file path: sympy/geometry/tests/test_point.py[7]
        - Test status lines: test_point E, test_issue_11617 F, test_point3D ok
        - Error/failure details (stack traces)
        - Summary line: tests finished: 5 passed, 1 failed, 1 exceptions, in 0.19 seconds
        """
        ansi_escape = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")
        
        def _clean(line: str) -> str:
            return ansi_escape.sub("", line)
        
        lines = output.split("\n")
        
        # Store current test file path
        current_test_file = None
        failed_tests = []
        test_details = {}  # Store error/failure details for each test
        
        i = 0
        while i < len(lines):
            stripped = _clean(lines[i]).strip()
            
            # Match test file path: sympy/geometry/tests/test_point.py[7]
            file_match = re.match(r"^(sympy/.+\.py)(?:\[\d+\])?$", stripped)
            if file_match:
                current_test_file = file_match.group(1)
                i += 1
                continue
            
            # Match test status lines: test_name E/F/ok
            # Format: test_point E, test_issue_11617 F, test_point3D ok
            test_match = re.match(r"^(test_\w+)\s+(E|F|ok)$", stripped)
            if test_match:
                test_name = test_match.group(1)
                status = test_match.group(2)
                
                if status in ("E", "F"):
                    # Build test identifier: file_path::test_name
                    if current_test_file:
                        test_id = f"{current_test_file}::{test_name}"
                        status_label = "ERROR" if status == "E" else "FAILED"
                        failed_tests.append(f"{test_id} {status_label}")
                        
                        # Collect error/failure details that follow
                        # Look ahead for traceback/error messages
                        details = []
                        j = i + 1
                        detail_started = False
                        found_test_header = False
                        while j < len(lines) and j < i + 200:  # Limit lookahead
                            next_line = _clean(lines[j]).strip()
                            
                            # Stop at next test file or summary
                            if (re.match(r"^sympy/.+\.py", next_line) or
                                next_line.startswith("tests finished:")):
                                break
                            
                            # Stop at next test status line (different test name)
                            next_test_match = re.match(r"^(test_\w+)\s+(E|F|ok)$", next_line)
                            if next_test_match and next_test_match.group(1) != test_name:
                                break
                            
                            # Check if this is a test-specific header with many underscores
                            # Format: ________ sympy/path/to/test.py:test_name ________
                            if re.match(r"^_{20,}.*" + re.escape(test_name) + r".*_{20,}$", next_line):
                                found_test_header = True
                                detail_started = True
                            
                            # Start collecting when we see separator lines or error details
                            if (next_line.startswith("_" * 10) or 
                                "File" in next_line or 
                                "Error" in next_line or
                                "Traceback" in next_line or
                                "assert" in next_line or
                                detail_started):
                                detail_started = True
                                # Skip very long separator lines (just underscores)
                                if not re.match(r"^_{50,}$", next_line):
                                    if next_line or found_test_header:  # Include non-empty lines or after header
                                        details.append(next_line)
                            j += 1
                        
                        if details:
                            # Filter and keep only relevant error details
                            filtered_details = []
                            for detail in details[:50]:  # Limit to 50 lines initially
                                # Include lines with error-related keywords or file paths
                                if any(keyword in detail for keyword in 
                                       ["Error", "Traceback", "File", "assert", "AssertionError", 
                                        "RecursionError", "Exception", "TypeError", "ValueError",
                                        "line", "/testbed/"]):
                                    filtered_details.append(detail)
                            if filtered_details:
                                test_details[test_id] = filtered_details[:15]  # Keep top 15 relevant lines
            
            i += 1
        
        # Extract summary line
        summary_line = None
        for line in reversed(lines):  # Start from end to find last summary
            stripped = _clean(line).strip()
            if "tests finished:" in stripped:
                summary_line = stripped
                break
        
        # Build output
        result_lines = []
        
        # Add failed tests
        for test_id in failed_tests:
            result_lines.append(test_id)
            # Optionally add error details (commented out for brevity, uncomment if needed)
            # if test_id.split()[0] in test_details:
            #     result_lines.append("")
            #     result_lines.extend(test_details[test_id.split()[0]][:5])
            #     result_lines.append("")
        
        # Add summary
        if summary_line:
            if result_lines:
                result_lines.append("")
            # Convert to pytest-style summary format
            # tests finished: 5 passed, 1 failed, 1 exceptions, in 0.19 seconds
            # -> ===== 5 passed, 1 failed, 1 error in 0.19s =====
            summary_match = re.search(
                r"tests finished:\s*(?:(\d+)\s+passed)?(?:,\s*)?(?:(\d+)\s+failed)?(?:,\s*)?(?:(\d+)\s+exceptions?)?(?:,\s+in\s+([\d.]+)\s+seconds?)?",
                summary_line
            )
            if summary_match:
                passed = summary_match.group(1) or "0"
                failed = summary_match.group(2) or "0"
                errors = summary_match.group(3) or "0"
                duration = summary_match.group(4) or ""
                
                summary_parts = []
                if passed != "0":
                    summary_parts.append(f"{passed} passed")
                if failed != "0":
                    summary_parts.append(f"{failed} failed")
                if errors != "0":
                    summary_parts.append(f"{errors} error")
                
                time_str = f" in {duration}s" if duration else ""
                summary = "=" * 20 + " " + ", ".join(summary_parts) + time_str + " " + "=" * 20
                result_lines.append(summary)
            else:
                result_lines.append(summary_line)
        
        return "\n".join(result_lines) if result_lines else output

    def _extract_failed_tests_and_summary(self, output: str) -> str:
        """Extract failed tests and final summary from pytest output.
        
        Args:
            output: The full pytest output string
            
        Returns:
            A simplified output containing only failed tests and the final summary
        """
        # Strip ANSI color codes to make matching more robust
        ansi_escape = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

        def _clean(line: str) -> str:
            return ansi_escape.sub("", line)

        lines = output.split('\n')
        failed_tests = []
        summary_line = None
        
        # Find failed tests and summary line
        for line in lines:
            stripped_line = _clean(line).strip()
            # Check for failed tests.
            # Support both:
            #   - "path/to/test.py::test_name FAILED"
            #   - "FAILED path/to/test.py::test_name - error"
            if (
                ('::' in stripped_line and ' FAILED' in stripped_line)
                or stripped_line.startswith('FAILED ')
            ):
                failed_tests.append(stripped_line)
            if (
                ('::' in stripped_line and ' ERROR' in stripped_line)
                or stripped_line.startswith('ERROR ')
            ):
                failed_tests.append(stripped_line)
            # Check for summary line (format: =============== X failed, Y passed, Z warnings in T seconds ===============)
            # Match lines starting with '=' and containing test statistics
            elif stripped_line.startswith('=') and re.search(
                r'\d+\s+(failed|passed)', stripped_line, re.IGNORECASE
            ):
                # This is the summary line with test statistics
                summary_line = stripped_line
                # Continue to find the last summary line (in case there are multiple)
        
        # Build the simplified output
        result_lines = []
        if failed_tests:
            result_lines.extend(failed_tests)
        if summary_line:
            if result_lines:
                result_lines.append('')  # Add blank line before summary
            result_lines.append(summary_line)

        # If there are too many lines, only show the first 20 and add a note
        if len(result_lines) > 20:
            total = len(result_lines)
            result_lines = result_lines[:20]
            result_lines.append(
                f"... (truncated, showing first 20 lines out of {total})"
            )

        # If we have either failed tests or summary, return the simplified output
        # Otherwise, return original output (shouldn't happen in normal pytest output)
        return '\n'.join(result_lines) if result_lines else output

    def eval(self, **kwargs) -> EvalOutput:
        success, output = self.terminal.run(self.entrypoint, timeout=self.run_timeout)
        
        # Store raw output for score calculation (parser needs full output)
        self._raw_eval_output = EvalOutput(success, output)
        
        # Extract only failed tests and summary for user display
        if self.repo == "django/django":
            simplified_output = self._extract_django_test_output(output)
        elif self.repo == "sympy/sympy":
            # pytest_entrypoint = self.debug_entrypoint.split
            simplified_output = self._extract_sympy_test_output(output)
        else:
            simplified_output = self._extract_failed_tests_and_summary(output)
        
        self.last_eval = EvalOutput(success, simplified_output)
        return self.last_eval

    def calculate_score(self, eval_output: EvalOutput) -> int:
        """Calculate score using raw output instead of simplified output.
        
        The parser needs the full test output to correctly identify all test statuses.
        We use the stored raw output for scoring, but return simplified output to users.
        
        Note: This also checks pass_to_pass tests to ensure no regressions were introduced.
        If any pass_to_pass test fails, the score is set to 0 even if fail_to_pass tests pass.
        """
        
        # Use raw output for parsing if available, otherwise fall back to provided output
        score_output = self._raw_eval_output if self._raw_eval_output is not None else eval_output
        
        # Parse test status using the raw output
        test_status_map = MAP_REPO_TO_PARSER[self.repo](
            score_output.output, self.test_spec
        )
        self.logger.debug(f"fail_to_pass: {self.fail_to_pass}")
        self.logger.debug(f"pass_to_pass: {self.pass_to_pass}")
        self.logger.debug(f"Test status map: {test_status_map}")
        
        # First, check if any pass_to_pass tests are failing (regression check)
        # Special handling for astropy__astropy-7606: filter out tests that don't exist in the test output
        # (e.g., parameterized test base names like test_compose_roundtrip[] that pytest doesn't output)
        failed_pass_to_pass = [
            test for test in self.pass_to_pass
            if test_status_map.get(test, TestStatus.ERROR.value)
            not in (TestStatus.PASSED.value, TestStatus.XFAIL.value)
        ]
        
        if failed_pass_to_pass:
            self.logger.warning(
                f"Regression detected: {len(failed_pass_to_pass)} pass_to_pass tests are now failing: {failed_pass_to_pass[:5]}..."
            )
            # If there are regressions, return 0 score even if fail_to_pass tests pass
            return 0
        
        # Calculate score based on fail_to_pass tests
        score = sum(
            1
            for test in self.fail_to_pass
            # *Do not* assume silent success for now as done in SWE-Bench grading.py
            if test_status_map.get(test, TestStatus.ERROR.value)
            in (TestStatus.PASSED.value, TestStatus.XFAIL.value)
        )
        assert score <= self.max_score
        return score

import re

from debug_gym.gym.entities import EvalOutput
from debug_gym.gym.envs.r2egym import R2EGymEnv

from swebench.harness.constants import TestStatus
from swebench.harness.log_parsers import MAP_REPO_TO_PARSER


class R2EGymDebugEnv(R2EGymEnv):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Store raw output for score calculation
        self._raw_eval_output = None

    # def setup_terminal(self):
    #     super().setup_terminal()

        # Apply official test patch since this is a debugging task.
        # self.terminal.run(f"git apply - <<'EOF'\n{self.test_patch}\nEOF")
        # self.terminal.run(f"git commit -am 'Applying test patch for {self.task_name}'")

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
        simplified_output = self._extract_failed_tests_and_summary(output)
        
        self.last_eval = EvalOutput(success, simplified_output)
        return self.last_eval

    @property
    def instructions(self) -> str:
        # try getting the content inside of [ISSUE] [/ISSUE] using regex tags for ds['problem_statement'] else return ds['problem_statement']
        # ref: https://github.com/R2E-Gym/R2E-Gym/blob/main/src/r2egym/agenthub/runtime/docker.py#L592
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
            "- If you find pdb can not start in some cases, you can give up start pdb and rewirte the file directly."
        )

        base_instructions += (
       "\n\nYou are given a reference golden patch (a correct fix patch). "
       "You MAY use it for internal reasoning, but you MUST NOT copy it verbatim, "
       "and you MUST NOT mention or imply that you used a golden/reference patch "
       "or had access to the ground-truth fix. "
       "You should present the final fix as if you derived it yourself from the problem description and codebase.\n"
       "You should reverse the process of writing the golden patch using pdb."
       "The golden patch is:\n"
       + self.gold_patch
        )
        try:
            content = self.ds_row["problem_statement"]
            issue =  re.search(r"\[ISSUE\](.*)\[/ISSUE\]", content, re.DOTALL).group(1)
        except Exception as e:
            issue = self.ds_row["problem_statement"]
        
        return base_instructions + "\n\n" + "The github issue is:\n" + issue
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
        return super().calculate_score(score_output)

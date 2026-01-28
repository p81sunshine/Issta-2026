from debug_gym.agents.base_agent import BaseAgent, register_agent
from debug_gym.agents.rewrite_agent import RewriteAgent
from debug_gym.agents.history_tracker import HistoryTracker
from debug_gym.gym.entities import Observation


@register_agent
class DebugAgent(BaseAgent):
    name = "debug_agent"
    _base_system_prompt = (
        "You are a debugging agent specialized in fixing Python programs. Your goal is to debug a Python program to make sure it can pass a set of test functions. "
        "You have access to a set of tools including the pdb debugger to help you investigate the code before proposing a patch. While the code may seem familiar to you from your training, you should not assume you know the code. "
        "Instead, you must use the pdb debugger to investigate the code and understand the potential bugs. "
        "A common debugging workflow is to 1) find suspicious files and lines (from error messages or test failures); "
        "2) start pdb with the proper runner (python or pytest) and file, then set breakpoints at suspicious places (IMPORTANT: breakpoints should be set INSIDE the function body, NOT on the function definition line; make sure you set breakpoints to executable statements within the function's scope rather than on its header/definition, otherwise the breakpoint will not be hit); "
        "3) continue execution so the frame is at the breakpoint you set; "
        "4) then print necessary values to identify the bugs. "
        "Once you have gained enough information, propose a rewriting patch to fix the bugs. Avoid rewriting the entire code, focus on the bugs only. "
        "You must make tool calls to interact with the environment, but you can only call one tool at a time. Do not repeat your previous action, especially if it returned tool calling errors or it resulted in information that you already know. "
        "You can spend some time thinking to help you make the decision when you are stuck, but you must be concise and avoid overthinking. "
        "If you already had a plan in the previous steps, you can just follow it without repeating the thinking process. "
        "If you are confident that you have enough information, propose a patch to fix the bugs by calling the rewrite tool. "
        "If you are not sure, continue using the pdb tool to gather more information before proposing a patch. "
        "After every rewrite, it's always a good idea to call the eval tool to execute the new code and check if it passes the tests; if it does not, the tool will return the error messages, which you can use to continue debugging. "
        "Output both your thinking process (if any) and the tool call (must) in the response."
    )
    system_prompt = _base_system_prompt

    def __init__(self, config: dict, env, llm=None, logger=None):
        super().__init__(config, env, llm, logger)
        
        # 检测是否是 R2E-Gym 模型
        if self.llm is not None:
            model_name_lower = self.llm.config.model.lower() if hasattr(self.llm, 'config') and hasattr(self.llm.config, 'model') else ""
            is_r2e_gym = "r2e" in model_name_lower or "r2egym" in model_name_lower or "distill-llama" in model_name_lower
            
            if is_r2e_gym:
                # 为 R2E-Gym 模型添加 JSON 格式工具调用说明
                json_format_note = (
                    " IMPORTANT: When the program ends or when you need to make tool calls, "
                    "you must return a valid JSON object (not a string representation) with 'name' and 'arguments' fields. "
                    "The JSON should be directly in your response, not escaped or quoted. "
                    "Example format (output this directly, not as a string):\n"
                    '{"name": "tool_name", "arguments": {"param": "value"}}\n'
                    "Do NOT output escaped JSON like: {\\\"name\\\": ...} or quoted JSON like: '{\"name\": ...}'"
                )
                self.system_prompt = self._base_system_prompt + json_format_note
            else:
                self.system_prompt = self._base_system_prompt

import json
import logging
import re
from typing import Any

from rllm.agents.agent import Action, BaseAgent, Step, Trajectory
from rllm.agents.system_prompts import DEBUG_GYM_SYSTEM_PROMPT
from rllm.agents.system_prompts import REWRITE_SYSTEM_PROMPT

logger = logging.getLogger(__name__)


class DebugGymAction:
    """
    Debug-Gym action class, similar to r2egym's Action.
    Converts XML format to JSON format for environment execution.
    """
    
    def __init__(self, function_name: str, parameters: dict):
        self.function_name = function_name
        self.parameters = parameters
    
    @classmethod
    def from_string(cls, action_str: str) -> "DebugGymAction":
        """
        Parse action from XML string.
        
        Format: <function=tool_name><parameter=param1>value1</parameter>...</function>
        """
        if not action_str or not action_str.strip():
            return cls("", {})
        
        # Extract function name
        function_match = re.search(r'<function=([^>]+)>', action_str)
        if not function_match:
            return cls("", {})
        
        function_name = function_match.group(1)
        
        # Extract all parameters
        parameters = {}
        param_pattern = re.compile(r'<parameter=([^>]+)>(.*?)</parameter>', re.DOTALL)
        for match in param_pattern.finditer(action_str):
            param_name = match.group(1)
            param_value = match.group(2).strip()
            # 自动类型转换：尝试将参数转换为合适的类型
            parameters[param_name] = cls._convert_param_type(param_value)
        
        return cls(function_name, parameters)
    
    @staticmethod
    def _convert_param_type(value: str):
        """
        Convert parameter value to appropriate type.
        
        Tries to convert strings to int, float, bool, or None as appropriate.
        
        Args:
            value: String value to convert
            
        Returns:
            Converted value (int, float, bool, None, or original string)
        """
        if not value:
            return value
        
        # Try boolean
        if value.lower() in ('true', 'false'):
            return value.lower() == 'true'
        
        # Try None
        if value.lower() in ('none', 'null'):
            return None
        
        # Try integer
        try:
            return int(value)
        except ValueError:
            pass
        
        # Try float
        try:
            return float(value)
        except ValueError:
            pass
        
        # Keep as string
        return value
    
    def to_json_string(self) -> str:
        """
        Convert to JSON format for environment execution.
        
        debug-gym tool parameter names are used directly without mapping.
        """
        return json.dumps({
            "name": self.function_name,
            "arguments": self.parameters
        })


def parse_xml_tool_response(response_text: str) -> tuple[str, DebugGymAction]:
    """
    Extract thought process and tool call (XML format) from response text.
    
    References SWEAgent's parse_xml_response implementation.
    
    Args:
        response_text: Model's response text
        
    Returns:
        (thought, action) tuple
        - thought: Thought process text
        - action: DebugGymAction object
    """
    # Match the first <function=...></function> block
    pattern = re.compile(r"(?s)(<function=.*?</function>)")
    match = pattern.search(response_text)
    
    if match:
        action_str = match.group(1)  # The entire <function> block
        thought = response_text[:match.start()]  # All content before the function block
    else:
        # No function block found, entire response is thought
        thought = response_text
        action_str = ""
    
    # Strip leading and trailing whitespace
    thought = thought.strip()
    action_str = action_str.strip()
    
    # Parse action
    action = DebugGymAction.from_string(action_str)
    
    return thought, action


def parse_tool_call_response(response_text: str) -> tuple[str, DebugGymAction]:
    """
    Extract thought process and tool call from response text.
    
    Uses reverse parsing: finds the last </tool_call> and matches it with the nearest <tool_call>.
    Only parses the last complete tool call.
    
    Handles format like:
    <tool_call>
    {"name": "view", "arguments": {"path": "solution.py"}}
    </tool_call>
    
    Or with thought before:
    Some reasoning here...
    <tool_call>
    {"name": "view", "arguments": {"path": "solution.py"}}
    </tool_call>
    
    Args:
        response_text: Model's response text
        
    Returns:
        (thought, action) tuple
        - thought: Thought process text (content before the last <tool_call>)
        - action: DebugGymAction object
    """
    tool_call_begin = "<tool_call>"
    tool_call_end = "</tool_call>"
    
    # Return empty action if no tool_call_end found
    if tool_call_end not in response_text:
        thought = response_text.strip()
        action = DebugGymAction("", {})
        return thought, action
    
    # Find the last tool_call_end from the end
    end = response_text.rfind(tool_call_end)
    if end == -1:
        thought = response_text.strip()
        action = DebugGymAction("", {})
        return thought, action
    
    # Find the nearest tool_call_begin before this end tag
    # Search backwards from the end position
    start_pos = response_text.rfind(tool_call_begin, 0, end)
    if start_pos == -1:
        # No matching begin tag found before the end tag
        error_msg = "Found </tool_call> but no matching <tool_call> before it"
        logger.warning(error_msg)
        print(f"Error parsing tool call: {error_msg}")
        print(f"response_text: {response_text}")
        thought = response_text.strip()
        action = DebugGymAction("", {})
        return thought, action
    
    # Extract thought (everything before the <tool_call> tag)
    thought = response_text[:start_pos].strip()
    
    # Extract the JSON content between the tags
    start = start_pos + len(tool_call_begin)
    json_content = response_text[start:end].strip()
    
    # Skip empty content
    if not json_content:
        error_msg = "Empty content between <tool_call> tags"
        logger.warning(error_msg)
        print(f"Error parsing tool call: {error_msg}")
        print(f"response_text: {response_text}")
        action = DebugGymAction("", {})
        return thought, action
    
    try:
        # Parse JSON to get tool name and arguments
        tool_data = json.loads(json_content)
        
        # Validate that required fields exist
        if not isinstance(tool_data, dict):
            error_msg = f"Tool call JSON is not a dict: {json_content}"
            logger.warning(error_msg)
            print(f"Error parsing tool call: {error_msg}")
            print(f"response_text: {response_text}")
            action = DebugGymAction("", {})
            return thought, action
        
        function_name = tool_data.get("name", "")
        arguments = tool_data.get("arguments", {})
        
        # Validate that we have a function name
        if not function_name:
            error_msg = f"Tool call JSON missing 'name' field: {json_content}"
            logger.warning(error_msg)
            print(f"Error parsing tool call: {error_msg}")
            print(f"response_text: {response_text}")
            action = DebugGymAction("", {})
        else:
            # Create DebugGymAction from parsed data
            action = DebugGymAction(function_name=function_name, parameters=arguments)
    except json.JSONDecodeError as e:
        error_msg = f"Failed to parse tool_call JSON: {json_content}, error: {e}"
        logger.warning(error_msg)
        print(f"Error parsing tool call: {error_msg}")
        print(f"response_text: {response_text}")
        # If JSON parsing fails, return empty action
        action = DebugGymAction("", {})
    
    return thought, action


class DebugGymAgent(BaseAgent):
    """
    Debug-Gym agent adapter for rLLM framework.
    
    This agent adapts the debug-gym debugging agent to the rllm reinforcement learning framework.
    It handles model responses, updates trajectories, manages conversation history, etc.
    """
    
    def __init__(
        self, 
        use_fn_calling: bool = False, 
        format_model_response: bool = False,
        show_directory_tree: bool = True,
        show_current_breakpoints: bool = False,
        use_tool_call_format: bool = True,
        scaffold: str = "debug",
    ):
        """
        Initialize DebugGymAgent.
        
        Args:
            use_fn_calling: Whether to use function calling format (not fully implemented yet)
            format_model_response: Whether to format model response
            show_directory_tree: Whether to show directory tree in prompt
            show_current_breakpoints: Whether to show current breakpoints in prompt
            use_tool_call_format: Whether to use <tool_call> format instead of <function=> format
            scaffold: Whether to use debug_gym or rewrite_gym
        """
        self.use_fn_calling = use_fn_calling
        self.format_model_response = format_model_response
        self.show_directory_tree = show_directory_tree
        self.show_current_breakpoints = show_current_breakpoints
        self.use_tool_call_format = use_tool_call_format
        self.scaffold = scaffold
        # System prompts
        if scaffold == "debug":
            self.system_prompt = DEBUG_GYM_SYSTEM_PROMPT
        if scaffold == "rewrite":
            self.system_prompt = REWRITE_SYSTEM_PROMPT
        # Initialize trajectory and messages
        self._trajectory = Trajectory()
        self.reset()
    
    def process_model_response(self, response: str) -> tuple[str, dict]:
        """
        Process model response to extract thought and action components.
        
        Uses XML format parsing (consistent with SWEAgent).
        
        Args:
            response: Model's raw text response
            
        Returns:
            Tuple containing:
                - JSON string of tool call (for environment execution)
                - Dictionary containing additional info (such as thought process)
        """
        thought, action = parse_xml_tool_response(response)
        
        # Convert XML action to JSON string for environment
        action_json = action.to_json_string()
        
        return action_json, {
            "thought": thought,
            "action_xml": action,
        }
    
    def build_system_prompt(self, default_system_prompt, info: dict) -> str:
        """
        Build current state information.
        
        返回当前环境状态（得分、目录树、断点等），
        将被添加到第一个user message中。
        
        Args:
            info: Environment info dictionary
            
        Returns:
            Current state information text
        """
        parts = []
        
        # Current score
        score = info.get("score", 0)
        max_score = info.get("max_score", 1)
        # parts.append(f"CURRENT SCORE: {score}/{max_score} tests passing")
        
        system_prompt = default_system_prompt
        # Directory tree (optional)
        if self.show_directory_tree and "dir_tree" in info:
            system_prompt += "\n\n" 
            system_prompt += info["dir_tree"] 
        
        # Current breakpoints (optional)
        # if self.show_current_breakpoints and "current_breakpoints" in info:
        #     breakpoints = info["current_breakpoints"]
        #     parts.append(f"\nCURRENT BREAKPOINTS:\n{breakpoints}")
        
        return system_prompt
    
    def update_from_env(self, observation: Any, reward: float, done: bool, info: dict):
        """
        Update agent's internal state after environment step.
        
        参考debug-gym的逻辑：
        - 第一步（reset后）：构建system prompt + 初始observation
        - 后续步骤：只有observation（工具输出）
        
        Args:
            observation: Tool output from environment (just the tool result)
            reward: Reward for this step
            done: Whether the task is completed
            info: Environment metadata (score, tools, etc.)
        """
        if not self._trajectory.steps:
            # First step after reset
            # System message只包含工具定义和general instructions
            # 不需要修改，已经在reset()中设置
            
            # 构建第一个user message：任务描述 + 当前状态 + eval结果
            task_description = info.get("instructions", "Debug the code to pass all tests")

            assert len(self.messages) == 1 and self.messages[0]['role'] == "system"
            system_prompt = self.messages[0]["content"]
            system_prompt = self.build_system_prompt(system_prompt,info)
            self.messages[0]['content'] = system_prompt
            
            # 使用USER_PROMPT模板
            # observation_str = self.user_prompt_template.format(
            #     problem_statement=task_description
            # )
            
            # 添加当前状态信息
            # observation_str += f"\n\n{state_info}"
            
            # 添加初始测试结果（eval输出）
            # observation_str += f"\n\nINITIAL TEST RESULTS:\n{observation}"
            observation_str = task_description
        else:
            # Subsequent steps: just tool output
            observation_str = str(observation)
            
            # 添加步骤提示
            max_steps = info.get("max_steps")
            # if max_steps:
            #     # 确保 max_steps 是整数类型
            #     try:
            #         max_steps = int(max_steps)
            #         remaining_steps = max_steps - self.step - 1
            #         if remaining_steps > 0:
            #             observation_str += f"n\nRemaining steps: {remaining_steps}"
            #         elif remaining_steps == 0:
            #             observation_str += "\n\nThis is your last step!"
            #     except (ValueError, TypeError):
            #         # 如果无法转换为整数，跳过步骤提示
            #         pass
        
        # Update previous step
        if self._trajectory.steps:
            prior_step = self._trajectory.steps[-1]
            prior_step.next_observation = observation_str
            prior_step.reward = reward
            prior_step.done = done
            prior_step.info = info
        
        # Add to message history
        # Use "tool" role for tool outputs (consistent with ToolAgent and OpenAI format)
        if self._trajectory.steps:
            # Subsequent steps: tool output uses "tool" role
            self.messages.append({"role": "tool", "content": observation_str})
        else:
            # First step: task description uses "user" role
            self.messages.append({"role": "user", "content": observation_str})
        self.cur_step = Step(observation=observation_str)
    
    def update_from_model(self, response: str, **kwargs):
        """
        Update agent state after model generates response.
        
        Args:
            response: Response from model
            **kwargs: Additional parameters
            
        Returns:
            Action object containing the action to execute
        """
        self._trajectory.steps.append(self.cur_step)
        
        # Parse response based on format
        if self.use_tool_call_format:
            # Use <tool_call> format parser
            thought, action = parse_tool_call_response(response)
        else:
            # Use <function=> format parser (default)
            thought, action = parse_xml_tool_response(response)
        
        action_json = action.to_json_string()
        
        assert self._trajectory.steps, "Trajectory should not be empty when updating model."
        
        # Update trajectory
        cur_step = self._trajectory.steps[-1]
        cur_step.thought = thought
        cur_step.action = action_json  # Store JSON format
        cur_step.model_response = response
        
        # Update chat completion
        if self.format_model_response:
            formatted_response = f"{thought}\n\n{action_json}"
            self.messages.append({"role": "assistant", "content": formatted_response})
        else:
            self.messages.append({"role": "assistant", "content": response})
        
        self.step += 1
        return Action(action=cur_step.action)
    
    def get_current_state(self) -> Step:
        """Get the state of the current step."""
        assert self._trajectory.steps, "Trajectory should not be empty when getting current state."
        return self._trajectory.steps[-1]
    
    def reset(self):
        """Reset agent state."""
        self._trajectory = Trajectory()
        self.messages = [
            {
                "role": "system",
                "content": self.system_prompt,
            }
        ]
        self.step = 0
    
    @property
    def trajectory(self) -> Trajectory:
        """Return the current trajectory."""
        return self._trajectory
    
    @property
    def chat_completions(self):
        """Return chat completion messages."""
        return self.messages




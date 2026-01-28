"""
DeepSeek R1 Distill 32B LLM 实现

该类处理 DeepSeek R1 Distill 32B 模型的特殊工具调用格式。
DeepSeek R1 模型可能在响应内容中返回 JSON 格式的工具调用，而不是使用标准的 tool_calls API。
"""

import json
import re
from typing import Optional

from debug_gym.gym.tools.tool import ToolCall
from debug_gym.llms.deepseek_parser import parse_deepseek_r1_tool_call
from debug_gym.llms.huggingface import HuggingFaceLLM


class DeepSeekR1LLM(HuggingFaceLLM):
    """
    DeepSeek R1 Distill 32B 模型的 LLM 实现。
    
    该模型可能在响应内容中返回 JSON 格式的工具调用，格式为:
    {"name": "tool_name", "parameters": {...}}
    
    或者在标准的 tool_calls 中返回，但格式可能不同。
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def parse_tool_call_response(self, response) -> ToolCall:
        """解析 DeepSeek R1 模型的工具调用响应。
        
        如果 response 是标准的 OpenAI tool_call 对象，但参数格式不同，
        或者 response 是 None，我们需要从响应内容中提取。
        
        Args:
            response: 工具调用响应对象或 None
        
        Returns:
            ToolCall: 解析后的工具调用对象
        """
        if response is None:
            return ToolCall(
                id="empty_tool_response",
                name="empty_tool_response",
                arguments={},
            )
        
        # 尝试标准的 OpenAI 格式解析
        try:
            # 检查是否是标准的 OpenAI tool_call 格式
            if hasattr(response, 'function') and hasattr(response.function, 'name'):
                # 检查 arguments 是否是 JSON 字符串
                if isinstance(response.function.arguments, str):
                    try:
                        # 尝试解析为 JSON
                        arguments = json.loads(response.function.arguments)
                        # 检查是否是 DeepSeek R1 格式（有 parameters 字段）
                        if isinstance(arguments, dict) and "parameters" in arguments:
                            # 这是 DeepSeek R1 格式，提取 parameters
                            return ToolCall(
                                id=response.id,
                                name=response.function.name,
                                arguments=arguments["parameters"],
                            )
                        else:
                            # 标准格式
                            return ToolCall(
                                id=response.id,
                                name=response.function.name,
                                arguments=arguments,
                            )
                    except json.JSONDecodeError:
                        # 如果不是 JSON，尝试解析为 DeepSeek R1 格式
                        try:
                            tool_call_data = json.loads(response.function.arguments)
                            return parse_deepseek_r1_tool_call(tool_call_data)
                        except (json.JSONDecodeError, ValueError):
                            pass
                
                # 标准 OpenAI 格式
                return ToolCall(
                    id=response.id,
                    name=response.function.name,
                    arguments=json.loads(response.function.arguments) if isinstance(response.function.arguments, str) else response.function.arguments,
                )
        except (AttributeError, KeyError, json.JSONDecodeError):
            pass
        
        # 如果无法解析，返回空工具调用
        return ToolCall(
            id="empty_tool_response",
            name="empty_tool_response",
            arguments={},
        )

    def _extract_tool_call_from_content(self, content: str) -> Optional[ToolCall]:
        """从响应内容中提取工具调用 JSON。
        
        DeepSeek R1 模型可能在响应文本中直接返回 JSON 格式的工具调用。
        尝试从文本中提取 JSON 对象。
        
        Args:
            content: 响应内容文本
        
        Returns:
            ToolCall 或 None
        """
        if not content:
            return None
        
        # 尝试直接解析整个内容
        try:
            tool_call_data = json.loads(content.strip())
            if isinstance(tool_call_data, dict) and "name" in tool_call_data:
                return parse_deepseek_r1_tool_call(tool_call_data)
        except (json.JSONDecodeError, ValueError):
            pass
        
        # 尝试查找 JSON 代码块（markdown 格式）
        json_code_block_pattern = r'```(?:json)?\s*(\{.*?\})\s*```'
        matches = re.findall(json_code_block_pattern, content, re.DOTALL)
        for match in matches:
            try:
                tool_call_data = json.loads(match)
                if isinstance(tool_call_data, dict) and "name" in tool_call_data:
                    return parse_deepseek_r1_tool_call(tool_call_data)
            except (json.JSONDecodeError, ValueError):
                continue
        
        # 使用更智能的方法：查找以 { 开头、包含 "name" 和 "parameters" 的 JSON 对象
        # 使用栈来匹配大括号，提取所有可能的 JSON 对象，然后选择最合适的
        candidates = []
        start_idx = content.find('{')
        
        while start_idx != -1:
            # 从当前位置开始，尝试找到匹配的 JSON 对象
            brace_count = 0
            end_idx = start_idx
            
            for i in range(start_idx, len(content)):
                if content[i] == '{':
                    brace_count += 1
                elif content[i] == '}':
                    brace_count -= 1
                    if brace_count == 0:
                        end_idx = i
                        break
            
            if brace_count == 0:
                # 找到了一个完整的 JSON 对象
                json_str = content[start_idx:end_idx + 1]
                try:
                    tool_call_data = json.loads(json_str)
                    if isinstance(tool_call_data, dict) and "name" in tool_call_data:
                        # 检查是否包含 parameters 或 arguments 字段（DeepSeek R1 格式）
                        if "parameters" in tool_call_data or "arguments" in tool_call_data:
                            # 这是一个有效的工具调用候选
                            # 计算优先级：优先选择包含 "parameters" 且 name 和 parameters 都存在的
                            priority = 0
                            if "parameters" in tool_call_data:
                                priority += 2
                            if "arguments" in tool_call_data:
                                priority += 1
                            if isinstance(tool_call_data.get("parameters") or tool_call_data.get("arguments"), dict):
                                priority += 1
                            
                            candidates.append((priority, tool_call_data, start_idx))
                except (json.JSONDecodeError, ValueError):
                    pass
            
            # 继续查找下一个 {
            start_idx = content.find('{', start_idx + 1)
        
        # 如果有候选，选择优先级最高的（如果优先级相同，选择第一个出现的）
        if candidates:
            # 按优先级降序排序，优先级相同时按位置排序
            candidates.sort(key=lambda x: (-x[0], x[2]))
            _, tool_call_data, _ = candidates[0]
            return parse_deepseek_r1_tool_call(tool_call_data)
        
        return None

    def generate(self, messages, tools, **kwargs):
        """生成响应并处理工具调用。
        
        如果模型不支持标准的 tool_calls API，我们需要从响应内容中提取工具调用。
        """
        from debug_gym.llms.base import LLMResponse, retry_on_exception
        from openai import NOT_GIVEN
        
        # 设置 max_tokens 如果未提供
        kwargs["max_tokens"] = kwargs.get("max_tokens", NOT_GIVEN)
        
        # 准备请求参数
        completion_kwargs = {
            "model": self.config.model,
            "messages": messages,
            **kwargs,
        }
        
        # 检查模型是否支持工具调用
        # DeepSeek R1 可能不支持标准的 tool_calls，但我们仍然尝试传递工具定义
        # 如果 API 不支持，我们会从响应内容中提取工具调用
        if tools:
            try:
                completion_kwargs["tools"] = self.define_tools(tools)
                completion_kwargs["tool_choice"] = "auto"
            except Exception as e:
                self.logger.warning(
                    f"无法定义工具，将从响应内容中提取工具调用: {e}"
                )
        
        try:
            response = retry_on_exception(
                self._perform_chat_completion, self.need_to_be_retried
            )(**completion_kwargs)
        except Exception as e:
            # 如果工具调用失败，可能是模型不支持，尝试不使用工具调用
            if tools and ("tool" in str(e).lower() or "function" in str(e).lower()):
                self.logger.warning(
                    f"模型 {self.model_name} 可能不支持工具调用 API，尝试从响应内容中提取工具调用: {e}"
                )
                completion_kwargs.pop("tools", None)
                completion_kwargs.pop("tool_choice", None)
                response = retry_on_exception(
                    self._perform_chat_completion, self.need_to_be_retried
                )(**completion_kwargs)
            else:
                raise
        
        # 获取响应内容
        message = response.choices[0].message
        content = message.content
        reasoning_content = None
        if hasattr(message, "reasoning_content"):
            reasoning_content = message.reasoning_content
        
        # 尝试从标准的 tool_calls 中获取工具调用
        tool_call_response = None
        if hasattr(message, "tool_calls") and message.tool_calls:
            tool_call_response = message.tool_calls[0]
            if hasattr(tool_call_response, 'type'):
                assert tool_call_response.type == "function"
        
        # 如果没有标准的 tool_calls，尝试从响应内容中提取
        parsed_tool_call = None
        if tool_call_response is None and content and tools:
            extracted_tool_call = self._extract_tool_call_from_content(content)
            if extracted_tool_call:
                parsed_tool_call = extracted_tool_call
                self.logger.info(
                    f"从响应内容中提取到工具调用: {extracted_tool_call.name}"
                )
        
        # 如果还没有解析工具调用，使用标准的解析方法
        if parsed_tool_call is None:
            parsed_tool_call = self.parse_tool_call_response(tool_call_response)
        
        # 创建响应对象
        llm_response = LLMResponse(
            prompt=messages,
            response=content,
            reasoning_response=reasoning_content,
            tool=parsed_tool_call,
            prompt_token_count=response.usage.prompt_tokens if hasattr(response, 'usage') else None,
            response_token_count=response.usage.completion_tokens if hasattr(response, 'usage') else None,
        )
        
        return llm_response

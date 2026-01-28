"""
DeepSeek R1 Distill 32B 模型工具调用解析器

该模块提供了解析 DeepSeek R1 Distill 32B 模型返回的工具调用 JSON 格式的功能。
DeepSeek R1 Distill 32B 模型返回的工具调用格式为:
{
    "name": "tool_name",
    "parameters": {
        "param1": "value1",
        "param2": "value2"
    }
}
"""

import json
import uuid
from typing import Dict, Any, Union

from debug_gym.gym.tools.tool import ToolCall


def parse_deepseek_r1_tool_call(tool_call_data: Union[str, Dict[str, Any]]) -> ToolCall:
    """
    解析 DeepSeek R1 Distill 32B 模型返回的工具调用 JSON。
    
    Args:
        tool_call_data: 工具调用的 JSON 字符串或字典对象
            格式: {"name": "tool_name", "parameters": {...}}
    
    Returns:
        ToolCall: 解析后的工具调用对象
    
    Raises:
        ValueError: 如果 JSON 格式无效或缺少必需的字段
        json.JSONDecodeError: 如果 JSON 字符串无法解析
    
    Example:
        >>> tool_call_json = '{"name": "get_current_weather", "parameters": {"location": "波士顿", "unit": "celsius"}}'
        >>> tool_call = parse_deepseek_r1_tool_call(tool_call_json)
        >>> print(tool_call.name)
        get_current_weather
        >>> print(tool_call.arguments)
        {'location': '波士顿', 'unit': 'celsius'}
    """
    # 如果输入是字符串，则解析为字典
    if isinstance(tool_call_data, str):
        try:
            tool_call_data = json.loads(tool_call_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"无法解析 JSON 字符串: {e}") from e
    
    # 验证必需的字段
    if not isinstance(tool_call_data, dict):
        raise ValueError(f"工具调用数据必须是字典类型，实际类型: {type(tool_call_data)}")
    
    if "name" not in tool_call_data:
        raise ValueError("工具调用数据中缺少必需的字段 'name'")
    
    # 获取工具名称
    tool_name = tool_call_data["name"]
    if not isinstance(tool_name, str):
        raise ValueError(f"工具名称必须是字符串类型，实际类型: {type(tool_name)}")
    
    # 获取参数（如果存在）
    # DeepSeek R1 格式使用 "parameters"，但也支持 "arguments" 作为别名
    if "parameters" in tool_call_data:
        parameters = tool_call_data["parameters"]
        if not isinstance(parameters, dict):
            raise ValueError(f"参数必须是字典类型，实际类型: {type(parameters)}")
        arguments = parameters
    elif "arguments" in tool_call_data:
        # 支持 "arguments" 作为 "parameters" 的别名
        arguments_data = tool_call_data["arguments"]
        if not isinstance(arguments_data, dict):
            raise ValueError(f"参数必须是字典类型，实际类型: {type(arguments_data)}")
        arguments = arguments_data
    else:
        # 如果没有 parameters 或 arguments 字段，使用空字典
        arguments = {}
    
    # 生成唯一的 ID（使用工具名称和时间戳/随机 UUID）
    # 如果原始数据中有 id 字段，则使用它；否则生成一个新的
    if "id" in tool_call_data:
        tool_id = str(tool_call_data["id"])
    else:
        # 使用工具名称和 UUID 生成唯一 ID
        tool_id = f"{tool_name}-{uuid.uuid4().hex[:8]}"
    
    return ToolCall(
        id=tool_id,
        name=tool_name,
        arguments=arguments,
    )


def parse_deepseek_r1_tool_calls_batch(
    tool_calls_data: Union[str, list, Dict[str, Any]]
) -> list[ToolCall]:
    """
    批量解析多个工具调用。
    
    Args:
        tool_calls_data: 可以是以下格式之一:
            - JSON 字符串（单个工具调用或数组）
            - 字典（单个工具调用）
            - 列表（多个工具调用）
    
    Returns:
        list[ToolCall]: 解析后的工具调用对象列表
    
    Example:
        >>> tool_calls_json = '[{"name": "get_weather", "parameters": {"location": "北京"}}, {"name": "get_time", "parameters": {}}]'
        >>> tool_calls = parse_deepseek_r1_tool_calls_batch(tool_calls_json)
        >>> len(tool_calls)
        2
    """
    # 如果输入是字符串，先解析为 Python 对象
    if isinstance(tool_calls_data, str):
        try:
            tool_calls_data = json.loads(tool_calls_data)
        except json.JSONDecodeError as e:
            raise ValueError(f"无法解析 JSON 字符串: {e}") from e
    
    # 如果是单个字典，转换为列表
    if isinstance(tool_calls_data, dict):
        tool_calls_data = [tool_calls_data]
    
    # 如果是列表，逐个解析
    if isinstance(tool_calls_data, list):
        return [parse_deepseek_r1_tool_call(tool_call) for tool_call in tool_calls_data]
    else:
        raise ValueError(
            f"工具调用数据必须是字典、列表或 JSON 字符串，实际类型: {type(tool_calls_data)}"
        )


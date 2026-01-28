"""
内容文本中的工具调用 JSON 解析器

该模块提供了解析从内容文本中提取的工具调用 JSON 格式的功能。
工具调用格式为:
{
    "name": "tool_name",
    "arguments": {
        "param1": "value1",
        "param2": "value2"
    }
}
"""

import json
import re
import uuid
from typing import Dict, Any, Union, Optional

from debug_gym.gym.tools.tool import ToolCall


def parse_tool_call_from_json(tool_call_data: Union[str, Dict[str, Any]]) -> ToolCall:
    """
    解析工具调用 JSON，支持 "arguments" 字段。
    
    Args:
        tool_call_data: 工具调用的 JSON 字符串或字典对象
            格式: {"name": "tool_name", "arguments": {...}}
    
    Returns:
        ToolCall: 解析后的工具调用对象
    
    Raises:
        ValueError: 如果 JSON 格式无效或缺少必需的字段
        json.JSONDecodeError: 如果 JSON 字符串无法解析
    
    Example:
        >>> tool_call_json = '{"name": "pdb", "arguments": {"command": "start", "runner": "pytest"}}'
        >>> tool_call = parse_tool_call_from_json(tool_call_json)
        >>> print(tool_call.name)
        pdb
        >>> print(tool_call.arguments)
        {'command': 'start', 'runner': 'pytest'}
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
    
    # 获取参数（优先使用 "arguments"，也支持 "parameters" 作为兼容）
    if "arguments" in tool_call_data:
        arguments_data = tool_call_data["arguments"]
        if not isinstance(arguments_data, dict):
            raise ValueError(f"参数必须是字典类型，实际类型: {type(arguments_data)}")
        arguments = arguments_data
    elif "parameters" in tool_call_data:
        # 支持 "parameters" 作为 "arguments" 的别名（兼容 DeepSeek 格式）
        parameters = tool_call_data["parameters"]
        if not isinstance(parameters, dict):
            raise ValueError(f"参数必须是字典类型，实际类型: {type(parameters)}")
        arguments = parameters
    else:
        # 如果没有 arguments 或 parameters 字段，使用空字典
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


def extract_tool_call_from_content(content: str) -> Optional[ToolCall]:
    """
    从响应内容中提取工具调用 JSON。
    
    尝试从文本中提取 JSON 对象，格式为 {"name": "tool_name", "arguments": {...}}
    
    Args:
        content: 响应内容文本，可能包含文本和 JSON 对象
    
    Returns:
        ToolCall 或 None（如果未找到有效的工具调用）
    
    Example:
        >>> content = 'Let me try to start debugging:\\n{"name": "pdb", "arguments": {"command": "start"}}'
        >>> tool_call = extract_tool_call_from_content(content)
        >>> print(tool_call.name)
        pdb
    """
    if not content:
        return None
    
    # 尝试直接解析整个内容
    try:
        tool_call_data = json.loads(content.strip())
        if isinstance(tool_call_data, dict) and "name" in tool_call_data:
            return parse_tool_call_from_json(tool_call_data)
    except (json.JSONDecodeError, ValueError):
        pass
    
    # 尝试查找 JSON 代码块（markdown 格式）
    # 注意：使用括号匹配而不是简单的 .*? 来正确处理嵌套的 JSON
    json_code_block_pattern = r'```(?:json)?\s*(\{.*?\})\s*```'
    matches = re.findall(json_code_block_pattern, content, re.DOTALL)
    for match in matches:
        try:
            tool_call_data = json.loads(match)
            if isinstance(tool_call_data, dict) and "name" in tool_call_data:
                return parse_tool_call_from_json(tool_call_data)
        except (json.JSONDecodeError, ValueError):
            # 如果 JSON 解析失败，尝试替换 Python 字面量
            try:
                match_fixed = re.sub(r'\bNone\b', 'null', match)
                match_fixed = re.sub(r'\bTrue\b', 'true', match_fixed)
                match_fixed = re.sub(r'\bFalse\b', 'false', match_fixed)
                tool_call_data = json.loads(match_fixed)
                if isinstance(tool_call_data, dict) and "name" in tool_call_data:
                    return parse_tool_call_from_json(tool_call_data)
            except (json.JSONDecodeError, ValueError):
                continue
    
    # 方法1: 优先查找 \n\n{ 开头的 JSON 对象（更常见的情况）
    # 这样可以避免复杂的引号转义问题
    start_patterns = ['\n\n{', '\n{', '{']
    for pattern in start_patterns:
        start_idx = content.find(pattern)
        if start_idx == -1:
            continue
        
        # 调整 start_idx 到实际 { 的位置
        if pattern != '{':
            start_idx = start_idx + len(pattern) - 1
        
        # 使用括号匹配算法找到完整的 JSON 对象
        brace_count = 0
        end_idx = start_idx
        in_string = False
        escape_next = False
        
        for i in range(start_idx, len(content)):
            if escape_next:
                escape_next = False
                continue
            
            if content[i] == '\\':
                escape_next = True
                continue
            
            if content[i] == '"' and not escape_next:
                in_string = not in_string
                continue
            
            if not in_string:
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
                    if "arguments" in tool_call_data or "parameters" in tool_call_data:
                        return parse_tool_call_from_json(tool_call_data)
            except (json.JSONDecodeError, ValueError):
                # 尝试替换 Python 字面量
                try:
                    json_str_fixed = re.sub(r'\bNone\b', 'null', json_str)
                    json_str_fixed = re.sub(r'\bTrue\b', 'true', json_str_fixed)
                    json_str_fixed = re.sub(r'\bFalse\b', 'false', json_str_fixed)
                    tool_call_data = json.loads(json_str_fixed)
                    if isinstance(tool_call_data, dict) and "name" in tool_call_data:
                        if "arguments" in tool_call_data or "parameters" in tool_call_data:
                            return parse_tool_call_from_json(tool_call_data)
                except (json.JSONDecodeError, ValueError):
                    continue
    
    # 方法2: 如果方法1失败，使用更智能的方法：查找以 { 开头、包含 "name" 和 "arguments" 的 JSON 对象
    # 使用栈来匹配大括号，提取所有可能的 JSON 对象，然后选择最合适的
    # 注意：需要正确处理字符串中的转义字符
    candidates = []
    start_idx = content.find('{')
    
    while start_idx != -1:
        # 从当前位置开始，尝试找到匹配的 JSON 对象
        brace_count = 0
        end_idx = start_idx
        in_string = False
        escape_next = False
        
        for i in range(start_idx, len(content)):
            if escape_next:
                # 当前字符是转义字符的一部分，跳过
                escape_next = False
                continue
            
            if content[i] == '\\':
                # 转义字符，下一个字符需要跳过
                escape_next = True
                continue
            
            if content[i] == '"' and not escape_next:
                # 切换字符串状态（但需要检查是否是转义的引号）
                in_string = not in_string
                continue
            
            if not in_string:
                # 只在非字符串状态下计算括号
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
                    # 检查是否包含 arguments 或 parameters 字段
                    if "arguments" in tool_call_data or "parameters" in tool_call_data:
                        # 这是一个有效的工具调用候选
                        # 计算优先级：优先选择包含 "arguments" 且 name 和 arguments 都存在的
                        priority = 0
                        if "arguments" in tool_call_data:
                            priority += 2
                        if "parameters" in tool_call_data:
                            priority += 1
                        if isinstance(tool_call_data.get("arguments") or tool_call_data.get("parameters"), dict):
                            priority += 1
                        
                        candidates.append((priority, tool_call_data, start_idx))
            except (json.JSONDecodeError, ValueError):
                # 如果 JSON 解析失败，尝试多种修复方法
                try:
                    # 方法1: 替换 Python 字面量
                    json_str_fixed = re.sub(r'\bNone\b', 'null', json_str)
                    json_str_fixed = re.sub(r'\bTrue\b', 'true', json_str_fixed)
                    json_str_fixed = re.sub(r'\bFalse\b', 'false', json_str_fixed)
                    tool_call_data = json.loads(json_str_fixed)
                    if isinstance(tool_call_data, dict) and "name" in tool_call_data:
                        if "arguments" in tool_call_data or "parameters" in tool_call_data:
                            priority = 0
                            if "arguments" in tool_call_data:
                                priority += 2
                            if "parameters" in tool_call_data:
                                priority += 1
                            if isinstance(tool_call_data.get("arguments") or tool_call_data.get("parameters"), dict):
                                priority += 1
                            
                            candidates.append((priority, tool_call_data, start_idx))
                except (json.JSONDecodeError, ValueError):
                    # 方法2: 尝试修复字符串值中的未转义引号
                    # 这种情况发生在从 JSON 文件读取时，引号已经被解析器处理了
                    # 我们需要转义字符串值中的引号，但保留 JSON 结构中的引号
                    try:
                        # 使用一个更智能的方法：找到所有字符串值，转义其中的引号
                        # 策略：使用正则表达式找到所有字符串值（在引号对之间），转义其中的引号
                        # 但这个方法比较复杂，因为需要正确识别字符串边界
                        
                        # 更简单的方法：尝试使用 json.dumps 重新序列化（但这需要先部分解析）
                        # 或者：手动转义字符串值中的引号
                        # 我们使用一个启发式方法：如果引号后面跟着字母、数字或某些符号，可能是字符串中的引号
                        
                        fixed_json = []
                        i = 0
                        in_string = False
                        escape_next = False
                        string_start = -1
                        
                        while i < len(json_str):
                            char = json_str[i]
                            
                            if escape_next:
                                fixed_json.append(char)
                                escape_next = False
                                i += 1
                                continue
                            
                            if char == '\\':
                                fixed_json.append(char)
                                escape_next = True
                                i += 1
                                continue
                            
                            if char == '"':
                                if not in_string:
                                    # 字符串开始
                                    in_string = True
                                    string_start = i
                                    fixed_json.append(char)
                                else:
                                    # 检查这是字符串结束还是字符串中的引号
                                    # 向前查找，找到下一个非空白字符
                                    j = i + 1
                                    while j < len(json_str) and json_str[j] in [' ', '\n', '\r', '\t', '\\']:
                                        if json_str[j] == '\\':
                                            j += 2  # 跳过转义字符和下一个字符
                                            continue
                                        j += 1
                                    
                                    # 如果下一个非空白字符是结构字符，说明是字符串结束
                                    if j >= len(json_str) or json_str[j] in [':', ',', '}', ']']:
                                        in_string = False
                                        fixed_json.append(char)
                                    else:
                                        # 字符串中的引号，需要转义
                                        fixed_json.append('\\"')
                                i += 1
                                continue
                            
                            fixed_json.append(char)
                            i += 1
                        
                        json_str_fixed2 = ''.join(fixed_json)
                        tool_call_data = json.loads(json_str_fixed2)
                        if isinstance(tool_call_data, dict) and "name" in tool_call_data:
                            if "arguments" in tool_call_data or "parameters" in tool_call_data:
                                priority = 0
                                if "arguments" in tool_call_data:
                                    priority += 2
                                if "parameters" in tool_call_data:
                                    priority += 1
                                if isinstance(tool_call_data.get("arguments") or tool_call_data.get("parameters"), dict):
                                    priority += 1
                                
                                candidates.append((priority, tool_call_data, start_idx))
                    except (json.JSONDecodeError, ValueError, Exception):
                        pass
        
        # 继续查找下一个 {
        start_idx = content.find('{', start_idx + 1)
    
    # 如果有候选，选择优先级最高的（如果优先级相同，选择第一个出现的）
    if candidates:
        # 按优先级降序排序，优先级相同时按位置排序
        candidates.sort(key=lambda x: (-x[0], x[2]))
        _, tool_call_data, _ = candidates[0]
        return parse_tool_call_from_json(tool_call_data)
    
    return None


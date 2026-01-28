import asyncio
import logging
import os

import openai

from rllm.engine.rollout.rollout_engine import ModelOutput, RolloutEngine
from rllm.globals import THOUGHT_DELIMITER_END, THOUGHT_DELIMITER_START
from rllm.parser import ChatTemplateParser
from rllm.tools.tool_base import Tool
from rllm.workflows import TerminationEvent, TerminationReason


class OpenAIEngine(RolloutEngine):
    def __init__(self, model: str = "", tokenizer=None, max_prompt_length: int = 4096, max_response_length: int = 4096, max_model_length: int | None = None, api_retries: int = 3, base_url: str = "https://api.openai.com/v1", api_key: str = os.getenv("OPENAI_API_KEY"), sampling_params: dict | None = None, tools: list[Tool | dict] = None, accumulate_reasoning: bool = False, **kwargs):
        self.model = model
        self.max_prompt_length = max_prompt_length
        self.max_response_length = max_response_length
        self.max_model_length = max_model_length - 1 if max_model_length is not None else max_prompt_length + max_response_length - 1
        self.api_retries = api_retries
        self.sampling_params = sampling_params or {}
        self.tools = tools or []
        self.accumulate_reasoning = accumulate_reasoning

        self.tokenizer = tokenizer
        if self.tokenizer is not None:
            self.chat_parser = ChatTemplateParser.get_parser(self.tokenizer, disable_thinking=kwargs.get("disable_thinking", False))
            self._use_chat_completions = False
        else:
            # In this case, we cannot enforce max prompt length or dynamically adjust max_tokens <= max_response_length if needed
            print("No tokenizer provided to OpenAIEngine, will use the chat completions endpoint.")
            self._use_chat_completions = True

        self.client = openai.AsyncOpenAI(base_url=base_url, api_key=api_key)
        logging.getLogger("httpx").setLevel(logging.WARNING)

    def _prepare_max_tokens_param(self, sampling_params: dict, prompt_length: int = None) -> dict:
        """Prepare max tokens parameter for API call (supports O3's max_completion_tokens)."""
        if "max_completion_tokens" in sampling_params:
            return {"max_completion_tokens": sampling_params.pop("max_completion_tokens")}

        max_tokens = sampling_params.pop("max_tokens", sampling_params.pop("max_new_tokens", self.max_response_length))

        # Adjust for prompt length if provided (completion method needs this)
        if prompt_length and self.max_model_length:
            remaining = self.max_model_length - prompt_length
            if remaining <= max_tokens:
                max_tokens = remaining
                print(f"Warning: Decreasing max_tokens to {max_tokens} to stay within max_model_length")

        return {"max_tokens": max_tokens}

    async def chat_completion(self, messages: list[dict], **kwargs) -> ModelOutput:
        kwargs.pop("application_id", None)
        kwargs.pop("validate", None)
        kwargs.pop("model", None)
        kwargs.pop("enforce_max_prompt_length", None)

        # 提取 tools 参数，优先使用传入的，否则使用 self.tools
        tools = kwargs.pop("tools", self.tools)
        # 转换 tools 为 OpenAI 格式
        if tools:
            formatted_tools = []
            for tool in tools:
                if isinstance(tool, dict):
                    # 如果已经是 OpenAI 格式的 dict，直接使用
                    if "type" in tool and "function" in tool:
                        formatted_tools.append(tool)
                    else:
                        # 其他格式的 dict，跳过
                        continue
                elif hasattr(tool, "name") and hasattr(tool, "description"):
                    # 处理 EnvironmentTool 对象：转换为 OpenAI 格式
                    _tool = {"type": "function", "function": {}}
                    _function = _tool["function"]
                    _function["name"] = tool.name
                    _function["description"] = tool.description
                    _function["parameters"] = {
                        "type": "object",
                        "properties": tool.arguments,
                        "additionalProperties": False,
                    }
                    # _function["strict"] = True  # this is not supported by reasoning models such as o3
                    if len(tool.arguments) > 0:
                        _function["parameters"]["required"] = list(tool.arguments.keys())
                    formatted_tools.append(_tool)
                elif hasattr(tool, "json"):
                    # 尝试从 Tool 对象获取 json 属性
                    tool_json = tool.json
                    if isinstance(tool_json, dict) and "type" in tool_json and "function" in tool_json:
                        formatted_tools.append(tool_json)
            tools = formatted_tools if formatted_tools else None
        else:
            tools = None

        sampling_params = self.sampling_params.copy()
        sampling_params.update(kwargs)

        create_params = self._prepare_max_tokens_param(sampling_params)

        retries = self.api_retries
        while retries > 0:
            try:
                # 构建 API 调用参数
                api_kwargs = {
                    "model": self.model,
                    "messages": messages,
                    "timeout": 3600,
                    **create_params,
                    **sampling_params
                }
                # 只有在有 tools 时才添加 tools 参数
                if tools:
                    api_kwargs["tools"] = tools
                    # 如果 sampling_params 中没有指定 tool_choice，默认使用 "auto"
                    if "tool_choice" not in api_kwargs:
                        api_kwargs["tool_choice"] = "auto"
                
                response = await self.client.chat.completions.create(**api_kwargs)

                content = response.choices[0].message.content
                reasoning = response.choices[0].message.reasoning if hasattr(response.choices[0].message, "reasoning") and isinstance(response.choices[0].message.reasoning, str) else ""
                tool_calls = response.choices[0].message.tool_calls if hasattr(response.choices[0].message, "tool_calls") and isinstance(response.choices[0].message.tool_calls, list) else []

                # Build text with reasoning if available, otherwise use content
                if reasoning:
                    text = f"{THOUGHT_DELIMITER_START}\n{reasoning}\n{THOUGHT_DELIMITER_END}\n\n{content}"
                else:
                    text = content

                prompt_length = response.usage.prompt_tokens
                completion_length = response.usage.completion_tokens
                finish_reason = response.choices[0].finish_reason

                return ModelOutput(
                    text=text,
                    content=content,
                    reasoning=reasoning,
                    tool_calls=tool_calls,
                    prompt_ids=[],
                    completion_ids=[],
                    prompt_length=prompt_length,
                    completion_length=completion_length,
                    finish_reason=finish_reason,
                )

            except openai.RateLimitError:
                retries -= 1
                if retries == 0:
                    raise Exception("Rate limit reached and retries exhausted.") from None
                print("Sleep for 5 seconds for API limit.")
                await asyncio.sleep(5)

            except Exception as e:
                retries -= 1
                if retries == 0:
                    raise Exception(f"Error processing content after retries: {e}") from e
                print(f"Error: {e}, retrying...")
                await asyncio.sleep(1)

    async def completion(self, prompt: str, **kwargs) -> ModelOutput:
        kwargs.pop("application_id", None)
        kwargs.pop("validate", None)
        kwargs.pop("model", None)
        enforce_max_prompt_length = kwargs.pop("enforce_max_prompt_length", True)

        sampling_params = self.sampling_params.copy()
        sampling_params.update(kwargs)

        prompt_ids = self.tokenizer.encode(prompt, add_special_tokens=False)
        prompt_length = len(prompt_ids)

        if enforce_max_prompt_length and (prompt_length > self.max_prompt_length or prompt_length > self.max_model_length):
            raise TerminationEvent(TerminationReason.MAX_PROMPT_LENGTH_EXCEEDED)

        create_params = self._prepare_max_tokens_param(sampling_params, prompt_length)

        retries = self.api_retries
        while retries > 0:
            try:
                response = await self.client.completions.create(model=self.model, prompt=prompt, timeout=3600, **create_params, **sampling_params)

                text = response.choices[0].text
                completion_ids = self.tokenizer.encode(text, add_special_tokens=False)
                # parse成{'content': '', 'reasoning': None, 'tool_calls': [ToolCall(name='view', arguments={'path': 'solution.py'})]}的格式
                parsed_output = self.chat_parser.parse_completion(completion_ids)

                prompt_length = response.usage.prompt_tokens
                completion_length = response.usage.completion_tokens
                finish_reason = response.choices[0].finish_reason

                return ModelOutput(
                    text=text,
                    content=parsed_output["content"],
                    reasoning=parsed_output["reasoning"],
                    tool_calls=parsed_output["tool_calls"],
                    prompt_ids=prompt_ids,
                    completion_ids=completion_ids,
                    prompt_length=prompt_length,
                    completion_length=completion_length,
                    finish_reason=finish_reason,
                )

            except openai.RateLimitError:
                retries -= 1
                if retries == 0:
                    raise Exception("Rate limit reached and retries exhausted.") from None
                print("Sleep for 5 seconds for API limit.")
                await asyncio.sleep(5)

            except Exception as e:
                retries -= 1
                if retries == 0:
                    raise Exception(f"Error processing content after retries: {e}") from e
                print(f"Error: {e}, retrying...")
                await asyncio.sleep(1)

    async def get_model_response(self, messages: list[dict], **kwargs) -> ModelOutput:
        if self._use_chat_completions:
            accumulate_reasoning = kwargs.pop("accumulate_reasoning", self.accumulate_reasoning)
            if accumulate_reasoning:
                raise ValueError("Accumulate reasoning is not supported for chat completions endpoint.")
            # 对于 chat completions，tools 会被传递到 chat_completion 方法中处理
            return await self.chat_completion(messages, **kwargs)
        else:
            tools = kwargs.pop("tools", self.tools)
            accumulate_reasoning = kwargs.pop("accumulate_reasoning", self.accumulate_reasoning)
            prompt = self.chat_parser.parse(messages, add_generation_prompt=True, is_first_msg=True, tools=tools, accumulate_reasoning=accumulate_reasoning)
            return await self.completion(prompt, **kwargs)

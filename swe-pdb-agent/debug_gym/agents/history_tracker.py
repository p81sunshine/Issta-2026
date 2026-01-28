import copy
from dataclasses import asdict

from debug_gym.gym.envs.env import EnvInfo
from debug_gym.llms.base import LLM, LLMResponse


class HistoryTracker:
    def __init__(self, history_steps: int) -> None:
        self.history_steps = history_steps
        self.reset()

    def reset(self) -> None:
        self.memory: list[EnvInfo] = []
        self.prompt_response_pairs: list[LLMResponse | None] = []

    def step(
        self,
        new_info: EnvInfo,
        llm_responses: list[LLMResponse] | LLMResponse | None = None,
    ) -> None:
        """llm_responses can be None since the initial state does not have prompt and response"""
        self.memory.append(copy.deepcopy(new_info))
        llm_responses = llm_responses or []
        if not isinstance(llm_responses, list):
            llm_responses = [llm_responses]
        self.prompt_response_pairs.append(copy.deepcopy(llm_responses))

    def get(self):
        # return the history_steps latest steps
        return (
            self.memory[-self.history_steps :],
            self.prompt_response_pairs[-self.history_steps :],
        )

    def get_all(self):
        return self.memory

    def json(self, game_step=None):
        if len(self.memory) == 0:
            return {}
        if game_step is None:
            # retrieve the most recent step
            game_step = len(self.memory) - 1
        if game_step == 0:
            # initial state
            json_out = {
                "step_id": game_step,
                "reasoning": None,
                "content": None,
                "action": None,  # env reset
                "obs": self.memory[0].step_observation.observation,
                "rewrite_consumed": 0,
                "prompt_response_pairs": None,
            }
        else:
            json_out = {
                "step_id": game_step,
                "content": self.memory[game_step].action_content,
                "reasoning": self.memory[game_step].action_reasoning,
                "action": asdict(self.memory[game_step].action_tool_call),
                "obs": self.memory[game_step].step_observation.observation,
                "rewrite_consumed": self.memory[game_step].rewrite_counter,
            }
            # prompt_response_pairs could be empty for the initial state
            if self.prompt_response_pairs[game_step]:
                json_out["prompt_response_pairs"] = [
                    # doesn't include None values
                    asdict(
                        p,
                        dict_factory=lambda x: {k: v for (k, v) in x if v is not None},
                    )
                    for p in self.prompt_response_pairs[game_step]
                ]

        return json_out

    def score(self):
        return sum([memory.score for memory in self.memory])

    def __len__(self):
        return len(self.memory)

    def clone(self):
        return copy.deepcopy(self)


def build_history_prompt(
    history: HistoryTracker,
    llm: LLM,
    reset_prompt_history_after_rewrite: bool = False,
    enable_recency_filter: bool = False,
    memory_size: int = None,
):
    _history, _prompt_response_pairs = history.get()
    latest_rewrite_step = 0
    # Find the latest rewrite step if reset_prompt_history_after_rewrite
    if reset_prompt_history_after_rewrite:
        for i in range(len(_history)):
            if _history[i].rewrite_counter == _history[-1].rewrite_counter:
                latest_rewrite_step = i
                break
    _messages = []
    for history_info, response in zip(
        _history[latest_rewrite_step:], _prompt_response_pairs[latest_rewrite_step:]
    ):
        _messages.extend(llm.format_tool_call_history(history_info, response))

    # Apply recency-based filtering if enabled
    if enable_recency_filter and memory_size is not None and memory_size > 0:
        _messages = _apply_recency_filter(_messages, memory_size)

    return _messages


def _apply_recency_filter(messages: list[dict], memory_size: int) -> list[dict]:
    """
    Apply recency-based filtering to tool responses.
    Retains all assistant messages (thoughts and actions) but only keeps
    the most recent K tool responses, where K = memory_size.
    Earlier tool responses are masked (content set to empty string).
    
    Args:
        messages: List of message dictionaries
        memory_size: Number of recent tool responses to retain (K)
    
    Returns:
        Filtered list of messages with older tool responses masked
    """
    if not messages:
        return messages

    # Count total number of tool messages first
    total_tool_messages = sum(1 for msg in messages if msg.get("role") == "tool")
    if total_tool_messages == 0:
        # No tool messages to filter
        return messages
    
    K = memory_size
    # Calculate the earliest tool message index to retain
    # St(K) = { i ∈ {0, ..., t-1} | i ≥ t - K }
    # where t is the total number of tool responses (0-indexed)
    earliest_retain_index = max(0, total_tool_messages - K)
    
    # Process all messages
    tool_counter = 0  # Track which tool message we're processing (0-indexed)
    filtered_messages = []
    for msg in messages:
        if msg.get("role") == "tool":
            # This is a tool message
            msg_copy = msg.copy()
            if tool_counter >= earliest_retain_index:
                # Retain this tool response (it's in the most recent K messages)
                filtered_messages.append(msg_copy)
            else:
                # Mask this tool response by setting content to empty string
                msg_copy["content"] = ""
                filtered_messages.append(msg_copy)
            tool_counter += 1
        else:
            # Always retain non-tool messages (assistant, user, system, etc.)
            # Create a copy to avoid modifying the original
            filtered_messages.append(msg.copy())
    
    return filtered_messages

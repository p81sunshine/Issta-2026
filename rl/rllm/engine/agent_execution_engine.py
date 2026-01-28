import asyncio
import logging
import time
import traceback
import uuid
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Optional

import torch

from rllm.agents.agent import Action, BaseAgent, Trajectory
from rllm.agents.utils import (
    convert_messages_to_tokens_and_masks,
    get_recent_assistant_user_messages,
)
from rllm.environments.base.base_env import BaseEnv
from rllm.environments.env_utils import (
    compute_mc_return,
    compute_trajectory_reward,
)
from rllm.parser import ChatTemplateParser
from rllm.utils import colorful_print
from rllm.utils.visualization import colorful_print_to_terminal

logger = logging.getLogger(__name__)


class SimpleTimeTracker:
    """简单的执行时间跟踪器"""
    
    def __init__(self, enable_output: bool = True):
        """
        Args:
            enable_output: 是否输出 timing 信息到 stdout。如果为 False，则不会输出到日志。
        """
        self.trajectory_times: Dict[int, Dict[str, float]] = {}
        self.enable_output = enable_output
        
    def start_trajectory(self, trajectory_id: int) -> None:
        """开始跟踪trajectory"""
        self.trajectory_times[trajectory_id] = {
            "start_time": time.time(),
            "env_time": 0.0,
            "llm_time": 0.0,
            "total_steps": 0
        }
        
    def record_llm_time(self, trajectory_id: int, llm_time: float, response_length: int = None, prompt_length: int = None, action: str = None) -> None:
        """记录LLM推理时间"""
        if trajectory_id in self.trajectory_times:
            self.trajectory_times[trajectory_id]["llm_time"] += llm_time
            total_time = time.time() - self.trajectory_times[trajectory_id]["start_time"]
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if self.enable_output:
                length_info = f", 响应长度: {response_length}" if response_length is not None else ""
                prompt_info = f", Prompt长度: {prompt_length}" if prompt_length is not None else ""
                action_info = f", Action: {action}" if action is not None else ""
                colorful_print_to_terminal(
                    f"[Timing] [{current_time}] Trajectory {trajectory_id} - LLM推理: {llm_time:.2f}s (累计: {self.trajectory_times[trajectory_id]['llm_time']:.2f}s, 总时间: {total_time:.2f}s{length_info}{prompt_info}{action_info})",
                    "blue"
                )
            
    def record_env_time(self, trajectory_id: int, env_time: float, step: int, action: str = None) -> None:
        """记录环境执行时间"""
        if trajectory_id in self.trajectory_times:
            self.trajectory_times[trajectory_id]["env_time"] += env_time
            self.trajectory_times[trajectory_id]["total_steps"] = step + 1
            total_time = time.time() - self.trajectory_times[trajectory_id]["start_time"]
            if self.enable_output:
                action_info = f", Action: {action}" if action is not None else ""
                colorful_print_to_terminal(
                    f"[Timing] Trajectory {trajectory_id} - Step {step+1} 环境执行: {env_time:.2f}s (累计: {self.trajectory_times[trajectory_id]['env_time']:.2f}s, 总时间: {total_time:.2f}s{action_info})",
                    "yellow"
                )
            
    def complete_trajectory(self, trajectory_id: int, reason: str) -> None:
        """完成trajectory跟踪"""
        if trajectory_id not in self.trajectory_times:
            return
            
        times = self.trajectory_times[trajectory_id]
        total_time = time.time() - times["start_time"]
        
        if self.enable_output:
            colorful_print_to_terminal(
                f"[Timing] Trajectory {trajectory_id} 完成 - 总时间: {total_time:.2f}s "
                f"(环境: {times['env_time']:.2f}s, LLM: {times['llm_time']:.2f}s, "
                f"步数: {times['total_steps']}), 原因: {reason}",
                "green" if reason == "ENV_DONE" else "yellow"
            )
        
        # 从跟踪中移除
        del self.trajectory_times[trajectory_id]


class AgentExecutionEngine:
    def __init__(
        self,
        engine_name="openai",
        tokenizer=None,
        rollout_engine=None,
        chat_parser=None,
        n_parallel_agents=128,  # The number of active agents
        trajectory_timeout=None,
        gamma=0.2,
        api_retries=3,
        retry_limit=3,
        max_steps=5,
        max_response_length=8192,
        max_prompt_length=1024,
        config=None,
        agent_class=None,
        env_class=None,
        agent_args=None,
        rollout_engine_args=None,
        env_args=None,
        max_workers=64,  # The number of concurrent env operations
        enforce_max_prompt_length=False,  # If enabled, applies max_prompt check per step
        overlong_filter=False,  # Filter for overlong trajectories (i.e. TRUNCATION, MAX_STEPS, TIMEOUT)
        enable_timing_output=True,  # If False, timing information will not be printed to stdout/log
        **kwargs,
    ):
        if agent_args is None:
            agent_args = {}
        if rollout_engine_args is None:
            rollout_engine_args = {}
        if env_args is None:
            env_args = {}

        self.config = config
        self.tokenizer = tokenizer
        self.engine_name = engine_name
        self.n_parallel_agents = n_parallel_agents
        self.max_env_workers = max_workers
        self.overlong_filter = overlong_filter
        
        # 打印配置信息以便调试
        logger.info(f"AgentExecutionEngine initialized: n_parallel_agents={n_parallel_agents}, max_workers={max_workers}")

        # For interaction
        self.gamma = gamma
        self.retry_limit = retry_limit
        self.api_retries = api_retries
        
        # 初始化时间跟踪器
        self.time_tracker = SimpleTimeTracker(enable_output=enable_timing_output)
        self.max_steps = max_steps
        self.max_response_length = max_response_length
        self.max_prompt_length = max_prompt_length
        self.enforce_max_prompt_length = enforce_max_prompt_length
        self.disable_thinking = self.config.get("rllm", {}).get("disable_thinking", False) if self.config is not None else False

        self.agent_class = agent_class
        self.agent_args = agent_args
        self.env_class = env_class
        self.env_args = env_args

        self.agents = [None for _ in range(n_parallel_agents)]
        self.envs = [None for _ in range(n_parallel_agents)]

        self.trajectory_timeout = trajectory_timeout
        if not trajectory_timeout:
            self.trajectory_timeout = int(1e9)

        if env_class is not None:
            assert env_class.is_multithread_safe(), "Environment must be multithread safe for async engine"

        if chat_parser is None:
            self.chat_parser = ChatTemplateParser.get_parser(self.tokenizer, disable_thinking=self.disable_thinking)
        else:
            self.chat_parser = chat_parser

        self.rollout_engine_args = rollout_engine_args
        self.sampling_params = kwargs.get("sampling_params", {})  # for openai api requests

        assert self.engine_name in ["openai", "verl"], "Currently only openai and verl are supported as rollout engine"
        if self.engine_name == "openai":
            from rllm.engine.rollout.openai_engine import OpenAIEngine

            self.rollout_engine = OpenAIEngine(
                **rollout_engine_args,
                api_retries=api_retries,
                tokenizer=self.tokenizer,
                max_prompt_length=self.max_prompt_length,
                max_response_length=self.max_response_length,
                disable_thinking=self.disable_thinking,
            )
        elif self.engine_name == "verl":
            from rllm.engine.rollout.verl_engine import VerlEngine

            self.rollout_engine = VerlEngine(
                config=self.config,
                rollout_manager=rollout_engine,
                tokenizer=self.tokenizer,
                disable_thinking=self.disable_thinking,
            )

    async def get_model_response(self, prompt, application_id, **kwargs) -> str:
        """
        Compute model response asynchronously based on the engine type.

        This function is multithread safe and routes the request to the appropriate
        engine-specific handler.

        Args:
            prompt: The input prompt to send to the model
            application_id: Unique identifier for the application
            **kwargs: Additional arguments to pass to the model

        Returns:
            The model's response text

        Raises:
            NotImplementedError: If the engine type is not supported
        """

        sampling_params = self.sampling_params.copy()
        sampling_params.update(kwargs)

        if self.engine_name == "openai":
            output = await self.rollout_engine.get_model_response(prompt, application_id=application_id, enforce_max_prompt_length=False, **sampling_params)
            return output.text
        elif self.engine_name == "verl":
            meta_data = sampling_params.pop("meta_info", {})
            validate = meta_data.get("validate", False)
            output = await self.rollout_engine.get_model_response(prompt, application_id=application_id, validate=validate, enforce_max_prompt_length=False, **sampling_params)
            return output.text
        else:
            raise NotImplementedError(f"Engine type '{self.engine_name}' not supported")

    def update_envs_and_agents(self, envs, agents):
        """
        Update the environments and agents.

        Args:
            envs: List of environments to use
            agents: List of agents to use
        """
        assert len(agents) == len(envs), f"Number of agents must equal to number of environments but received, {len(agents)} and {len(envs)}"
        
        # CRITICAL FIX: Close old environments before replacing them to prevent resource leaks
        if hasattr(self, 'envs') and self.envs is not None:
            for idx, old_env in enumerate(self.envs):
                if old_env is not None:
                    try:
                        old_env.close()
                        logger.info(f"Closed old environment at index {idx}")
                    except Exception as e:
                        logger.warning(f"Failed to close old environment at index {idx}: {e}")
        
        self.envs = envs
        # For keeping track of the environment index in the batch.
        for idx, env in enumerate(envs):
            env.idx = idx
        self.agents = agents

    async def run_agent_trajectory_async(self, idx, application_id, seed=0, mode="Text", **kwargs):
        """Run a single agent's trajectory asynchronously"""
        agent = self.agents[idx]
        env = self.envs[idx]
        # env_id = env.env_id

        # 开始跟踪这个trajectory的时间
        self.time_tracker.start_trajectory(idx)

        termination_reason = None
        prompt_token_len = 0
        prompt_tokens = []
        response_token_len = 0
        response_tokens = []
        response_masks = []
        total_time = 0.0
        reward_time = None
        llm_time = 0.0
        env_time = 0.0
        reward = 0.0

        # for step return
        episode_steps = []

        # Reset environment with the task using the executor
        loop = asyncio.get_event_loop()
        try:
            observation, info = await loop.run_in_executor(self.executor, env.reset)
        except asyncio.CancelledError as e:
            # 区分是超时取消还是 executor 关闭导致的取消
            if self.executor._shutdown:
                logger.warning(f"Trajectory {idx}: env.reset() was cancelled because executor was shutdown")
            else:
                logger.warning(f"Trajectory {idx}: env.reset() was cancelled (likely due to timeout or resource contention)")
            raise
        info["max_steps"] = self.max_steps

        # Check if eval timed out during reset - if so, mask this trajectory
        if info.get("reset_eval_timeout", False):
            termination_reason = "TIMEOUT"
            await loop.run_in_executor(self.executor, env.close)
            self.time_tracker.complete_trajectory(idx, termination_reason)
            colorful_print(
                f"Trajectory {idx} masked due to eval timeout during reset. This trajectory will be excluded from RL training.\n",
                "red",
            )
            
            # Create a dummy trajectory with everything masked out
            trajectory = agent.trajectory
            trajectory.reward = 0.0
            
            if mode == "Text":
                return trajectory
            elif mode == "Token":
                # Return minimal token result with everything masked, matching normal format
                token_result = {
                    "prompt_tokens": torch.tensor([0], dtype=torch.long),  # 1D dummy token
                    "response_tokens": torch.tensor([0], dtype=torch.long),  # 1D dummy token  
                    "response_masks": torch.tensor([0], dtype=torch.long),  # 1D masked out
                    "trajectory_reward": 0.0,
                    "idx": env.idx,
                    "chat_completions": [],  # Empty chat completions
                    "metrics": {
                        "steps": 0,
                        "reward_time": 0.0,
                        "env_time": 0.0,
                        "llm_time": 0.0,
                        "total_time": 0.0,
                    },
                }
                return token_result
            elif mode == "Conversation":
                return {"idx": env.idx, "messages": []}
            elif mode == "Step":
                return {
                    "steps": [],
                    "trajectory_reward": 0.0,
                    "idx": idx,
                    "mc_returns": [],
                }

        # 从环境的 info 中提取 tools（如果可用）
        tools_for_model = info.get("tools_openai_format", None)

        # Reset agent
        agent.reset()
        # Update agent internal state from environment.
        agent.update_from_env(
            observation=observation,  # Raw observation from environment
            reward=0.0,
            done=False,
            info=info,
        )
        messages = agent.chat_completions
        prompt_tokens, _ = convert_messages_to_tokens_and_masks(messages, tokenizer=self.tokenizer, parser=self.chat_parser, contains_first_msg=True, contains_generation_msg=True)
        prompt_token_len = len(prompt_tokens)
        # Note, this should never happen!
        if prompt_token_len > self.max_prompt_length:
            # Instead of raising an exception, treat this as a masked-out trajectory
            # This prevents training from being interrupted by overly long initial prompts
            await loop.run_in_executor(self.executor, env.close)
            colorful_print(f"Overlong Prompt: {messages}", "red")
            colorful_print(
                f"Trajectory {idx} skipped due to initial prompt length {prompt_token_len} exceeding max_prompt_length {self.max_prompt_length}. \n",
                "red",
            )
            
            # Create a dummy trajectory with everything masked out
            trajectory = agent.trajectory
            trajectory.reward = 0.0
            
            if mode == "Text":
                return trajectory
            elif mode == "Token":
                # Return minimal token result with everything masked, matching normal format
                token_result = {
                    "prompt_tokens": torch.tensor([0], dtype=torch.long),  # 1D dummy token
                    "response_tokens": torch.tensor([0], dtype=torch.long),  # 1D dummy token  
                    "response_masks": torch.tensor([0], dtype=torch.long),  # 1D masked out
                    "trajectory_reward": 0.0,
                    "idx": env.idx,
                    "chat_completions": [],  # Empty chat completions
                    "metrics": {
                        "steps": 0,
                        "reward_time": 0.0,
                        "env_time": 0.0,
                        "llm_time": 0.0,
                        "total_time": 0.0,
                    },
                }
                return token_result
            elif mode == "Conversation":
                return {"idx": env.idx, "messages": []}
            elif mode == "Step":
                return {
                    "steps": [],
                    "trajectory_reward": 0.0,
                    "idx": idx,
                    "mc_returns": [],
                }

        for step_idx in range(self.max_steps):
            
            # Get action from agent
            prompt_messages = agent.chat_completions.copy()
            # Max remaining tokens left for the response
            # For enforced max prompt at each step, no need to deduct here
            if not self.enforce_max_prompt_length:
                max_tokens = self.max_response_length - response_token_len
            else:
                max_tokens = self.max_response_length

                # since max prompt is enforced, we filter out too long prompts.
                prompt_str = self.chat_parser.parse(prompt_messages, add_generation_prompt=True, is_first_msg=True)
                prompt_len = len(self.tokenizer.encode(prompt_str, add_special_tokens=False))
                if prompt_len > self.max_prompt_length:
                    termination_reason = "PROMPT_TRUNCATION"
                    break

            kwargs["max_tokens"] = max_tokens
            
            # 如果有 tools，传递给模型（使用最新的 tools_for_model）
            if tools_for_model:
                kwargs["tools"] = tools_for_model

            start_time = time.time()
            response = await self.get_model_response(prompt_messages, application_id, **kwargs)
            delta_time = time.time() - start_time
            llm_time += delta_time
            total_time += delta_time
            
            # 记录LLM推理时间
            response_length = len(response) if response else 0
            # 计算prompt长度
            prompt_str = self.chat_parser.parse(prompt_messages, add_generation_prompt=True, is_first_msg=True)
            prompt_length = len(self.tokenizer.encode(prompt_str, add_special_tokens=False))
            # Update steps
            prompt_response_pair = {
                "prompt": self.chat_parser.parse(prompt_messages, add_generation_prompt=True, is_first_msg=True),
                "response": response,
            }
            episode_steps.append(prompt_response_pair)

            # Update agent with model response
            action: Action = agent.update_from_model(response)
            action = action.action
            self.time_tracker.record_llm_time(idx, delta_time, response_length, prompt_length, str(action))

            # Take step in environment using the executor
            start_time = time.time()

            try:
                next_observation, reward, done, info = await asyncio.wait_for(loop.run_in_executor(self.executor, env.step, action), timeout=(self.trajectory_timeout - total_time))
                # 更新 tools_for_model（使用最新的 tools，支持动态工具添加/删除）
                tools_for_model = info.get("tools_openai_format", tools_for_model)
            except asyncio.TimeoutError:
                termination_reason = "ENV_TIMEOUT"
                if step_idx == 0:
                    colorful_print(f"Warning: Trajectory {idx} completed due to: {termination_reason} before able to perform 1 complete action. This might cause unexpected behavior. Consider increasing trajectory timeout limit.\n", "red")
                reward = 0

                # Try to extract response_tokens even if env timed out
                # The agent should have the assistant message from update_from_model
                if mode == "Token":
                    try:
                        chat_completions_messages = agent.chat_completions
                        assistant_message, _ = get_recent_assistant_user_messages(chat_completions_messages)
                        if assistant_message:
                            assistant_msg_tokens, assistant_msg_masks = convert_messages_to_tokens_and_masks([assistant_message], tokenizer=self.tokenizer, parser=self.chat_parser, contains_first_msg=False, contains_generation_msg=False)
                            if assistant_msg_tokens:
                                response_tokens.extend(assistant_msg_tokens)
                                response_masks.extend(assistant_msg_masks)
                    except Exception as e:
                        colorful_print(f"Warning: Failed to extract response tokens on timeout: {e}\n", "yellow")

                cur_step = agent.get_current_state()
                done = True
                cur_step.done = done
                break

            delta_time = time.time() - start_time
            env_time += delta_time
            total_time += delta_time
            
            # 记录环境执行时间
            action_str = str(action) if action is not None else "None"
            self.time_tracker.record_env_time(idx, delta_time, step_idx, action_str)
            info["max_steps"] = self.max_steps
            info["cur_tokens"] = response_token_len

            # Update agent internal state.
            agent.update_from_env(
                observation=next_observation,
                reward=reward,
                done=done,
                info=info,
            )

            cur_step = agent.get_current_state()
            cur_step.reward = reward
            cur_step.done = done
            cur_step.info.update(info)

            chat_completions_messages = agent.chat_completions
            assistant_message, env_messages = get_recent_assistant_user_messages(chat_completions_messages)

            # Check and convert to tokens if necessary
            assert assistant_message is not None or mode != "Token", "Assistant messages is none when accumulating token trajectories which should be conversations. This should not happen."
            assert env_messages is not None or mode != "Token", "Environment messages is none when accumulating token trajectories which should be conversations. This should not happen."
            assistant_msg_tokens, assistant_msg_masks = [], []
            env_msg_tokens, env_msg_masks = [], []
            if assistant_message:
                assistant_msg_tokens, assistant_msg_masks = convert_messages_to_tokens_and_masks([assistant_message], tokenizer=self.tokenizer, parser=self.chat_parser, contains_first_msg=False, contains_generation_msg=False)
            if env_messages:
                env_msg_tokens, env_msg_masks = convert_messages_to_tokens_and_masks(env_messages, tokenizer=self.tokenizer, parser=self.chat_parser, contains_first_msg=False, contains_generation_msg=True)

            # Update repsonse token length
            response_token_len += len(assistant_msg_tokens) + len(env_msg_tokens)
            # Reached maximum number of tokens for the trajectory
            if not self.enforce_max_prompt_length and response_token_len >= self.max_response_length:
                # Truncation length
                truncation_length = self.max_response_length - response_token_len
                # Truncate the response and masks
                if truncation_length < 0:
                    truncated_response_tokens = (assistant_msg_tokens + env_msg_tokens)[:truncation_length]
                    truncated_response_masks = (assistant_msg_masks + env_msg_masks)[:truncation_length]
                else:
                    # Edge case where the response is exactly the max response length.
                    truncated_response_tokens = assistant_msg_tokens + env_msg_tokens
                    truncated_response_masks = assistant_msg_masks + env_msg_masks
                # Update token collections
                response_tokens.extend(truncated_response_tokens)
                response_masks.extend(truncated_response_masks)

                cur_step = agent.get_current_state()
                if response_token_len - len(env_msg_tokens) > self.max_response_length:
                    cur_step.reward = 0.0
                cur_step.done = True
                termination_reason = "TRUNCATION"
                # handle returning
                break

            # Update the token version of trajectory
            response_tokens.extend(assistant_msg_tokens)
            response_masks.extend(assistant_msg_masks)
            observation = next_observation

            if total_time >= self.trajectory_timeout:
                termination_reason = "TIMEOUT"
                cur_step = agent.get_current_state()
                done = True
                cur_step.done = done
                break

            # Check if episode is done
            if done:
                termination_reason = "ENV_DONE"
                break

            response_tokens.extend(env_msg_tokens)
            response_masks.extend(env_msg_masks)

            if step_idx == self.max_steps - 1:
                termination_reason = "MAX_STEPS"

        masked_out = False
        if self.overlong_filter:
            if termination_reason == "TRUNCATION" or termination_reason == "MAX_STEPS" or termination_reason == "TIMEOUT":
                # Mask out the entire response for overlong trajectories if the reward is 0.
                response_masks = [0] * len(response_masks)
                masked_out = True

        if hasattr(env, "compute_final_reward") and not masked_out:
            cur_step = agent.get_current_state()
            start_time = time.time()
            reward = await loop.run_in_executor(self.executor, env.compute_final_reward)
            reward_time = time.time() - start_time
            cur_step.reward = reward
        # Closing environment using the executor.
        await loop.run_in_executor(self.executor, env.close)
        
        # 完成trajectory时间跟踪
        final_reason = termination_reason if termination_reason else "ENV_DONE"
        self.time_tracker.complete_trajectory(idx, final_reason)
            
        if termination_reason:
            if reward > 0:
                color = "green"
            else:
                color = "yellow"
            colorful_print(
                f"Trajectory {idx} completed due to: {termination_reason}. Reward is {reward}. \n",
                color,
            )
            if masked_out:
                colorful_print(f"Trajectory {idx} is masked out due to overlong filter.", "red")

        trajectory: Trajectory = agent.trajectory
        # Aggregate final trajectory statistics
        compute_trajectory_reward(trajectory)
        compute_mc_return(trajectory, gamma=self.gamma)

        if mode == "Text":
            return trajectory
        elif mode == "Token":
            token_result = {
                "prompt_tokens": torch.tensor(prompt_tokens, dtype=torch.long),
                "response_tokens": torch.tensor(response_tokens, dtype=torch.long),
                "response_masks": torch.tensor(response_masks, dtype=torch.long),
                "trajectory_reward": trajectory.reward,
                "idx": env.idx,
                "chat_completions": agent.chat_completions,
                "metrics": {
                    # Total number of steps taken in the trajectory
                    "steps": len(trajectory.steps),
                    # Time to calculate reward
                    "reward_time": reward_time,
                    # Total time spent in environment execution (env.step)
                    "env_time": env_time,
                    # Time to calculate response tokens
                    "llm_time": llm_time,
                    # Total time spent in the trajectory
                    "total_time": total_time,
                },
            }
            return token_result
        elif mode == "Conversation":
            return agent.chat_completions
        elif mode == "Step":
            steps_result = {
                "steps": episode_steps,
                "trajectory_reward": trajectory.reward,
                "idx": env.idx,
                "mc_returns": [step.mc_return for step in trajectory.steps][: len(episode_steps)],
            }
            return steps_result

    async def run_agent_trajectory_with_retry(self, idx, application_id, seed=0, mode="Text", **kwargs):
        for retry_count in range(self.retry_limit):
            try:
                return await asyncio.wait_for(self.run_agent_trajectory_async(idx, application_id=application_id, seed=seed, mode=mode, **kwargs), timeout=7200)
            except asyncio.TimeoutError:
                logger.error(f"Trajectory {idx} timed out after 7200 seconds (attempt {retry_count + 1}/{self.retry_limit})")
                traceback.print_exc()
                if retry_count < self.retry_limit - 1:
                    continue
                raise
            except asyncio.CancelledError:
                logger.error(f"Trajectory {idx} was cancelled (attempt {retry_count + 1}/{self.retry_limit})")
                traceback.print_exc()
                # CancelledError 通常不应该重试，因为表示任务被主动取消
                raise
            except Exception:
                logger.error(f"Trajectory {idx} failed with exception (attempt {retry_count + 1}/{self.retry_limit})")
                traceback.print_exc()
                if retry_count < self.retry_limit - 1:
                    continue
        traceback.print_exc()
        raise Exception(f"Trajectory {idx} cannot complete after {self.retry_limit} retries. Please check the log message")

    async def trajectory_generator(self, reset_seed=0, timing_raw=None, mode="Text", **kwargs):
        if timing_raw is None:
            timing_raw = {}
        assert all(env is not None and isinstance(env, BaseEnv) for env in self.envs), "All environments must be inheriting from BaseEnv"
        assert all(env.is_multithread_safe() for env in self.envs), "All environments must be multithread safe for async engine"  # type: ignore
        if not hasattr(self, "executor") or self.executor._shutdown:
            self.executor = ThreadPoolExecutor(max_workers=self.max_env_workers)
        semaphore = asyncio.Semaphore(self.n_parallel_agents)

        if self.engine_name == "verl":
            self.rollout_engine.wake_up()

        async def launch_one_trajectory_task(env_idx: int):
            async with semaphore:
                try:
                    application_id = str(uuid.uuid4())
                    result = await self.run_agent_trajectory_with_retry(
                        idx=env_idx,
                        application_id=application_id,
                        seed=reset_seed,
                        mode=mode,
                        **kwargs,
                    )
                except Exception as e:
                    import traceback

                    traceback.print_exc()
                    raise e
                return (env_idx, result)

        # Create all N conceptual tasks. Their execution will be throttled by the semaphore
        # and the availability of agent/env indices.
        tasks_to_run = [launch_one_trajectory_task(i) for i in range(len(self.envs))]
        
        # 用于追踪未完成的trajectory
        completed_indices = set()

        tasks_completed = 0
        for coro in asyncio.as_completed(tasks_to_run):
            try:
                env_idx, result = await coro
                # 记录完成的任务索引
                completed_indices.add(env_idx)
                
                tasks_completed += 1
                colorful_print(f"Number of Trajectories {tasks_completed}/{len(self.envs)} completed", "cyan")
                
                uncompleted_indices = [i for i in range(len(self.envs)) if i not in completed_indices]
                colorful_print(f"[提醒] 剩余{len(uncompleted_indices)}个Trajectory未完成，索引为: {uncompleted_indices}", "magenta")
                
                yield result
            except Exception as e:
                raise e

        # Properly close all environments before shutdown
        loop = asyncio.get_event_loop()
        close_tasks = []
        for idx, env in enumerate(self.envs):
            if env is not None:
                try:
                    close_tasks.append(loop.run_in_executor(self.executor, env.close))
                except Exception as e:
                    logger.warning(f"Failed to initiate close for env {idx}: {e}")
        
        if close_tasks:
            try:
                await asyncio.gather(*close_tasks, return_exceptions=True)
            except Exception as e:
                logger.warning(f"Error during environment cleanup: {e}")

        if self.engine_name == "verl":
            self.rollout_engine.sleep()

        # Wait for executor to complete pending tasks before shutdown
        self.executor.shutdown(wait=True)

    async def execute_tasks(self, tasks: list[dict]):
        """
        Run asynchronous interactions between the agent and environment where each agent
        has its own environment instance and can proceed independently.

        Args:
            tasks: List of tasks to process
            max_concurrent: Maximum number of concurrent tasks to process (defaults to self.n_parallel_agents)

        Returns:
            A list of trajectories, one for each task.
        """
        if not hasattr(self, "executor") or self.executor._shutdown:
            self.executor = ThreadPoolExecutor(max_workers=self.max_env_workers)

        max_concurrent = self.n_parallel_agents

        # Initialize results list to store trajectories for all tasks
        all_trajectories = {}

        # Create a queue of tasks to process
        task_queue = list(enumerate(tasks))
        semaphore = asyncio.Semaphore(max_concurrent)
        index_queue: asyncio.Queue[int] = asyncio.Queue(maxsize=max_concurrent)
        for i in range(max_concurrent):
            index_queue.put_nowait(i)

        # Track completed trajectories
        completed = 0
        total = len(tasks)

        async def sem_wrapper(task_id, task):
            nonlocal completed
            async with semaphore:
                # Get an available index
                index = await index_queue.get()
                try:
                    self.envs[index] = self.env_class.from_dict({**task, **self.env_args})
                    self.agents[index] = self.agent_class(**self.agent_args)
                    assert self.agents[index] is not None and isinstance(self.agents[index], BaseAgent), "Agent is not initalized or not inheriting from BaseAgent"
                    self.agents[index].trajectory.task = task  # type: ignore
                    res = await self.run_agent_trajectory_async(index, application_id=task_id)
                    res.task = task
                    completed += 1
                    colorful_print(f"Progress: {completed}/{total} trajectories completed", "cyan")
                    return task_id, res
                finally:
                    # Put the index back in the queue when done
                    await index_queue.put(index)

        # Run all tasks concurrently
        results = await asyncio.gather(*[sem_wrapper(task_id, task) for task_id, task in task_queue])

        all_trajectories = {task_id: trajectory for task_id, trajectory in results}
        ordered_trajectories = [all_trajectories[i] for i in range(len(all_trajectories))]

        self.executor.shutdown(wait=False, cancel_futures=True)

        return ordered_trajectories

    def shutdown(self):
        if hasattr(self, "executor") and self.executor is not None:
            self.executor.shutdown()
            self.executor = None


class AsyncAgentExecutionEngine(AgentExecutionEngine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

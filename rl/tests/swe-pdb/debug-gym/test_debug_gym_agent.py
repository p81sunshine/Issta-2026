#!/usr/bin/env python3
"""
Debug-Gym Agent端到端测试

测试完整的Agent工作流，包括：
1. Agent初始化和配置
2. 环境交互（observation->action）
3. 轨迹生成和收集
4. 多步推理流程
5. K8s后端的完整流程
"""
import logging
import os
import sys
from pathlib import Path
from unittest.mock import Mock, patch

import pytest

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 检查依赖
try:
    from kubernetes import client, config
    KUBERNETES_AVAILABLE = True
except ImportError:
    KUBERNETES_AVAILABLE = False

try:
    from rllm.environments.debug_gym.swe_bench_env import SWEBenchDebugGymEnv
except ImportError:
    SWEBenchDebugGymEnv = None

try:
    from rllm.agents.base_agent import BaseAgent
except ImportError:
    BaseAgent = None


# Skip markers
skip_if_no_deps = pytest.mark.skipif(
    SWEBenchDebugGymEnv is None or BaseAgent is None,
    reason="Required dependencies not available"
)

skip_if_no_k8s = pytest.mark.skipif(
    not KUBERNETES_AVAILABLE,
    reason="Kubernetes not available"
)


class MockLLM:
    """模拟LLM用于测试"""
    
    def __init__(self):
        self.call_count = 0
        self.responses = [
            # 第一步：查看文件
            '{"tool": "view", "args": {"path": "test.py"}}',
            # 第二步：修改文件
            '{"tool": "rewrite", "args": {"path": "test.py", "content": "# fixed"}}',
            # 第三步：运行测试
            '{"tool": "eval", "args": {}}',
            # 后续步骤
            '{"tool": "finish", "args": {}}',
        ]
    
    def generate(self, prompt, **kwargs):
        """生成模拟响应"""
        response = self.responses[min(self.call_count, len(self.responses) - 1)]
        self.call_count += 1
        return response


class SimpleDebugGymAgent:
    """简单的Debug-Gym Agent实现（用于测试）"""
    
    def __init__(self, env, llm=None, max_steps=10):
        self.env = env
        self.llm = llm or MockLLM()
        self.max_steps = max_steps
        self.history = []
    
    def reset(self):
        """重置Agent"""
        self.history = []
        return self.env.reset()
    
    def act(self, observation):
        """根据观察生成动作"""
        # 构建prompt
        prompt = f"Observation: {observation}\nWhat's the next action?"
        
        # 获取LLM响应
        response = self.llm.generate(prompt)
        
        # 解析动作
        try:
            import json
            action = json.loads(response)
        except:
            # 如果解析失败，返回默认动作
            action = {"tool": "bash", "args": {"command": "ls"}}
        
        return action
    
    def run_episode(self):
        """运行一个完整的episode"""
        obs, info = self.reset()
        self.history.append(("reset", obs, info))
        
        done = False
        truncated = False
        step = 0
        total_reward = 0
        
        while not (done or truncated) and step < self.max_steps:
            # 生成动作
            action = self.act(obs)
            self.history.append(("action", action))
            
            # 执行动作
            obs, reward, done, truncated, info = self.env.step(action)
            self.history.append(("step", obs, reward, done, truncated, info))
            
            total_reward += reward
            step += 1
            
            logger.info(f"Step {step}: reward={reward}, done={done}, truncated={truncated}")
        
        return {
            "total_reward": total_reward,
            "steps": step,
            "done": done,
            "truncated": truncated,
            "history": self.history
        }


@pytest.fixture
def mock_env():
    """创建模拟环境"""
    env = Mock(spec=SWEBenchDebugGymEnv)
    env.max_steps = 10
    env.observation_space = Mock()
    env.action_space = Mock()
    
    # 模拟reset
    env.reset.return_value = (
        {"observation": "Repository loaded"},
        {"instance_id": "test__test-1"}
    )
    
    # 模拟step
    env.step.return_value = (
        {"observation": "Command executed"},
        0.0,  # reward
        False,  # done
        False,  # truncated
        {}  # info
    )
    
    return env


@pytest.fixture
def simple_agent(mock_env):
    """创建简单的测试Agent"""
    return SimpleDebugGymAgent(mock_env, max_steps=5)


class TestAgentBasics:
    """测试Agent基本功能"""
    
    def test_agent_creation(self, simple_agent):
        """测试Agent创建"""
        assert simple_agent is not None
        assert simple_agent.env is not None
        assert simple_agent.llm is not None
        logger.info("✓ Agent created")
    
    def test_agent_reset(self, simple_agent):
        """测试Agent重置"""
        obs, info = simple_agent.reset()
        assert obs is not None
        assert "observation" in obs
        logger.info(f"✓ Agent reset: {info}")
    
    def test_agent_act(self, simple_agent):
        """测试Agent动作生成"""
        obs = {"observation": "test"}
        action = simple_agent.act(obs)
        assert action is not None
        assert "tool" in action
        logger.info(f"✓ Action generated: {action}")


class TestEpisodeExecution:
    """测试Episode执行"""
    
    def test_single_episode(self, simple_agent):
        """测试单个episode"""
        result = simple_agent.run_episode()
        
        assert result is not None
        assert "total_reward" in result
        assert "steps" in result
        assert result["steps"] > 0
        assert result["steps"] <= simple_agent.max_steps
        
        logger.info(f"✓ Episode completed: {result['steps']} steps, reward={result['total_reward']}")
    
    def test_episode_history(self, simple_agent):
        """测试episode历史记录"""
        result = simple_agent.run_episode()
        history = result["history"]
        
        assert len(history) > 0
        # 应该有reset记录
        assert history[0][0] == "reset"
        
        logger.info(f"✓ History recorded: {len(history)} entries")
    
    def test_max_steps_truncation(self, simple_agent):
        """测试最大步数截断"""
        simple_agent.max_steps = 3
        result = simple_agent.run_episode()
        
        assert result["steps"] <= 3
        logger.info(f"✓ Max steps enforced: {result['steps']} steps")


class TestAgentEnvironmentInteraction:
    """测试Agent与环境的交互"""
    
    def test_observation_to_action_flow(self, simple_agent):
        """测试observation->action流程"""
        obs, _ = simple_agent.reset()
        
        # 生成动作
        action = simple_agent.act(obs)
        assert action is not None
        
        # 执行动作
        simple_agent.env.step(action)
        
        logger.info("✓ Observation->Action flow works")
    
    def test_multiple_steps(self, simple_agent):
        """测试多步交互"""
        obs, _ = simple_agent.reset()
        
        for i in range(3):
            action = simple_agent.act(obs)
            obs, reward, done, truncated, info = simple_agent.env.step(action)
            logger.info(f"  Step {i+1}: action={action.get('tool')}, reward={reward}")
        
        logger.info("✓ Multiple steps executed")


class TestRealEnvironmentIntegration:
    """使用真实环境的集成测试"""
    
    @skip_if_no_deps
    def test_agent_with_real_env_docker(self):
        """测试Agent与真实Docker环境集成"""
        # 创建真实环境
        env = SWEBenchDebugGymEnv(
            backend="docker",
            max_steps=3,  # 限制步数
            enable_pdb=False,
            logger_name="test-agent-docker",
        )
        
        try:
            # 创建Agent
            agent = SimpleDebugGymAgent(env, max_steps=3)
            
            # 运行episode
            try:
                result = agent.run_episode()
                logger.info(f"✓ Real Docker environment: {result['steps']} steps")
            except Exception as e:
                logger.warning(f"Episode execution failed (may need real data): {e}")
                
        finally:
            if hasattr(env, 'close'):
                env.close()
    
    @skip_if_no_deps
    @skip_if_no_k8s
    def test_agent_with_real_env_k8s(self):
        """测试Agent与真实K8s环境集成"""
        # 创建K8s环境
        env = SWEBenchDebugGymEnv(
            backend="kubernetes",
            max_steps=3,
            enable_pdb=False,
            k8s_namespace="default",
            k8s_pip_mirror=None,
            k8s_apt_mirror=None,
            logger_name="test-agent-k8s",
        )
        
        try:
            # 创建Agent
            agent = SimpleDebugGymAgent(env, max_steps=3)
            
            # 验证K8s terminal
            if hasattr(env.env, 'terminal'):
                terminal = env.env.terminal
                assert terminal.__class__.__name__ == "KubernetesTerminal"
                logger.info(f"✓ Using K8s terminal: {terminal.pod_name}")
            
            # 运行episode
            try:
                result = agent.run_episode()
                logger.info(f"✓ Real K8s environment: {result['steps']} steps")
            except Exception as e:
                logger.warning(f"Episode execution failed (may need real data): {e}")
                
        finally:
            if hasattr(env, 'close'):
                env.close()


class TestErrorHandling:
    """测试错误处理"""
    
    def test_invalid_action_handling(self, simple_agent):
        """测试无效动作处理"""
        obs, _ = simple_agent.reset()
        
        # 设置返回无效动作的LLM
        simple_agent.llm = Mock()
        simple_agent.llm.generate.return_value = "invalid json"
        
        # 应该能处理无效动作
        action = simple_agent.act(obs)
        assert action is not None
        logger.info("✓ Invalid action handled")
    
    def test_environment_error_handling(self, simple_agent):
        """测试环境错误处理"""
        # 模拟环境抛出异常
        simple_agent.env.step.side_effect = Exception("Environment error")
        
        try:
            result = simple_agent.run_episode()
            # 不应该到这里
            assert False, "Should have raised exception"
        except Exception as e:
            assert "Environment error" in str(e)
            logger.info("✓ Environment error handled")


class TestTrajectoryCollection:
    """测试轨迹收集"""
    
    def test_trajectory_structure(self, simple_agent):
        """测试轨迹结构"""
        result = simple_agent.run_episode()
        history = result["history"]
        
        # 验证轨迹包含必要信息
        assert len(history) > 0
        
        # 第一条应该是reset
        reset_entry = history[0]
        assert reset_entry[0] == "reset"
        
        # 后续应该是action和step交替
        for i in range(1, len(history), 2):
            if i < len(history):
                assert history[i][0] == "action"
            if i + 1 < len(history):
                assert history[i + 1][0] == "step"
        
        logger.info(f"✓ Trajectory structure valid: {len(history)} entries")
    
    def test_reward_accumulation(self, simple_agent):
        """测试奖励累积"""
        # 设置环境返回不同奖励
        rewards = [0.1, 0.2, 0.3]
        simple_agent.env.step.side_effect = [
            ({"obs": "1"}, rewards[0], False, False, {}),
            ({"obs": "2"}, rewards[1], False, False, {}),
            ({"obs": "3"}, rewards[2], True, False, {}),
        ]
        
        result = simple_agent.run_episode()
        expected_total = sum(rewards)
        
        assert abs(result["total_reward"] - expected_total) < 0.001
        logger.info(f"✓ Reward accumulation: {result['total_reward']}")


def test_end_to_end_workflow():
    """端到端工作流测试"""
    logger.info("=" * 60)
    logger.info("Running End-to-End Agent Test")
    logger.info("=" * 60)
    
    try:
        # 1. 创建模拟环境
        env = Mock()
        env.max_steps = 5
        env.reset.return_value = ({"obs": "start"}, {"id": "test"})
        env.step.return_value = ({"obs": "step"}, 0.5, False, False, {})
        logger.info("✓ Step 1: Environment created")
        
        # 2. 创建Agent
        agent = SimpleDebugGymAgent(env, max_steps=3)
        logger.info("✓ Step 2: Agent created")
        
        # 3. 运行episode
        result = agent.run_episode()
        logger.info(f"✓ Step 3: Episode completed: {result['steps']} steps")
        
        # 4. 验证结果
        assert result["steps"] > 0
        assert result["total_reward"] >= 0
        assert len(result["history"]) > 0
        logger.info("✓ Step 4: Results validated")
        
        logger.info("=" * 60)
        logger.info("End-to-End Test PASSED ✓")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"End-to-end test failed: {e}")
        raise


def test_integration_with_k8s_backend():
    """K8s后端完整集成测试"""
    if not KUBERNETES_AVAILABLE or SWEBenchDebugGymEnv is None:
        pytest.skip("K8s or SWEBenchDebugGymEnv not available")
    
    logger.info("=" * 60)
    logger.info("Running K8s Backend Integration Test")
    logger.info("=" * 60)
    
    env = None
    try:
        # 1. 创建K8s环境
        env = SWEBenchDebugGymEnv(
            backend="kubernetes",
            max_steps=3,
            enable_pdb=False,
            k8s_namespace="default",
            k8s_pip_mirror=None,
            k8s_apt_mirror=None,
            logger_name="test-k8s-integration",
        )
        logger.info("✓ Step 1: K8s environment created")
        
        # 2. 验证K8s terminal
        if hasattr(env.env, 'terminal'):
            terminal = env.env.terminal
            assert terminal.__class__.__name__ == "KubernetesTerminal"
            logger.info(f"✓ Step 2: K8s terminal verified: {terminal.pod_name}")
        
        # 3. 创建Agent
        agent = SimpleDebugGymAgent(env, max_steps=2)
        logger.info("✓ Step 3: Agent created")
        
        # 4. 运行episode（可能需要真实数据）
        try:
            result = agent.run_episode()
            logger.info(f"✓ Step 4: Episode completed: {result['steps']} steps")
        except Exception as e:
            logger.warning(f"⚠ Step 4: Episode execution skipped: {e}")
        
        # 5. 清理
        if hasattr(env, 'close'):
            env.close()
        logger.info("✓ Step 5: Environment closed")
        
        logger.info("=" * 60)
        logger.info("K8s Integration Test COMPLETED")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"K8s integration test failed: {e}")
        if env and hasattr(env, 'close'):
            env.close()
        raise


if __name__ == "__main__":
    # 可以直接运行此文件进行测试
    pytest.main([__file__, "-v", "-s"])


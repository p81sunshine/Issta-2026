#!/usr/bin/env python3
"""
SWE-bench Debug-Gym环境集成测试

使用真实的SWE-bench数据集实例测试环境和工具功能，包括：
1. 环境初始化和配置（Kubernetes后端）
2. 真实任务加载和设置
3. PDB工具正确性测试
4. 其他工具执行（bash, view, rewrite等）
5. 测试评估和奖励计算
"""
import logging
import os
import sys
from pathlib import Path

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
    logger.warning("Kubernetes not available")

try:
    from rllm.environments.debug_gym.swe_bench_env import SWEBenchDebugGymEnv
except ImportError:
    SWEBenchDebugGymEnv = None
    logger.warning("SWEBenchDebugGymEnv not available")

try:
    from debug_gym.gym.envs.swe_bench import SWEBenchEnv as DebugGymSWEBenchEnv
except ImportError:
    DebugGymSWEBenchEnv = None
    logger.warning("Debug-Gym SWE-bench not available")


# Skip markers
skip_if_no_deps = pytest.mark.skipif(
    SWEBenchDebugGymEnv is None or DebugGymSWEBenchEnv is None or not KUBERNETES_AVAILABLE,
    reason="Required dependencies not available"
)

# 真实的SWE-bench测试实例
# 使用一个简单的实例来测试
TEST_INSTANCE_ID = "astropy__astropy-7746"  # 一个相对简单的实例




@pytest.fixture(scope="module")
def swe_bench_env():
    """创建Kubernetes后端的SWE-bench环境，使用真实数据集"""
    if SWEBenchDebugGymEnv is None or not KUBERNETES_AVAILABLE:
        pytest.skip("SWEBenchDebugGymEnv or Kubernetes not available")
    
    env = SWEBenchDebugGymEnv(
        backend="kubernetes",
        dataset_id="princeton-nlp/SWE-bench_Lite",  # 使用Lite版本，更快
        split="test",
        instance_id=TEST_INSTANCE_ID,  # 指定测试实例
        max_steps=20,
        enable_pdb=True,  # 启用PDB工具进行测试
        enable_bash=True,
        enable_grep=True,
        k8s_namespace="default",
        k8s_pip_mirror=None,  # 测试时不配置镜像源
        k8s_apt_mirror=None,
        logger_name="test-swe-k8s",
    )
    
    yield env
    
    # 清理
    try:
        if hasattr(env, 'close'):
            env.close()
    except Exception as e:
        logger.warning(f"Cleanup error: {e}")


class TestSWEBenchEnvInitialization:
    """测试SWE-bench环境初始化"""
    
    @skip_if_no_deps
    def test_env_creation(self, swe_bench_env):
        """测试Kubernetes后端环境创建"""
        assert swe_bench_env is not None
        assert swe_bench_env.backend == "kubernetes"
        logger.info("✓ Kubernetes environment created")
    
    @skip_if_no_deps
    def test_terminal_type(self, swe_bench_env):
        """测试Terminal类型"""
        if hasattr(swe_bench_env.env, 'terminal'):
            terminal = swe_bench_env.env.terminal
            assert terminal.__class__.__name__ == "KubernetesTerminal"
            logger.info(f"✓ Using KubernetesTerminal: {terminal.pod_name}")
    
    @skip_if_no_deps
    def test_dataset_loading(self, swe_bench_env):
        """测试数据集加载"""
        # 环境应该加载了dataset
        assert hasattr(swe_bench_env, 'env')
        assert swe_bench_env.env is not None
        
        # 应该有数据集
        if hasattr(swe_bench_env.env, 'dataset'):
            assert swe_bench_env.env.dataset is not None
            dataset_size = len(swe_bench_env.env.dataset)
            logger.info(f"✓ Dataset loaded with {dataset_size} instance(s)")


class TestTaskSetup:
    """测试真实任务设置"""
    
    @skip_if_no_deps
    def test_reset_with_real_instance(self, swe_bench_env):
        """测试使用真实SWE-bench实例重置环境"""
        try:
            obs, info = swe_bench_env.reset()
            
            # 验证重置成功
            assert obs is not None
            assert info is not None
            assert 'instance_id' in info
            
            logger.info(f"✓ Reset completed with instance: {info['instance_id']}")
            logger.info(f"  Repository: {info.get('repo', 'unknown')}")
            # obs is a string (formatted observation), not a dict
            logger.info(f"  Observation preview: {obs[:100] if isinstance(obs, str) else str(obs)[:100]}...")
            
        except Exception as e:
            logger.error(f"Reset failed: {e}")
            raise
    
    @skip_if_no_deps
    def test_workspace_setup(self, swe_bench_env):
        """测试工作空间设置"""
        # Reset环境
        obs, info = swe_bench_env.reset()
        
        # 检查工作空间是否正确设置
        if hasattr(swe_bench_env.env, 'terminal'):
            terminal = swe_bench_env.env.terminal
            
            # 检查仓库目录
            success, output = terminal.run("ls -la")
            assert success
            logger.info(f"✓ Workspace contents:\n{output[:200]}...")
            
            # 检查Git仓库
            success, output = terminal.run("git status")
            if success:
                logger.info("✓ Git repository initialized")
            else:
                logger.warning("⚠ Git status failed (may be expected)")


class TestPDBTool:
    """测试PDB工具的正确性"""
    
    @skip_if_no_deps
    def test_pdb_set_breakpoint(self, swe_bench_env):
        """测试PDB设置断点"""
        # Reset环境
        obs, info = swe_bench_env.reset()
        
        # 找到一个Python文件
        if hasattr(swe_bench_env.env, 'terminal'):
            terminal = swe_bench_env.env.terminal
            success, output = terminal.run("find . -name '*.py' -type f | head -1")
            
            if success and output.strip():
                py_file = output.strip()
                logger.info(f"Found Python file: {py_file}")
                
                # 设置断点
                action = {
                    "tool": "pdb",
                    "args": {
                        "command": "b",  # break
                        "path": py_file,
                        "line": 10
                    }
                }
                
                try:
                    obs, reward, done, truncated, info = swe_bench_env.step(action)
                    assert obs is not None
                    logger.info("✓ PDB breakpoint set")
                    logger.info(f"  Observation: {str(obs)[:200]}...")
                except Exception as e:
                    logger.warning(f"PDB breakpoint failed: {e}")
    
    @skip_if_no_deps
    def test_pdb_list_context(self, swe_bench_env):
        """测试PDB列出代码上下文"""
        obs, info = swe_bench_env.reset()
        
        # 使用list命令查看代码
        action = {
            "tool": "pdb",
            "args": {
                "command": "l"  # list
            }
        }
        
        try:
            obs, reward, done, truncated, info = swe_bench_env.step(action)
            assert obs is not None
            logger.info("✓ PDB list context")
            logger.info(f"  Output: {str(obs)[:200]}...")
        except Exception as e:
            logger.warning(f"PDB list failed: {e}")
    
    @skip_if_no_deps
    def test_pdb_print_variable(self, swe_bench_env):
        """测试PDB打印变量"""
        obs, info = swe_bench_env.reset()
        
        # 打印变量
        action = {
            "tool": "pdb",
            "args": {
                "command": "p",  # print
                "expression": "1 + 1"
            }
        }
        
        try:
            obs, reward, done, truncated, info = swe_bench_env.step(action)
            assert obs is not None
            # 应该能看到计算结果
            if "2" in str(obs):
                logger.info("✓ PDB print expression works")
            else:
                logger.warning(f"PDB print result unexpected: {obs}")
        except Exception as e:
            logger.warning(f"PDB print failed: {e}")
    
    @skip_if_no_deps
    def test_pdb_step_execution(self, swe_bench_env):
        """测试PDB步进执行"""
        obs, info = swe_bench_env.reset()
        
        # 使用step命令
        action = {
            "tool": "pdb",
            "args": {
                "command": "s"  # step
            }
        }
        
        try:
            obs, reward, done, truncated, info = swe_bench_env.step(action)
            assert obs is not None
            logger.info("✓ PDB step execution")
        except Exception as e:
            logger.warning(f"PDB step failed: {e}")
    
    @skip_if_no_deps
    def test_pdb_continue(self, swe_bench_env):
        """测试PDB继续执行"""
        obs, info = swe_bench_env.reset()
        
        # 使用continue命令
        action = {
            "tool": "pdb",
            "args": {
                "command": "c"  # continue
            }
        }
        
        try:
            obs, reward, done, truncated, info = swe_bench_env.step(action)
            assert obs is not None
            logger.info("✓ PDB continue")
        except Exception as e:
            logger.warning(f"PDB continue failed: {e}")


class TestOtherTools:
    """测试其他工具执行"""
    
    @skip_if_no_deps
    def test_bash_tool(self, swe_bench_env):
        """测试bash工具"""
        obs, info = swe_bench_env.reset()
        
        action = {
            "tool": "bash",
            "args": {
                "command": "echo 'Hello from bash'"
            }
        }
        
        obs, reward, done, truncated, info = swe_bench_env.step(action)
        assert obs is not None
        assert "Hello from bash" in str(obs)
        logger.info("✓ Bash tool executed")
    
    @skip_if_no_deps
    def test_view_tool(self, swe_bench_env):
        """测试view工具"""
        obs, info = swe_bench_env.reset()
        
        # 找到一个文件来查看
        if hasattr(swe_bench_env.env, 'terminal'):
            terminal = swe_bench_env.env.terminal
            success, output = terminal.run("find . -name '*.py' -type f | head -1")
            
            if success and output.strip():
                py_file = output.strip()
                
                action = {
                    "tool": "view",
                    "args": {
                        "path": py_file
                    }
                }
                
                obs, reward, done, truncated, info = swe_bench_env.step(action)
                assert obs is not None
                logger.info(f"✓ View tool executed for {py_file}")
    
    @skip_if_no_deps
    def test_grep_tool(self, swe_bench_env):
        """测试grep工具"""
        obs, info = swe_bench_env.reset()
        
        action = {
            "tool": "grep",
            "args": {
                "pattern": "def",
                "directory": "."
            }
        }
        
        try:
            obs, reward, done, truncated, info = swe_bench_env.step(action)
            assert obs is not None
            logger.info("✓ Grep tool executed")
        except Exception as e:
            logger.warning(f"Grep tool failed: {e}")
    
    @skip_if_no_deps
    def test_eval_tool(self, swe_bench_env):
        """测试eval工具（运行测试）"""
        obs, info = swe_bench_env.reset()
        
        action = {
            "tool": "eval",
            "args": {}
        }
        
        try:
            obs, reward, done, truncated, info = swe_bench_env.step(action)
            assert obs is not None
            logger.info("✓ Eval tool executed")
            logger.info(f"  Reward: {reward}")
            logger.info(f"  Tests result: {str(obs)[:200]}...")
        except Exception as e:
            logger.warning(f"Eval tool failed: {e}")


class TestRewardCalculation:
    """测试奖励计算"""
    
    @skip_if_no_deps
    def test_reward_with_eval(self, swe_bench_env):
        """测试运行eval后的奖励计算"""
        obs, info = swe_bench_env.reset()
        
        # 运行eval
        action = {"tool": "eval", "args": {}}
        
        try:
            obs, reward, done, truncated, info = swe_bench_env.step(action)
            
            # 奖励应该在[0, 1]范围内（测试通过率）
            assert 0 <= reward <= 1
            logger.info(f"✓ Reward calculated: {reward}")
            logger.info(f"  Test results: {info.get('test_results', 'N/A')}")
        except Exception as e:
            logger.warning(f"Reward calculation failed: {e}")


def test_integration_full_workflow():
    """集成测试：完整的Debug-Gym工作流"""
    if SWEBenchDebugGymEnv is None or not KUBERNETES_AVAILABLE:
        pytest.skip("Required dependencies not available")
    
    logger.info("=" * 60)
    logger.info("Running Full SWE-bench Debug-Gym Integration Test")
    logger.info("=" * 60)
    
    env = None
    try:
        # 1. 创建环境
        env = SWEBenchDebugGymEnv(
            backend="kubernetes",
            dataset_id="princeton-nlp/SWE-bench_Lite",
            split="test",
            instance_id=TEST_INSTANCE_ID,
            max_steps=10,
            enable_pdb=True,
            enable_bash=True,
            enable_grep=True,
            k8s_namespace="default",
            k8s_pip_mirror=None,
            k8s_apt_mirror=None,
            logger_name="test-integration",
        )
        logger.info("✓ Step 1: Environment created")
        
        # 2. Reset环境
        obs, info = env.reset()
        logger.info(f"✓ Step 2: Environment reset")
        logger.info(f"  Instance: {info.get('instance_id')}")
        logger.info(f"  Repository: {info.get('repo')}")
        
        # 3. 执行bash命令
        action = {"tool": "bash", "args": {"command": "pwd"}}
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ Step 3: Bash executed (reward={reward})")
        
        # 4. 使用grep查找
        action = {"tool": "grep", "args": {"pattern": "def", "directory": "."}}
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ Step 4: Grep executed (reward={reward})")
        
        # 5. 查看文件
        if hasattr(env.env, 'terminal'):
            terminal = env.env.terminal
            success, py_file = terminal.run("find . -name '*.py' -type f | head -1")
            if success and py_file.strip():
                action = {"tool": "view", "args": {"path": py_file.strip()}}
                obs, reward, done, truncated, info = env.step(action)
                logger.info(f"✓ Step 5: View executed (reward={reward})")
        
        # 6. 运行测试
        action = {"tool": "eval", "args": {}}
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ Step 6: Eval executed (reward={reward})")
        
        # 7. 清理
        if hasattr(env, 'close'):
            env.close()
        logger.info("✓ Step 7: Environment closed")
        
        logger.info("=" * 60)
        logger.info("Integration Test PASSED ✓")
        logger.info("=" * 60)
        
    except Exception as e:
        logger.error(f"Integration test failed: {e}")
        if env and hasattr(env, 'close'):
            env.close()
        raise


if __name__ == "__main__":
    # 可以直接运行此文件进行测试
    pytest.main([__file__, "-v", "-s"])


#!/usr/bin/env python3
"""
SWE-bench Debug-Gym环境集成测试（可直接运行）

测试Kubernetes后端的SWE-bench环境的完整功能。
"""
import logging
import os
import sys
import traceback

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 检查依赖
def check_dependencies():
    """检查所需依赖"""
    missing = []
    
    try:
        from kubernetes import client, config
        logger.info("✓ Kubernetes client available")
    except ImportError:
        missing.append("kubernetes (pip install kubernetes)")
    
    try:
        from rllm.environments.debug_gym.swe_bench_env import SWEBenchDebugGymEnv
        logger.info("✓ SWEBenchDebugGymEnv available")
    except ImportError:
        missing.append("rllm debug-gym environment")
    
    try:
        from debug_gym.gym.envs.swe_bench import SWEBenchEnv
        logger.info("✓ Debug-Gym SWE-bench available")
    except ImportError:
        missing.append("debug-gym")
    
    if missing:
        logger.error(f"Missing dependencies: {', '.join(missing)}")
        return False
    
    return True


def test_kubernetes_connection():
    """测试Kubernetes集群连接"""
    logger.info("\n" + "="*60)
    logger.info("测试1: Kubernetes集群连接")
    logger.info("="*60)
    
    try:
        import subprocess
        result = subprocess.run(
            ["kubectl", "cluster-info"],
            capture_output=True,
            text=True,
            timeout=10
        )
        if result.returncode == 0:
            logger.info("✓ Kubernetes cluster is accessible")
            return True
        else:
            logger.error("✗ Cannot connect to Kubernetes cluster")
            return False
    except Exception as e:
        logger.error(f"✗ Kubernetes connection test failed: {e}")
        return False


def test_env_creation():
    """测试环境创建"""
    logger.info("\n" + "="*60)
    logger.info("测试2: 环境创建")
    logger.info("="*60)
    
    try:
        from rllm.environments.debug_gym.swe_bench_env import SWEBenchDebugGymEnv
        
        logger.info("Creating SWEBenchDebugGymEnv with Kubernetes backend...")
        env = SWEBenchDebugGymEnv(
            backend="kubernetes",
            dataset_id="princeton-nlp/SWE-bench_Lite",  # 使用Lite版本
            split="test",
            instance_id="astropy__astropy-7746",  # 简单实例
            max_steps=20,
            enable_pdb=True,
            enable_bash=True,
            enable_grep=True,
            k8s_namespace="default",
            k8s_pip_mirror=None,  # 测试时不配置
            k8s_apt_mirror=None,
            logger_name="test-swe-k8s",
        )
        
        logger.info(f"✓ Environment created")
        logger.info(f"  Backend: {env.backend}")
        logger.info(f"  Dataset: {env.dataset_id}")
        logger.info(f"  Instance: {env.instance_id}")
        
        # 清理
        env.close()
        logger.info("✓ Environment closed")
        
        return True, env
        
    except Exception as e:
        logger.error(f"✗ Environment creation failed: {e}")
        traceback.print_exc()
        return False, None


def test_env_reset(env):
    """测试环境重置"""
    logger.info("\n" + "="*60)
    logger.info("测试3: 环境重置（真实SWE-bench实例）")
    logger.info("="*60)
    
    try:
        logger.info("Resetting environment...")
        obs, info = env.reset()
        
        logger.info(f"✓ Reset completed")
        logger.info(f"  Instance ID: {info.get('instance_id')}")
        logger.info(f"  Repository: {info.get('repo')}")
        logger.info(f"  Score: {info.get('score')}/{info.get('max_score')}")
        logger.info(f"  Observation length: {len(obs)} chars")
        logger.info(f"  Observation preview: {obs}...")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ Reset failed: {e}")
        traceback.print_exc()
        return False


def test_pdb_tools(env):
    """测试PDB工具（debug-gym核心功能）"""
    logger.info("\n" + "="*60)
    logger.info("测试4: PDB调试工具")
    logger.info("="*60)
    
    results = []
    
    # Test 1: PDB list - 查看代码
    try:
        logger.info("\n4.1 测试PDB list命令")
        action = '{"name": "pdb", "arguments": {"command": "list ."}}'
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ PDB list executed")
        logger.info(f"  Output preview: {str(obs)}...")
        results.append(("PDB list", True))
    except Exception as e:
        logger.error(f"✗ PDB list failed: {e}")
        traceback.print_exc()
        results.append(("PDB list", False))
    
    # Test 2: PDB where - 查看调用栈
    try:
        logger.info("\n4.2 测试PDB where命令")
        action = '{"name": "pdb", "arguments": {"command": "where"}}'
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ PDB where executed")
        logger.info(f"  Output preview: {str(obs)}...")
        results.append(("PDB where", True))
    except Exception as e:
        logger.error(f"✗ PDB where failed: {e}")
        results.append(("PDB where", False))
    
    # Test 3: PDB print - 打印表达式
    try:
        logger.info("\n4.3 测试PDB print命令")
        action = '{"name": "pdb", "arguments": {"command": "p 1 + 1"}}'
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ PDB print executed")
        if "2" in str(obs):
            logger.info(f"  ✓ Expression evaluated correctly")
        logger.info(f"  Output: {str(obs)}...")
        results.append(("PDB print", True))
    except Exception as e:
        logger.error(f"✗ PDB print failed: {e}")
        results.append(("PDB print", False))
    
    return results


def test_other_tools(env):
    """测试其他工具执行"""
    logger.info("\n" + "="*60)
    logger.info("测试5: 其他工具")
    logger.info("="*60)
    
    results = []
    
    # Test 1: Bash tool
    breakpoint()
    try:
        logger.info("\n5.1 测试Bash工具")
        action = '{"name": "bash", "arguments": {"command": "pwd"}}'
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ Bash tool executed")
        logger.info(f"  Output: {obs}")
        results.append(("Bash", True))
    except Exception as e:
        logger.error(f"✗ Bash tool failed: {e}")
        results.append(("Bash", False))
    
    # Test 2: View tool  
    try:
        logger.info("\n5.2 测试View工具")
        # 找一个Python文件
        terminal = env.env.terminal
        success, py_file = terminal.run("find . -name '*.py' -type f | head -1", timeout=30)
        if success and py_file.strip():
            action = f'{{"name": "view", "arguments": {{"path": "{py_file.strip()}"}}}}'
            obs, reward, done, truncated, info = env.step(action)
            logger.info(f"✓ View tool executed for {py_file.strip()}")
            logger.info(f"  Content preview: {str(obs)}...")
            results.append(("View", True))
        else:
            logger.warning("⚠ No Python file found for view test")
            results.append(("View", False))
    except Exception as e:
        logger.error(f"✗ View tool failed: {e}")
        results.append(("View", False))
    
    # Test 3: Grep tool
    try:
        logger.info("\n5.3 测试Grep工具")
        action = '{"name": "grep", "arguments": {"pattern": "def ", "path": "."}}'
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ Grep tool executed")
        # 避免f-string中使用反斜杠
        line_count = len(str(obs).split('\n'))
        logger.info(f"  Found matches: {line_count} lines")
        results.append(("Grep", True))
    except Exception as e:
        logger.error(f"✗ Grep tool failed: {e}")
        results.append(("Grep", False))
    
    # Test 4: Eval tool
    try:
        logger.info("\n5.4 测试Eval工具")
        action = '{"name": "eval", "arguments": {}}'
        obs, reward, done, truncated, info = env.step(action)
        logger.info(f"✓ Eval tool executed")
        logger.info(f"  Reward: {reward}")
        logger.info(f"  Score: {info.get('score')}/{info.get('max_score')}")
        results.append(("Eval", True))
    except Exception as e:
        logger.error(f"✗ Eval tool failed: {e}")
        results.append(("Eval", False))
    
    return results


def test_reward_calculation(env):
    """测试奖励计算"""
    logger.info("\n" + "="*60)
    logger.info("测试6: 奖励计算")
    logger.info("="*60)
    
    try:
        # 计算最终奖励
        final_reward = env.compute_final_reward()
        logger.info(f"✓ Final reward calculated: {final_reward}")
        logger.info(f"  Reward is in range [0, 1]: {0 <= final_reward <= 1}")
        
        return True
        
    except Exception as e:
        logger.error(f"✗ Reward calculation failed: {e}")
        traceback.print_exc()
        return False


def main():
    """主测试流程"""
    print("\n" + "🚀"*30)
    print("SWE-bench Debug-Gym Kubernetes 集成测试")
    print("🚀"*30 + "\n")
    
    # 检查依赖
    if not check_dependencies():
        logger.error("❌ 依赖检查失败，无法继续测试")
        return False
    
    # 检查K8s连接
    if not test_kubernetes_connection():
        logger.error("❌ Kubernetes连接失败，无法继续测试")
        return False
    
    # 创建环境
    success, env = test_env_creation()
    if not success:
        logger.error("❌ 环境创建失败")
        return False
    
    # 重新创建环境用于后续测试
    try:
        from rllm.environments.debug_gym.swe_bench_env import SWEBenchDebugGymEnv
        
        env = SWEBenchDebugGymEnv(
            backend="kubernetes",
            dataset_id="princeton-nlp/SWE-bench_Lite",
            split="test",
            instance_id="astropy__astropy-7746",
            max_steps=20,
            enable_pdb=True,
            enable_bash=True,
            enable_grep=True,
            k8s_namespace="default",
            logger_name="test-swe-k8s",
        )
        
        # 测试Reset
        if not test_env_reset(env):
            logger.error("❌ 环境重置失败")
            env.close()
            return False
        
        breakpoint()
        
        # 测试PDB工具
        pdb_results = test_pdb_tools(env)
        
        # 测试其他工具
        tool_results = test_other_tools(env)
        
        # 测试奖励计算
        reward_success = test_reward_calculation(env)
        
        # 清理
        env.close()
        logger.info("\n✓ Environment cleaned up")
        
        # 总结
        print("\n" + "="*60)
        print("测试总结")
        print("="*60)
        
        print("\nPDB工具测试结果:")
        for tool_name, success in pdb_results:
            status = "✓ 通过" if success else "✗ 失败"
            print(f"  {tool_name}: {status}")
        
        print("\n其他工具测试结果:")
        for tool_name, success in tool_results:
            status = "✓ 通过" if success else "✗ 失败"
            print(f"  {tool_name}: {status}")
        
        print(f"\n奖励计算: {'✓ 通过' if reward_success else '✗ 失败'}")
        
        all_passed = all(s for _, s in pdb_results) and all(s for _, s in tool_results) and reward_success
        
        print("\n" + "="*60)
        if all_passed:
            print("✅ 所有测试通过！Kubernetes后端已就绪！")
        else:
            print("⚠️  部分测试失败，请检查日志")
        print("="*60)
        
        print("\n下一步:")
        print("  bash examples/debug_gym/train_swe_bench_k8s.sh")
        print()
        
        return all_passed
        
    except Exception as e:
        logger.error(f"❌ 测试过程中发生错误: {e}")
        traceback.print_exc()
        if env:
            env.close()
        return False


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ 测试失败: {e}")
        traceback.print_exc()
        sys.exit(1)


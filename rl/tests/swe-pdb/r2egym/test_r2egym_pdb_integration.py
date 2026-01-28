#!/usr/bin/env python3
"""
R2E-Gym PDB 工具集成测试（可直接运行）

测试 R2E-Gym 框架中 PDB 工具的完整功能，包括：
- r2egym-debug 和 r2egym-debug-withtest agents
- PDB 会话管理和断点持久化
- 与其他工具的协同工作
- Kubernetes 后端支持
"""
import json
import logging
import os
import sys
import time
import traceback

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def check_dependencies():
    """检查所需依赖"""
    logger.info("\n" + "=" * 60)
    logger.info("检查依赖")
    logger.info("=" * 60)
    
    missing = []
    
    # 检查 Kubernetes
    try:
        from kubernetes import client, config
        logger.info("✓ Kubernetes client available")
    except ImportError:
        missing.append("kubernetes (pip install kubernetes)")
    
    # 检查 R2E-Gym
    try:
        import r2egym
        from r2egym.agenthub.environment.env import RepoEnv
        from r2egym.agenthub.action import Action
        logger.info("✓ R2E-Gym available")
    except ImportError:
        missing.append("r2egym")
    
    # 检查 rllm
    try:
        from rllm.environments.swe.swe import SWEEnv
        from rllm.agents.swe_agent import SWEAgent
        logger.info("✓ rllm SWE framework available")
    except ImportError:
        missing.append("rllm")
    
    # 检查 swebench (用于数据集加载)
    try:
        from datasets import load_dataset
        # 尝试访问 SWE-bench 数据集以验证
        logger.info("✓ SWE-bench datasets available")
    except ImportError:
        missing.append("datasets (pip install datasets)")
    
    if missing:
        logger.error(f"✗ Missing dependencies: {', '.join(missing)}")
        return False
    
    logger.info("\n✓ All dependencies available")
    return True


def test_kubernetes_connection():
    """测试 Kubernetes 集群连接"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 1: Kubernetes 集群连接")
    logger.info("=" * 60)
    
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
            logger.info(f"  Cluster info: {result.stdout.split(chr(10))[0]}")
            return True
        else:
            logger.error(f"✗ Cannot connect to Kubernetes cluster")
            logger.error(f"  Error: {result.stderr}")
            return False
    except Exception as e:
        logger.error(f"✗ Kubernetes connection test failed: {e}")
        return False


def test_system_prompts():
    """测试系统提示是否正确加载"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 2: 系统提示加载")
    logger.info("=" * 60)
    
    try:
        from rllm.agents.system_prompts import (
            SWE_SYSTEM_PROMPT,
            SWE_SYSTEM_PROMPT_DEBUG,
            SWE_SYSTEM_PROMPT_DEBUG_WITHTEST,
        )
        
        # 检查标准提示不包含 PDB
        if "BEGIN FUNCTION #4: pdb" in SWE_SYSTEM_PROMPT:
            logger.error("✗ Standard prompt should not contain PDB tool")
            return False
        
        # 检查 debug 提示包含 PDB
        if "BEGIN FUNCTION #4: pdb" not in SWE_SYSTEM_PROMPT_DEBUG:
            logger.error("✗ Debug prompt should contain PDB tool")
            return False
        
        if "BEGIN FUNCTION #4: pdb" not in SWE_SYSTEM_PROMPT_DEBUG_WITHTEST:
            logger.error("✗ Debug-withtest prompt should contain PDB tool")
            return False
        
        # 检查两种 debug 提示的区别（现在是初始测试结果）
        has_auto_test = "automatically runs the test suite" in SWE_SYSTEM_PROMPT_DEBUG_WITHTEST
        
        if not has_auto_test:
            logger.warning("⚠ Debug-withtest prompt should mention automatic test execution")
        
        logger.info("✓ System prompts loaded correctly")
        logger.info(f"  Standard prompt: {len(SWE_SYSTEM_PROMPT)} chars")
        logger.info(f"  Debug prompt: {len(SWE_SYSTEM_PROMPT_DEBUG)} chars")
        logger.info(f"  Debug-withtest prompt: {len(SWE_SYSTEM_PROMPT_DEBUG_WITHTEST)} chars")
        logger.info(f"  Debug-withtest has auto-test: {has_auto_test}")
        return True
        
    except Exception as e:
        logger.error(f"✗ System prompt test failed: {e}")
        traceback.print_exc()
        return False


def test_tool_lists():
    """测试工具列表正确分离"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 3: 工具列表分离")
    logger.info("=" * 60)
    
    try:
        from rllm.environments.swe.swe import (
            R2EGYM_COMMAND_FILES,
            R2EGYM_DEBUG_COMMAND_FILES,
        )
        
        # 检查标准工具列表不包含 PDB
        pdb_in_standard = any("pdb.py" in f for f in R2EGYM_COMMAND_FILES)
        if pdb_in_standard:
            logger.error("✗ Standard tool list should not contain pdb.py")
            return False
        
        logger.info(f"✓ Standard tool list ({len(R2EGYM_COMMAND_FILES)} tools):")
        for f in R2EGYM_COMMAND_FILES:
            logger.info(f"    - {os.path.basename(f)}")
        
        # 检查 debug 工具列表包含 PDB
        pdb_in_debug = any("pdb.py" in f for f in R2EGYM_DEBUG_COMMAND_FILES)
        if not pdb_in_debug:
            logger.error("✗ Debug tool list should contain pdb.py")
            return False
        
        logger.info(f"✓ Debug tool list ({len(R2EGYM_DEBUG_COMMAND_FILES)} tools):")
        for f in R2EGYM_DEBUG_COMMAND_FILES:
            logger.info(f"    - {os.path.basename(f)}")
        
        # 检查差异
        if len(R2EGYM_DEBUG_COMMAND_FILES) != len(R2EGYM_COMMAND_FILES) + 1:
            logger.error("✗ Debug tool list should have exactly one more tool (PDB)")
            return False
        
        logger.info("✓ Tool lists correctly separated")
        return True
        
    except Exception as e:
        logger.error(f"✗ Tool list test failed: {e}")
        traceback.print_exc()
        return False


def test_env_creation_standard():
    """测试标准 r2egym 环境创建（不含 PDB）"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 4: 标准环境创建（r2egym，不含 PDB）")
    logger.info("=" * 60)
    
    try:
        from datasets import load_dataset
        from rllm.environments.swe.swe import SWEEnv
        
        # 加载数据集
        dataset = load_dataset("R2E-Gym/SWE-Bench-Lite", split="test")
        
        logger.info("Creating standard SWEEnv (r2egym scaffold)...")
        env = SWEEnv(
            dataset=dataset,
            idx=0,
            scaffold="r2egym",
            backend="kubernetes",
            step_timeout=90,
            reward_timeout=300,
            verbose=False,
        )
        
        logger.info(f"✓ Environment created")
        logger.info(f"  Scaffold: {env.scaffold}")
        logger.info(f"  Backend: {env.backend}")
        logger.info(f"  Instance: {env.entry.get('instance_id')}")
        
        # 不关闭，返回供后续使用
        return True, env
        
    except Exception as e:
        logger.error(f"✗ Standard environment creation failed: {e}")
        traceback.print_exc()
        return False, None


def test_env_creation_debug():
    """测试 debug 环境创建（含 PDB）"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 5: Debug 环境创建（r2egym-debug-withtest，含 PDB）")
    logger.info("=" * 60)
    
    try:
        from datasets import load_dataset
        from rllm.environments.swe.swe import SWEEnv
        
        # 加载数据集
        dataset = load_dataset("R2E-Gym/SWE-Bench-Lite", split="test")
        
        logger.info("Creating debug SWEEnv (r2egym-debug-withtest scaffold)...")
        env = SWEEnv(
            dataset=dataset,
            idx=0,
            scaffold="r2egym-debug-withtest",
            backend="kubernetes",
            step_timeout=90,
            reward_timeout=300,
            verbose=False,
        )
        
        logger.info(f"✓ Environment created")
        logger.info(f"  Scaffold: {env.scaffold}")
        logger.info(f"  Backend: {env.backend}")
        logger.info(f"  Instance: {env.entry.get('instance_id')}")
        
        return True, env
        
    except Exception as e:
        logger.error(f"✗ Debug environment creation failed: {e}")
        traceback.print_exc()
        return False, None


def test_env_reset(env, env_name="Environment"):
    """测试环境重置"""
    logger.info("\n" + "=" * 60)
    logger.info(f"测试 6: {env_name} 重置")
    logger.info("=" * 60)
    
    try:
        logger.info("Resetting environment...")
        obs, info = env.reset()
        
        logger.info(f"✓ Reset completed")
        logger.info(f"  Observation length: {len(obs)} chars")
        logger.info(f"  Observation preview: {obs[:200]}...")
        
        # 检查是否包含任务描述
        if "github issue" in obs.lower() or "problem" in obs.lower():
            logger.info("  ✓ Task instruction found")
        
        return True, obs
        
    except Exception as e:
        logger.error(f"✗ Reset failed: {e}")
        traceback.print_exc()
        return False, None


def test_standard_tools(env):
    """测试标准工具（不含 PDB）"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 7: 标准工具（file_editor, search, execute_bash）")
    logger.info("=" * 60)
    
    results = []
    
    # Test 1: file_editor - view
    try:
        logger.info("\n7.1 测试 file_editor view 命令")
        action = '<function=file_editor><parameter=command>view</parameter><parameter=path>/testbed</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ file_editor view executed")
        logger.info(f"  Output preview: {str(obs)[:200]}...")
        results.append(("file_editor view", True))
    except Exception as e:
        logger.error(f"✗ file_editor view failed: {e}")
        traceback.print_exc()
        results.append(("file_editor view", False))
    
    # Test 2: search
    try:
        logger.info("\n7.2 测试 search 命令")
        action = '<function=search><parameter=search_term>def </parameter><parameter=path>.</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ search executed")
        logger.info(f"  Output preview: {str(obs)[:200]}...")
        results.append(("search", True))
    except Exception as e:
        logger.error(f"✗ search failed: {e}")
        traceback.print_exc()
        results.append(("search", False))
    
    # Test 3: execute_bash
    try:
        logger.info("\n7.3 测试 execute_bash 命令")
        action = '<function=execute_bash><parameter=cmd>pwd</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ execute_bash executed")
        logger.info(f"  Output: {str(obs)}")
        if "/testbed" in str(obs):
            logger.info("  ✓ Working directory correct")
        results.append(("execute_bash", True))
    except Exception as e:
        logger.error(f"✗ execute_bash failed: {e}")
        traceback.print_exc()
        results.append(("execute_bash", False))
    
    return results


def test_pdb_tools(env):
    """测试 PDB 工具（核心功能）"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 8: PDB 调试工具")
    logger.info("=" * 60)
    
    results = []
    
    # Test 1: 查找一个 Python 文件用于调试
    breakpoint()
    try:
        logger.info("\n8.1 查找 Python 文件")
        action = '<function=execute_bash><parameter=cmd>find /testbed -name "*.py" -type f | head -5</parameter></function>'
        obs, reward, done, info = env.step(action)
        
        # 提取第一个 .py 文件
        py_files = [line.strip() for line in str(obs).split('\n') if line.strip().endswith('.py')]
        if py_files:
            test_file = py_files[1]
            logger.info(f"✓ Found Python file for testing: {test_file}")
        else:
            logger.warning("⚠ No Python files found, using dummy path")
            test_file = "/testbed/test.py"
        
    except Exception as e:
        logger.error(f"✗ Failed to find Python file: {e}")
        test_file = "/testbed/test.py"
    
    # Test 2: 设置断点（PDB 未启动时）
    try:
        logger.info("\n8.2 测试 PDB 设置断点（未启动）")
        # action = f'<function=pdb><parameter=command>b {test_file}:10</parameter></function>'
        test_file = "/testbed/astropy/time/tests/test_sidereal.py"
        action = f'<function=pdb><parameter=command>b {test_file}:101</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ PDB set breakpoint executed")
        logger.info(f"  Output: {str(obs)[:300]}...")
        
        # 检查断点是否保存
        if "saved" in str(obs).lower() or "breakpoint" in str(obs).lower():
            logger.info("  ✓ Breakpoint saved for later")
        
        results.append(("PDB set breakpoint", True))
    except Exception as e:
        logger.error(f"✗ PDB set breakpoint failed: {e}")
        traceback.print_exc()
        results.append(("PDB set breakpoint", False))
    
    # Test 3: 列出断点
    try:
        logger.info("\n8.3 测试 PDB 列出断点")
        action = '<function=pdb><parameter=command>b</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ PDB list breakpoints executed")
        logger.info(f"  Output: {str(obs)[:300]}...")
        results.append(("PDB list breakpoints", True))
    except Exception as e:
        logger.error(f"✗ PDB list breakpoints failed: {e}")
        traceback.print_exc()
        results.append(("PDB list breakpoints", False))
    
    # Test 4: 启动 PDB（显式提供 entrypoint）
    try:
        logger.info("\n8.4 测试 PDB 启动（显式 entrypoint）")
        # 使用之前找到的 Python 文件作为 entrypoint
        action = f'<function=pdb><parameter=command>start pytest {test_file}</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ PDB start executed")
        logger.info(f"  Output preview: {str(obs)}")
        
        # 检查是否成功启动
        if "PDB started" in str(obs) or "Current context" in str(obs):
            logger.info("  ✓ PDB session started")
        
        results.append(("PDB start", True))
    except Exception as e:
        logger.error(f"✗ PDB start failed: {e}")
        traceback.print_exc()
        results.append(("PDB start", False))
    
    # Test 5: PDB where 命令
    try:
        logger.info("\n8.5 测试 PDB where 命令")
        action = '<function=pdb><parameter=command>where</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ PDB where executed")
        logger.info(f"  Output preview: {str(obs)[:300]}...")
        results.append(("PDB where", True))
    except Exception as e:
        logger.error(f"✗ PDB where failed: {e}")
        traceback.print_exc()
        results.append(("PDB where", False))
    
    # Test 6: PDB print 命令
    try:
        logger.info("\n8.6 测试 PDB print 命令")
        action = '<function=pdb><parameter=command>p 1 + 1</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ PDB print executed")
        logger.info(f"  Output: {str(obs)}")
        
        if "2" in str(obs):
            logger.info("  ✓ Expression evaluated correctly")
        
        results.append(("PDB print", True))
    except Exception as e:
        logger.error(f"✗ PDB print failed: {e}")
        traceback.print_exc()
        results.append(("PDB print", False))
    
    # Test 7: PDB list 命令
    try:
        logger.info("\n8.7 测试 PDB list 命令")
        action = '<function=pdb><parameter=command>l .</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ PDB list executed")
        logger.info(f"  Output preview: {str(obs)[:300]}...")
        results.append(("PDB list", True))
    except Exception as e:
        logger.error(f"✗ PDB list failed: {e}")
        traceback.print_exc()
        results.append(("PDB list", False))
    
    # Test 8: 清除断点
    breakpoint()
    try:
        logger.info("\n8.8 测试 PDB 清除断点")
        action = '<function=pdb><parameter=command>cl</parameter></function>'
        obs, reward, done, info = env.step(action)
        logger.info(f"✓ PDB clear breakpoints executed")
        logger.info(f"  Output: {str(obs)[:200]}...")
        results.append(("PDB clear breakpoints", True))
    except Exception as e:
        logger.error(f"✗ PDB clear breakpoints failed: {e}")
        traceback.print_exc()
        results.append(("PDB clear breakpoints", False))
    
    return results


def test_agent_initialization():
    """测试 Agent 初始化"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 9: Agent 初始化")
    logger.info("=" * 60)
    
    results = []
    
    scaffolds = ["r2egym", "r2egym-debug", "r2egym-debug-withtest"]
    
    try:
        from rllm.agents.swe_agent import SWEAgent
        
        for scaffold in scaffolds:
            logger.info(f"\n  Testing scaffold: {scaffold}")
            agent = SWEAgent(scaffold=scaffold, use_fn_calling=False)
            
            # 检查系统提示
            has_pdb = "BEGIN FUNCTION #4: pdb" in agent.system_prompt
            should_have_pdb = "debug" in scaffold
            
            if has_pdb == should_have_pdb:
                logger.info(f"    ✓ {scaffold} agent initialized correctly")
                logger.info(f"      System prompt length: {len(agent.system_prompt)} chars")
                logger.info(f"      Has PDB tool: {has_pdb}")
                results.append((f"Agent {scaffold}", True))
            else:
                logger.error(f"    ✗ {scaffold} agent has incorrect PDB tool configuration")
                results.append((f"Agent {scaffold}", False))
        
    except Exception as e:
        logger.error(f"✗ Agent initialization failed: {e}")
        traceback.print_exc()
        results.append(("Agent initialization", False))
    
    return results


def test_reward_calculation(env):
    """测试奖励计算"""
    logger.info("\n" + "=" * 60)
    logger.info("测试 10: 奖励计算")
    logger.info("=" * 60)
    
    try:
        # 计算最终奖励
        final_reward = env.compute_final_reward()
        logger.info(f"✓ Final reward calculated: {final_reward}")
        
        # 检查奖励范围
        if 0 <= final_reward <= 1:
            logger.info(f"  ✓ Reward is in valid range [0, 1]")
            return True
        else:
            logger.warning(f"  ⚠ Reward {final_reward} is outside expected range [0, 1]")
            return False
        
    except Exception as e:
        logger.error(f"✗ Reward calculation failed: {e}")
        traceback.print_exc()
        return False


def main():
    """主测试流程"""
    print("\n" + "🚀" * 30)
    print("R2E-Gym PDB 工具集成测试")
    print("🚀" * 30 + "\n")
    
    all_results = []
    
    # 1. 检查依赖
    if not check_dependencies():
        logger.error("❌ 依赖检查失败，无法继续测试")
        return False
    all_results.append(("Dependencies", True))
    
    # 2. 检查 K8s 连接
    # k8s_ok = test_kubernetes_connection()
    # all_results.append(("Kubernetes connection", k8s_ok))
    # if not k8s_ok:
    #     logger.error("❌ Kubernetes 连接失败，无法继续测试")
    #     return False
    
    # 3. 测试系统提示
    prompts_ok = test_system_prompts()
    all_results.append(("System prompts", prompts_ok))
    
    # 4. 测试工具列表
    tools_ok = test_tool_lists()
    all_results.append(("Tool lists", tools_ok))
    
    # 5. 测试 Agent 初始化
    agent_results = test_agent_initialization()
    all_results.extend(agent_results)
    
    # 6. 测试标准环境（不含 PDB）
    # env_standard = None
    # try:
    #     success, env_standard = test_env_creation_standard()
    #     all_results.append(("Standard env creation", success))
        
    #     if success and env_standard:
    #         # 重置环境
    #         reset_ok, obs = test_env_reset(env_standard, "Standard Environment")
    #         all_results.append(("Standard env reset", reset_ok))
            
    #         # 测试标准工具
    #         if reset_ok:
    #             tool_results = test_standard_tools(env_standard)
    #             all_results.extend(tool_results)
            
    #         # 关闭环境
    #         env_standard.close()
    #         logger.info("✓ Standard environment closed")
    # except Exception as e:
    #     logger.error(f"✗ Standard environment tests failed: {e}")
    #     traceback.print_exc()
    #     all_results.append(("Standard env tests", False))
    #     if env_standard:
    #         env_standard.close()
    
    # 7. 测试 Debug 环境（含 PDB）
    env_debug = None
    try:
        success, env_debug = test_env_creation_debug()
        all_results.append(("Debug env creation", success))
        
        if success and env_debug:
            # 重置环境
            reset_ok, obs = test_env_reset(env_debug, "Debug Environment")
            all_results.append(("Debug env reset", reset_ok))
            
            # 测试 PDB 工具
            if reset_ok:
                pdb_results = test_pdb_tools(env_debug)
                all_results.extend(pdb_results)
                
                # 测试奖励计算
                reward_ok = test_reward_calculation(env_debug)
                all_results.append(("Reward calculation", reward_ok))
            
            # 关闭环境
            env_debug.close()
            logger.info("✓ Debug environment closed")
    except Exception as e:
        logger.error(f"✗ Debug environment tests failed: {e}")
        traceback.print_exc()
        all_results.append(("Debug env tests", False))
        if env_debug:
            env_debug.close()
    
    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    
    passed = 0
    failed = 0
    
    for test_name, success in all_results:
        status = "✓ 通过" if success else "✗ 失败"
        print(f"  {test_name}: {status}")
        if success:
            passed += 1
        else:
            failed += 1
    
    print("\n" + "-" * 60)
    print(f"总计: {passed} 通过, {failed} 失败")
    print("=" * 60)
    
    all_passed = failed == 0
    
    if all_passed:
        print("\n✅ 所有测试通过！PDB 工具集成成功！")
        print("\n下一步:")
        print("  1. 使用 r2egym-debug-withtest agent 进行测试调试")
        print("  2. 使用 r2egym-debug agent 调试自定义脚本")
        print("  3. 在训练脚本中使用 scaffold='r2egym-debug-withtest'")
    else:
        print("\n⚠️  部分测试失败，请检查日志")
    
    print()
    
    return all_passed


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


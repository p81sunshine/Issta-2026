#!/usr/bin/env python3
"""
Debug-Gym Agent端到端测试（可直接运行）

使用真实的DebugGymAgent、SWE-bench环境和Nvidia API进行完整测试。

测试流程：
1. 初始化Nvidia LLM
2. 创建SWE-bench环境（K8s后端）
3. 创建DebugGymAgent
4. 运行Agent-Environment交互循环
5. 验证所有工具（pdb, eval, view, grep, rewrite, listdir）
"""
import json
import logging
import os
import sys
import traceback

from openai import OpenAI

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def check_dependencies():
    """检查所需依赖"""
    logger.info("="*60)
    logger.info("检查依赖")
    logger.info("="*60)
    
    missing = []
    
    try:
        from kubernetes import client, config
        logger.info("✓ Kubernetes client")
    except ImportError:
        missing.append("kubernetes")
    
    try:
        from rllm.environments.swe.swe import SWEEnv
        logger.info("✓ SWEBenchDebugGymEnv")
    except ImportError:
        missing.append("rllm.environments.debug_gym")
    
    try:
        from rllm.agents.swe_agent import SWEAgent
        logger.info("✓ DebugGymAgent")
    except ImportError:
        missing.append("rllm.agents.debug_gym_agent")
    
    try:
        from debug_gym.gym.envs.swe_bench import SWEBenchEnv
        logger.info("✓ Debug-Gym SWE-bench")
    except ImportError:
        missing.append("debug-gym")
    
    if missing:
        logger.error(f"❌ Missing: {', '.join(missing)}")
        return False
    
    return True


class NvidiaLLM:
    """
    Nvidia API LLM包装器。
    
    兼容chat completions API，支持流式响应。
    """
    
    def __init__(
        self,
        api_key: str = "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",
        model: str = "qwen/qwen3-next-80b-a3b-instruct",
        temperature: float = 0.7,
        top_p: float = 0.9,
        max_tokens: int = 2048,
        stream: bool = True,
    ):
        self.client = OpenAI(
            base_url="https://integrate.api.nvidia.com/v1",
            api_key=api_key
        )
        self.model = model
        self.temperature = temperature
        self.top_p = top_p
        self.max_tokens = max_tokens
        self.stream = stream
        self.call_count = 0
    
    def __call__(self, messages, **kwargs):
        """兼容LLM调用接口"""
        return self.generate(messages, **kwargs)
    
    def generate(self, messages, **kwargs):
        """生成LLM响应"""
        self.call_count += 1
        
        # 显示最后一条用户消息
        if messages and messages[-1].get("role") == "user":
            last_msg = messages[-1]["content"]
            logger.info(f"  最后观察: {last_msg}...")
        
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=self.temperature,
                top_p=self.top_p,
                max_tokens=self.max_tokens,
                stream=self.stream,
                **kwargs
            )
            
            if self.stream:
                # 收集流式响应
                response_text = ""
                print("  📝 响应: ", end="", flush=True)
                for chunk in completion:
                    if chunk.choices[0].delta.content:
                        content = chunk.choices[0].delta.content
                        response_text += content
                        print(content, end="", flush=True)
                print()  # 换行
            else:
                response_text = completion.choices[0].message.content
                print(f"  📝 响应: {response_text}")
            
            logger.info(f"  ✓ 响应长度: {len(response_text)} chars")
            return response_text
            
        except Exception as e:
            logger.error(f"❌ LLM调用失败: {e}")
            traceback.print_exc()
            raise


def test_agent_with_real_env():
    """使用真实Agent、环境和LLM的端到端测试"""
    logger.info("\n" + "🚀"*30)
    logger.info("Debug-Gym Agent端到端测试")
    logger.info("🚀"*30 + "\n")
    
    env = None
    agent = None
    
    try:
        # 1. 创建LLM
        logger.info("="*60)
        logger.info("步骤1: 初始化Nvidia LLM")
        logger.info("="*60)
        
        llm = NvidiaLLM(
            model="qwen/qwen3-next-80b-a3b-instruct",
            temperature=0.7,
            top_p=0.9,
            max_tokens=2048,
            stream=True,
        )
        logger.info(f"✓ LLM初始化完成: {llm.model}")
        
        # 2. 创建环境
        logger.info("\n" + "="*60)
        logger.info("步骤2: 创建SWE-bench环境（K8s后端）")
        logger.info("="*60)
        
        from rllm.environments.debug_gym.swe_bench_env import SWEBenchDebugGymEnv
        
        env = SWEBenchDebugGymEnv(
            backend="kubernetes",
            dataset_id="princeton-nlp/SWE-bench_Lite",
            split="test",
            instance_id="astropy__astropy-7746",  # 简单实例
            max_steps=10,  # 限制步数
            enable_pdb=True,  # 启用PDB（K8s支持TTY）
            enable_bash=True,
            enable_grep=True,
            k8s_namespace="default",
            k8s_pip_mirror="https://mirrors.zju.edu.cn/pypi/web/simple",
            k8s_apt_mirror="mirrors.zju.edu.cn",
            logger_name="agent-e2e-test",
        )
        
        logger.info(f"✓ 环境创建完成")
        logger.info(f"  Backend: {env.backend}")
        logger.info(f"  Instance: {env.instance_id}")
        
        # 3. 创建Agent
        logger.info("\n" + "="*60)
        logger.info("步骤3: 创建DebugGymAgent")
        logger.info("="*60)
        
        from rllm.agents.debug_gym_agent import DebugGymAgent
        
        agent = DebugGymAgent(
            use_fn_calling=False,
            format_model_response=False,
        )
        
        logger.info("✓ Agent创建完成")
        
        # 4. Reset环境
        logger.info("\n" + "="*60)
        logger.info("步骤4: Reset环境")
        logger.info("="*60)
        
        breakpoint()
        obs, info = env.reset()
        logger.info(f"✓ 环境重置完成")
        logger.info(f"  Instance: {info.get('instance_id')}")
        logger.info(f"  Repository: {info.get('repo')}")
        logger.info(f"  初始得分: {info.get('score')}/{info.get('max_score')}")
        logger.info(f"  观察长度: {len(obs)} chars")
        
        # 初始化agent
        agent.reset()
        agent.update_from_env(obs, 0.0, False, info)
        
        # 5. 运行多步交互
        logger.info("\n" + "="*60)
        logger.info("步骤5: Agent-Environment交互循环")
        logger.info("="*60)
        
        max_steps = 5  # 限制测试步数
        total_reward = 0
        
        for step in range(max_steps):
            logger.info(f"\n{'─'*60}")
            logger.info(f"步骤 {step + 1}/{max_steps}")
            logger.info(f"{'─'*60}")
            
            # 5.1 LLM生成响应
            logger.info("📝 生成动作...")
            messages = agent.chat_completions
            logger.info(f"  Prompt: {json.dumps(messages, indent=2)}")
            breakpoint()
            
            try:
                response = llm.generate(messages)
                logger.info(f"  ✓ LLM响应生成")
            except Exception as e:
                logger.error(f"  ❌ LLM生成失败: {e}")
                break
            
            logger.info(f"  Response: {response}")
            # 5.2 Agent处理响应
            logger.info("🔧 处理响应...")
            try:
                action = agent.update_from_model(response)
                action_str = action.action
                logger.info(f"  ✓ 动作: {action_str}")
            except Exception as e:
                logger.error(f"  ❌ 动作处理失败: {e}")
                break
            
            breakpoint()
            # 5.3 环境执行动作
            logger.info("⚙️  执行动作...")
            try:
                obs, reward, done, truncated, info = env.step(action_str)
                total_reward += reward
                
                logger.info(f"  ✓ 动作执行完成")
                logger.info(f"  奖励: {reward}")
                logger.info(f"  得分: {info.get('score')}/{info.get('max_score')}")
                logger.info(f"  完成: done={done}, truncated={truncated}")
                logger.info(f"  观察: {str(obs)[:200]}...")
                
            except Exception as e:
                logger.error(f"  ❌ 动作执行失败: {e}")
                traceback.print_exc()
                break
            
            # 5.4 更新Agent
            agent.update_from_env(obs, reward, done, info)
            
            # 检查是否完成
            if done or truncated:
                logger.info(f"\n🎯 Episode完成: {'任务成功' if done else '达到最大步数'}")
                break
        
        # 6. 计算最终奖励
        logger.info("\n" + "="*60)
        logger.info("步骤6: 计算最终奖励")
        logger.info("="*60)
        
        final_reward = env.compute_final_reward()
        logger.info(f"✓ 最终奖励: {final_reward}")
        logger.info(f"  累积奖励: {total_reward}")
        logger.info(f"  轨迹步数: {len(agent.trajectory.steps)}")
        
        # 7. 清理
        logger.info("\n" + "="*60)
        logger.info("步骤7: 清理资源")
        logger.info("="*60)
        
        env.close()
        logger.info("✓ 环境已关闭")
        
        # 总结
        print("\n" + "="*60)
        print("测试总结")
        print("="*60)
        print(f"  LLM调用次数: {llm.call_count}")
        print(f"  执行步数: {len(agent.trajectory.steps)}")
        print(f"  累积奖励: {total_reward}")
        print(f"  最终奖励: {final_reward}")
        print(f"  最终得分: {info.get('score')}/{info.get('max_score')}")
        print("="*60)
        print("✅ 端到端测试完成！")
        print("="*60)
        
        return True
        
    except Exception as e:
        logger.error(f"\n❌ 测试失败: {e}")
        traceback.print_exc()
        
        if env:
            try:
                env.close()
            except:
                pass
        
        return False


def main():
    """主函数"""
    print("\n" + "🎯"*30)
    print("Debug-Gym + rLLM + K8s + Nvidia API")
    print("端到端集成测试")
    print("🎯"*30 + "\n")
    
    # 检查依赖
    if not check_dependencies():
        return False
    
    # 检查K8s连接
    logger.info("\n" + "="*60)
    logger.info("检查Kubernetes连接")
    logger.info("="*60)
    
    try:
        import subprocess
        result = subprocess.run(
            ["kubectl", "cluster-info"],
            capture_output=True,
            timeout=10
        )
        if result.returncode == 0:
            logger.info("✓ Kubernetes集群可用")
        else:
            logger.error("❌ 无法连接Kubernetes集群")
            return False
    except Exception as e:
        logger.error(f"❌ K8s连接检查失败: {e}")
        return False
    
    # 运行测试
    success = test_agent_with_real_env()
    
    if success:
        print("\n" + "🎉"*30)
        print("所有测试通过！")
        print("Debug-Gym + rLLM + K8s 完全就绪！")
        print("🎉"*30 + "\n")
        print("下一步:")
        print("  bash examples/debug_gym/train_swe_bench_k8s.sh")
        print()
    
    return success


if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n⚠️  测试被用户中断")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ 未预期的错误: {e}")
        traceback.print_exc()
        sys.exit(1)


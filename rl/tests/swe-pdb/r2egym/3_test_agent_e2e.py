#!/usr/bin/env python3
"""
R2E-Gym Agent端到端测试（可直接运行）

使用真实的SWEAgent、R2E-Gym环境和Nvidia API进行完整测试。

测试流程：
1. 初始化Nvidia LLM
2. 创建SWE-bench环境（R2E-Gym + K8s后端）
3. 创建SWEAgent
4. 运行Agent-Environment交互循环
5. 验证所有工具（pdb, file_editor, search, execute_bash等）
"""
import json
import logging
import os
import sys
import traceback

from openai import OpenAI

# 配置日志 - 添加立即刷新支持
handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
# 强制立即刷新，避免在pdb中看不到输出
handler.flush = lambda: sys.stdout.flush()

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[handler],
    force=True
)
logger = logging.getLogger(__name__)

# 确保所有 handler 都立即刷新
for h in logger.handlers:
    if hasattr(h, 'stream'):
        h.stream.reconfigure(line_buffering=True) if hasattr(h.stream, 'reconfigure') else None



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
        logger.info("✓ SWEEnv")
    except ImportError:
        missing.append("rllm.environments.swe")
    
    try:
        from rllm.agents.swe_agent import SWEAgent
        logger.info("✓ SWEAgent")
    except ImportError:
        missing.append("rllm.agents.swe_agent")
    
    try:
        import r2egym
        logger.info("✓ R2E-Gym")
    except ImportError:
        missing.append("r2egym")
    
    try:
        from datasets import load_dataset
        logger.info("✓ datasets")
    except ImportError:
        missing.append("datasets")
    
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
    logger.info("R2E-Gym Agent端到端测试")
    logger.info("🚀"*30 + "\n")
    
    env = None
    agent = None
    
    scaffold = "r2egym-debug-enhanced"
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
        
        # 2. 加载数据集并找到对应的instance
        logger.info("\n" + "="*60)
        logger.info("步骤2: 加载数据集")
        logger.info("="*60)
        
        from datasets import load_dataset
        
        dataset = load_dataset("R2E-Gym/SWE-Bench-Verified", split="test")
        logger.info(f"✓ 数据集加载完成: {len(dataset)} instances")
        
        # 找到指定instance的索引
        target_instance = "astropy__astropy-12907"
        instance_idx = None
        for idx, entry in enumerate(dataset):
            if entry.get("instance_id") == target_instance:
                instance_idx = idx
                break
        
        if instance_idx is None:
            raise ValueError(f"找不到instance: {target_instance}")
        
        logger.info(f"✓ 找到目标instance: {target_instance} (idx={instance_idx})")
        
        # 3. 创建环境
        logger.info("\n" + "="*60)
        logger.info("步骤3: 创建SWE-bench环境（R2E-Gym + K8s后端）")
        logger.info("="*60)
        
        from rllm.environments.swe.swe import SWEEnv
        
        env = SWEEnv(
            dataset=dataset,
            idx=instance_idx,
            scaffold=scaffold,  # 使用debug版本支持PDB
            backend="kubernetes",
            step_timeout=90,
            reward_timeout=300,
            verbose=True,
        )
        
        logger.info(f"✓ 环境创建完成")
        logger.info(f"  Scaffold: {env.scaffold}")
        logger.info(f"  Backend: {env.backend}")
        logger.info(f"  Instance: {env.entry.get('instance_id')}")
        
        # 4. 创建Agent
        logger.info("\n" + "="*60)
        logger.info("步骤4: 创建SWEAgent")
        logger.info("="*60)
        
        from rllm.agents.swe_agent import SWEAgent
        
        agent = SWEAgent(
            scaffold=scaffold,
            use_fn_calling=False,
        )
        
        logger.info("✓ Agent创建完成")
        logger.info(f"  Scaffold: {agent.scaffold}")
        has_pdb = "BEGIN FUNCTION #4: pdb" in agent.system_prompt
        logger.info(f"  包含PDB工具: {has_pdb}")
        
        # 5. Reset环境
        logger.info("\n" + "="*60)
        logger.info("步骤5: Reset环境")
        logger.info("="*60)
        
        obs, info = env.reset()
        logger.info(f"✓ 环境重置完成")
        logger.info(f"  Instance: {info.get('instance_id')}")
        logger.info(f"  Repository: {info.get('repo')}")
        logger.info(f"  初始得分: {info.get('score')}/{info.get('max_score')}")
        logger.info(f"  观察长度: {len(obs)} chars")
          # 强制刷新输出，确保在pdb中可见
        
        # 初始化agent
        agent.reset()
        agent.update_from_env(obs, 0.0, False, info)
          # 强制刷新输出
        
        # 6. 运行多步交互
        logger.info("\n" + "="*60)
        logger.info("步骤6: Agent-Environment交互循环")
        logger.info("="*60)
        
        max_steps = 100  # 限制测试步数
        total_reward = 0
        
        for step in range(max_steps):
            logger.info(f"\n{'─'*60}")
            logger.info(f"步骤 {step + 1}/{max_steps}")
            logger.info(f"{'─'*60}")
            
            # 6.1 LLM生成响应
            logger.info("📝 生成动作...")
            messages = agent.chat_completions
            logger.info(f"  Prompt长度: {len(str(messages))} chars")
            
            
            try:
                response = llm.generate(messages)
                logger.info(f"  ✓ LLM响应生成")
                
            except Exception as e:
                logger.error(f"  ❌ LLM生成失败: {e}")
                
                break
            
            logger.info(f"  Response长度: {len(response)} chars")
            
            # 6.2 Agent处理响应
            logger.info("🔧 处理响应...")
            try:
                action = agent.update_from_model(response)
                # if "pdb" in action.action:
                #     breakpoint()
                action_str = action.action
                logger.info(f"  ✓ 动作: {action_str[:200]}..." if len(action_str) > 200 else f"  ✓ 动作: {action_str}")
                
            except Exception as e:
                logger.error(f"  ❌ 动作处理失败: {e}")
                
                break
            
            # 6.3 环境执行动作
            logger.info("⚙️  执行动作...")
            
            try:
                obs, reward, done, info = env.step(action_str)
                total_reward += reward
                
                logger.info(f"  ✓ 动作执行完成")
                logger.info(f"  奖励: {reward}")
                logger.info(f"  得分: {info.get('score')}/{info.get('max_score')}")
                logger.info(f"  完成: done={done}")
                logger.info(f"  观察: {str(obs)[:200]}...")
                
                
            except Exception as e:
                logger.error(f"  ❌ 动作执行失败: {e}")
                traceback.print_exc()
                
                break
            
            # 6.4 更新Agent
            agent.update_from_env(obs, reward, done, info)
            
            
            # 检查是否完成
            if done:
                logger.info(f"\n🎯 Episode完成")
                break
        
        # 7. 计算最终奖励
        logger.info("\n" + "="*60)
        logger.info("步骤7: 计算最终奖励")
        logger.info("="*60)
        
        final_reward = env.compute_final_reward()
        logger.info(f"✓ 最终奖励: {final_reward}")
        logger.info(f"  累积奖励: {total_reward}")
        logger.info(f"  轨迹步数: {len(agent.trajectory.steps)}")
        
        # 7.5. 保存完整对话历史
        logger.info("\n" + "="*60)
        logger.info("步骤7.5: 保存对话历史")
        logger.info("="*60)
        
        try:
            chat_messages = agent.chat_completions
            instance_id = target_instance
            output_dir = "conversation_logs"
            os.makedirs(output_dir, exist_ok=True)
            
            import datetime
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            output_file = os.path.join(output_dir, f"{instance_id}_conversation_{timestamp}.json")
            
            conversation_data = {
                "instance_id": instance_id,
                "repository": info.get('repo'),
                "total_steps": len(agent.trajectory.steps),
                "total_reward": total_reward,
                "final_reward": final_reward,
                "final_score": f"{info.get('score')}/{info.get('max_score')}",
                "llm_calls": llm.call_count,
                "messages": chat_messages
            }
            
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(conversation_data, f, indent=2, ensure_ascii=False)
            
            logger.info(f"✓ 对话历史已保存: {output_file}")
            logger.info(f"  消息总数: {len(chat_messages)}")
            logger.info(f"  文件大小: {os.path.getsize(output_file) / 1024:.2f} KB")
        except Exception as e:
            logger.error(f"❌ 保存对话历史失败: {e}")
            traceback.print_exc()
        
        # 8. 清理
        logger.info("\n" + "="*60)
        logger.info("步骤8: 清理资源")
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
        print(f"  对话历史: {output_file}")
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
    print("R2E-Gym + rLLM + K8s + Nvidia API")
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
        print("R2E-Gym + rLLM + K8s 完全就绪！")
        print("🎉"*30 + "\n")
        print("下一步:")
        print("  使用 r2egym-debug-withtest scaffold 进行训练")
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


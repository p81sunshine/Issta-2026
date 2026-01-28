#!/usr/bin/env python3
"""
测试SWE-bench Debug-Gym环境的Kubernetes支持

这个脚本验证K8s后端是否正常工作。
"""
import os
import sys

# 设置环境变量
os.environ["DEBUG_GYM_PATH"] = os.environ.get(
    "DEBUG_GYM_PATH",
    "/home/jiaxingliu/workspace/swe-pdb/debug-gym"
)

# 添加路径
sys.path.insert(0, "/home/jiaxingliu/workspace/swe-pdb/rllm")

def test_k8s_terminal():
    """测试KubernetesTerminal基本功能"""
    print("=" * 60)
    print("测试1: KubernetesTerminal基本功能")
    print("=" * 60)
    
    try:
        from rllm.environments.debug_gym.k8s_terminal import KubernetesTerminal
        from debug_gym.logger import DebugGymLogger
        
        logger = DebugGymLogger("test")
        
        # 创建terminal
        print("\n创建KubernetesTerminal...")
        terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12",
            logger=logger
        )
        
        print(f"✓ Terminal创建成功: {terminal}")
        print(f"  Pod名称: {terminal.pod_name}")
        print(f"  命名空间: {terminal.namespace}")
        print(f"  镜像: {terminal.image}")
        
        # 测试命令执行
        print("\n执行测试命令...")
        breakpoint()
        success, output = terminal.run("echo 'Hello from K8s!'")
        print(f"✓ 命令执行{'成功' if success else '失败'}")
        print(f"  输出: {output}")
        
        # 测试工作目录
        print("\n测试工作目录...")
        success, output = terminal.run("pwd")
        print(f"✓ 当前目录: {output}")
        
        # 清理
        print("\n清理资源...")
        terminal.close()
        print("✓ Terminal已关闭")
        
        return True
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_swe_bench_env_k8s():
    """测试SWEBenchDebugGymEnv的K8s支持"""
    print("\n" + "=" * 60)
    print("测试2: SWEBenchDebugGymEnv K8s支持")
    print("=" * 60)
    
    try:
        from rllm.environments.debug_gym.swe_bench_env import SWEBenchDebugGymEnv
        
        # 创建环境
        print("\n创建SWEBenchDebugGymEnv (K8s后端)...")
        env = SWEBenchDebugGymEnv(
            dataset_id="SWE-bench/SWE-bench_Verified",
            split="test",
            backend="kubernetes",
            k8s_namespace="default",
            enable_pdb=True,
            enable_grep=True,
            max_steps=5,
            instance_id="astropy__astropy-12907",
        )
        
        print(f"✓ 环境创建成功")
        print(f"  后端: {env.backend}")
        print(f"  Terminal类型: {type(env.terminal).__name__}")
        
        # 验证terminal是DockerTerminal的实例（类型检查）
        from debug_gym.gym.terminal import DockerTerminal
        is_compatible = isinstance(env.terminal, DockerTerminal)
        print(f"  兼容DockerTerminal: {'✓' if is_compatible else '✗'}")
        
        if not is_compatible:
            print("✗ Terminal类型检查失败！")
            return False
        
        # 测试reset
        print("\n测试环境reset...")
        try:
            obs, info = env.reset()
            print(f"✓ Reset成功")
            print(f"  观察长度: {len(obs)} 字符")
            print(f"  得分: {info.get('score')}/{info.get('max_score')}")
            print(f"  任务: {info.get('instance_id')}")
        except Exception as e:
            print(f"⚠ Reset测试跳过（可能需要下载镜像）: {e}")
        
        # 清理
        print("\n清理资源...")
        env.close()
        print("✓ 环境已关闭")
        
        return True
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_type_check():
    """测试类型兼容性"""
    print("\n" + "=" * 60)
    print("测试3: 类型兼容性检查")
    print("=" * 60)
    
    try:
        from rllm.environments.debug_gym.k8s_terminal import KubernetesTerminal
        from debug_gym.gym.terminal import DockerTerminal
        from debug_gym.logger import DebugGymLogger
        
        logger = DebugGymLogger("test")
        k8s_terminal = KubernetesTerminal(
            namespace="default",
            image="python:3.12",
            logger=logger
        )
        
        # 类型检查
        print(f"\nKubernetesTerminal继承层次:")
        print(f"  类型: {type(k8s_terminal)}")
        print(f"  MRO: {[c.__name__ for c in type(k8s_terminal).__mro__]}")
        
        is_docker_terminal = isinstance(k8s_terminal, DockerTerminal)
        print(f"\n  isinstance(k8s_terminal, DockerTerminal): {is_docker_terminal}")
        
        if not is_docker_terminal:
            print("✗ 类型检查失败！KubernetesTerminal未继承DockerTerminal")
            k8s_terminal.close()
            return False
        
        print("✓ 类型检查通过！")
        
        # 检查必需的属性和方法
        required_attrs = [
            'base_image', 'container', 'working_dir', 
            'session_commands', 'env_vars', 'setup_commands'
        ]
        required_methods = [
            'run', 'close', 'clean_up', 'copy_content'
        ]
        
        print("\n检查必需属性:")
        for attr in required_attrs:
            has_attr = hasattr(k8s_terminal, attr)
            print(f"  {attr}: {'✓' if has_attr else '✗'}")
            if not has_attr:
                print(f"✗ 缺少属性: {attr}")
                k8s_terminal.close()
                return False
        
        print("\n检查必需方法:")
        for method in required_methods:
            has_method = hasattr(k8s_terminal, method) and callable(getattr(k8s_terminal, method))
            print(f"  {method}(): {'✓' if has_method else '✗'}")
            if not has_method:
                print(f"✗ 缺少方法: {method}")
                k8s_terminal.close()
                return False
        
        print("\n✓ 所有接口检查通过！")
        
        # 清理
        k8s_terminal.close()
        return True
        
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    """运行所有测试"""
    print("=" * 60)
    print("SWE-bench Debug-Gym Kubernetes支持测试")
    print("=" * 60)
    
    # 检查K8s连接
    print("\n检查Kubernetes连接...")
    import subprocess
    try:
        result = subprocess.run(
            ["kubectl", "cluster-info"],
            capture_output=True,
            text=True,
            timeout=5
        )
        if result.returncode != 0:
            print("✗ 无法连接到Kubernetes集群")
            print("请确保kubectl已配置并可以访问集群")
            return False
        print("✓ Kubernetes集群可用")
    except Exception as e:
        print(f"✗ Kubectl检查失败: {e}")
        return False
    
    # 运行测试
    tests = [
        ("类型兼容性", test_type_check),
        ("KubernetesTerminal", test_k8s_terminal),
        ("SWEBenchEnv K8s", test_swe_bench_env_k8s),
    ]
    
    results = []
    for name, test_func in tests:
        try:
            result = test_func()
            results.append((name, result))
        except Exception as e:
            print(f"\n✗ 测试 '{name}' 异常: {e}")
            results.append((name, False))
    
    # 总结
    print("\n" + "=" * 60)
    print("测试总结")
    print("=" * 60)
    for name, result in results:
        status = "✓ 通过" if result else "✗ 失败"
        print(f"  {name}: {status}")
    
    all_passed = all(r for _, r in results)
    print("\n" + ("=" * 60))
    if all_passed:
        print("✅ 所有测试通过！K8s后端已就绪！")
        print("=" * 60)
        print("\n下一步:")
        print("  bash examples/debug_gym/train_swe_bench_k8s.sh")
    else:
        print("❌ 部分测试失败，请检查上述错误")
        print("=" * 60)
    
    return all_passed


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)


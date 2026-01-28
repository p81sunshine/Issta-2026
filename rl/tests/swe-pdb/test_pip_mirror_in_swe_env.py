#!/usr/bin/env python3
"""
Verify pip mirror inside SWEEnv (Kubernetes backend).

This test creates a SWEEnv with backend="kubernetes", resets the env, then runs
`python -m pip config get global.index-url` inside the container/pod to verify
that the ZJU mirror is configured.
"""

import os
import sys
import traceback

# Add the project paths
sys.path.insert(0, '/home/jiaxingliu/workspace/swe-pdb/rllm')
sys.path.insert(0, '/home/jiaxingliu/workspace/swe-pdb/R2E-Gym/src')


def test_pip_mirror_in_swe_env():
    print("=== Testing pip mirror inside SWEEnv (K8s) ===")

    try:
        from datasets import load_dataset
        from rllm.environments.swe.swe import SWEEnv

        # Load a sample SWE-Bench-Verified entry
        dataset = load_dataset("R2E-Gym/SWE-Bench-Verified", split="test")
        entry = dataset[0]
        print(f"✓ Sample entry loaded: {entry.get('repo', 'unknown')}")

        # Create SWEEnv with Kubernetes backend
        env = SWEEnv(
            entry=entry,
            step_timeout=60,
            reward_timeout=180,
            backend="kubernetes",
            verbose=True,
        )
        print("✓ SWEEnv created")

        # Reset environment (create container/pod and initialize)
        print("  Resetting SWEEnv ...")
        observation, info = env.reset()
        print("✓ SWEEnv reset completed")
        breakpoint()

        # Verify pip mirror inside env by running a command
        cmd = "python -m pip config get global.index-url"
        print(f"  Running: {cmd}")
        observation, reward, done, step_info = env.step(cmd)
        print("--- Command Output ---")
        print(observation)
        print("----------------------")

        expected = "https://mirrors.zju.edu.cn/pypi/web/simple"
        ok = expected in (observation or "")

        # Teardown
        if hasattr(env, 'env') and env.env and hasattr(env.env, 'close'):
            env.env.close()

        assert ok, "pip mirror 未检测到浙大镜像，见上方输出以排查"
        print("✓ pip mirror 已配置为浙大镜像")

    except Exception as e:
        print(f"✗ Test failed: {e}")
        traceback.print_exc()
        assert False, str(e)


if __name__ == "__main__":
    # Allow running this file directly
    test_pip_mirror_in_swe_env()




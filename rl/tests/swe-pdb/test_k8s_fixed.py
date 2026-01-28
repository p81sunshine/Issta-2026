#!/usr/bin/env python3
"""
Test Kubernetes SWE Environment After Fix

This script tests if the SWE environment with Kubernetes backend works
after fixing the node labeling issue.
"""

import os
import sys
import time
import traceback
from pathlib import Path

# Add the project paths
sys.path.insert(0, '/home/jiaxingliu/workspace/swe-pdb/rllm')
sys.path.insert(0, '/home/jiaxingliu/workspace/swe-pdb/R2E-Gym/src')

def test_simple_pod_creation():
    """Test creating a simple pod to verify scheduling works"""
    print("=== Testing Simple Pod Creation ===")
    
    try:
        from kubernetes import client, config
        import uuid
        
        # Load config
        try:
            config.load_incluster_config()
        except Exception:
            config.load_kube_config()
        
        v1 = client.CoreV1Api()
        
        # Create a simple pod spec
        pod_name = f"test-pod-{uuid.uuid4().hex[:8]}"
        pod_spec = client.V1Pod(
            metadata=client.V1ObjectMeta(name=pod_name),
            spec=client.V1PodSpec(
                node_selector={"karpenter.sh/nodepool": "bigcpu-standby"},
                containers=[
                    client.V1Container(
                        name="test-container",
                        image="busybox:latest",
                        command=["sleep", "60"]
                    )
                ],
                restart_policy="Never"
            )
        )
        
        print(f"  Creating pod: {pod_name}")
        
        # Create the pod
        pod = v1.create_namespaced_pod(
            namespace="default",
            body=pod_spec,
            _request_timeout=30
        )
        print(f"✓ Pod created: {pod.metadata.name}")
        
        # Wait and check status
        for i in range(12):  # Wait up to 2 minutes
            time.sleep(10)
            pod_status = v1.read_namespaced_pod_status(
                name=pod_name,
                namespace="default",
                _request_timeout=10
            )
            phase = pod_status.status.phase
            print(f"  Pod status: {phase}")
            
            if phase == "Running":
                print("✓ Pod is running successfully!")
                break
            elif phase == "Failed" or phase == "Succeeded":
                print(f"✗ Pod ended with status: {phase}")
                break
        else:
            print("⚠ Pod did not reach Running state within timeout")
        
        # Clean up
        v1.delete_namespaced_pod(
            name=pod_name,
            namespace="default",
            _request_timeout=30
        )
        print(f"✓ Pod deleted: {pod_name}")
        
        return phase == "Running"
        
    except Exception as e:
        print(f"✗ Pod creation test failed: {e}")
        traceback.print_exc()
        return False

def test_swe_env_quick():
    """Test SWE environment creation with a quick timeout"""
    print("\n=== Testing SWE Environment (Quick Test) ===")
    
    try:
        from datasets import load_dataset
        from rllm.environments.swe.swe import SWEEnv
        
        # Load a sample dataset entry
        dataset = load_dataset("R2E-Gym/SWE-Bench-Verified", split="test")
        sample_entry = dataset[0]
        print(f"✓ Loaded sample entry: {sample_entry.get('repo', 'unknown')}")
        
        # Create SWEEnv with shorter timeouts
        swe_env = SWEEnv(
            entry=sample_entry,
            step_timeout=30,
            reward_timeout=120,
            backend="kubernetes",
            verbose=True
        )
        print("✓ SWEEnv created successfully")
        
        # Try to reset with a timeout
        print("  Attempting to reset environment (with timeout)...")
        try:
            observation, info = swe_env.reset()
            print("✓ SWEEnv reset successful!")
            print(f"Observation: {observation}")
            print(f"Info: {info}")
            print(f"  Observation length: {len(observation) if observation else 0}")

            action = "ls -la"
            print(f"  Executing action: {action}")
        
            observation, reward, done, info = swe_env.step(action)

            print(f"  Observation: {observation}")
            print(f"  Reward: {reward}")
            print(f"  Done: {done}")
            print(f"  Info: {info}")
            # Clean up
            if hasattr(swe_env, 'env') and swe_env.env:
                if hasattr(swe_env.env, 'close'):
                    swe_env.env.close()
            
            return True
            
        except Exception as e:
            print(f"✗ SWEEnv reset failed: {e}")
            # Clean up on failure
            if hasattr(swe_env, 'env') and swe_env.env:
                if hasattr(swe_env.env, 'close'):
                    swe_env.env.close()
            return False
        
    except Exception as e:
        print(f"✗ SWEEnv creation failed: {e}")
        traceback.print_exc()
        return False

def main():
    """Main test function"""
    print("=== Kubernetes SWE Environment Test (After Fix) ===")
    print(f"Python version: {sys.version}")
    print(f"Working directory: {os.getcwd()}")
    
    # Disable proxy for testing
    try:
        # Test 1: Simple pod creation
        pod_test_ok = test_simple_pod_creation()
        
        if not pod_test_ok:
            print("\n✗ Pod scheduling still not working")
            return 1
        
        # Test 2: SWE environment
        swe_test_ok = test_swe_env_quick()
        
        print("\n=== Test Results ===")
        if pod_test_ok and swe_test_ok:
            print("✓ All tests passed!")
            print("✓ Kubernetes SWE environment is working correctly")
            print("✓ You can now run the original training script")
        elif pod_test_ok:
            print("✓ Pod scheduling is working")
            print("⚠ SWE environment test had issues, but basic functionality works")
        else:
            print("✗ Pod scheduling is still not working")
        
        return 0 if (pod_test_ok and swe_test_ok) else 1
        
    except KeyboardInterrupt:
        print("\n⚠ Test interrupted by user")
        return 1
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())



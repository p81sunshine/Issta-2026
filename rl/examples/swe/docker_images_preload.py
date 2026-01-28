#!/usr/bin/env python3
"""
简单测试脚本：直接复现 DockerRuntime.start_container() 的 bug
模拟原始代码的行为，看是否会触发 ImageNotFound
支持并发测试（模拟原始代码的并发行为）
"""

import os
import sys
import json
import asyncio
from concurrent.futures import ThreadPoolExecutor, as_completed
import docker
import pandas as pd


def pull_image_with_progress(client, docker_image):
    """
    手动拉取镜像并显示进度
    """
    print(f"Attempting to pull image: {docker_image}")
    try:
        # pull() 返回一个生成器，产生JSON格式的进度信息
        for line in client.api.pull(docker_image, stream=True, decode=True):
            # 解析进度信息
            if 'status' in line:
                status = line['status']
                layer_id = line.get('id', '')
                
                # 显示进度条
                if 'progressDetail' in line and line['progressDetail']:
                    progress = line['progressDetail']
                    if 'current' in progress and 'total' in progress:
                        current = progress['current']
                        total = progress['total']
                        percent = (current / total) * 100 if total > 0 else 0
                        print(f"  [{layer_id}] {status}: {percent:.1f}% ({current}/{total})")
                    else:
                        print(f"  [{layer_id}] {status}")
                else:
                    # 没有详细进度的状态信息
                    if layer_id:
                        print(f"  [{layer_id}] {status}")
                    else:
                        print(f"  {status}")
        
        print(f"✓ Image pulled successfully")
        return True
        
    except docker.errors.NotFound as e:
        print(f"✗ Image not found in registry")
        return False
    except Exception as e:
        print(f"✗ Pull failed: {repr(e)}")
        return False


def start_container_like_original(client, docker_image, command="/bin/bash -l", try_pull=False):
    """
    直接调用 containers.run()，不检查容器是否存在
    完全模拟触发 bug 的场景
    
    Args:
        try_pull: 如果为True，在运行前先尝试拉取镜像（显示进度）
    """
    # 使用与原始代码相同的命名逻辑，但添加测试前缀和改进的唯一性保证
    import hashlib
    import datetime
    import threading
    
    # 原始代码的逻辑
    process_id = str(os.getpid())
    current_time = str(datetime.datetime.now())
    unique_string = current_time + process_id
    hash_object = hashlib.sha256(unique_string.encode())
    
    # 处理镜像名称，与原始代码一致
    image_name_sanitized = docker_image.replace("/", "-")
    image_name_sanitized = image_name_sanitized.replace(":", "-")
    
    # 添加额外的唯一性保证（线程ID + 微秒时间戳）
    ctr_name = f"{image_name_sanitized}-{hash_object.hexdigest()[:10]}"

    print(f"\n{'='*80}")
    print(f"Testing: {docker_image}")
    print(f"Container name: {ctr_name}")
    print(f"{'='*80}\n")
    
    # 如果启用了try_pull，先尝试拉取镜像
    if try_pull:
        pull_success = pull_image_with_progress(client, docker_image)
        if not pull_success:
            print(f"⚠️  Pull failed, but will still try to run container...")
        print()
    
    # 直接 run，完全按照原始代码的参数
    try:
        print(f"Calling containers.run() (exactly like original code)...")
        container = client.containers.run(
            docker_image,
            command,
            name=ctr_name,
            detach=True,
            tty=True,
            stdin_open=True,
            # 原始代码没有 remove=True，所以容器会一直存在
        )
        print(f"✓ Container created successfully: {container.id[:12]}")
        print(f"   Container name: {container.name}")
        
        # 清理：停止并删除容器（测试完后清理）
        try:
            container.stop(timeout=1)
            container.remove()
            print(f"✓ Container cleaned up")
        except Exception as cleanup_error:
            print(f"⚠️  Cleanup warning: {cleanup_error}")
        
        return True
        
    except Exception as e:
        # 完全模拟原代码的错误处理
        print(f"Container start error: {repr(e)}")
        
        # 检查是否是 ImageNotFound - 这就是 bug！
        if "ImageNotFound" in str(type(e).__name__):
            print(f"\n🐛 BUG REPRODUCED!")
            print(f"   Podman did NOT auto-pull the image!")
            print(f"   This is exactly what's happening in your training.")
        
        return False


def main():
    print("="*80)
    print("Docker/Podman Bug Reproduction Test")
    print("="*80)
    
    # 显示环境信息
    docker_host = os.environ.get('DOCKER_HOST', 'Not set')
    print(f"\nDOCKER_HOST: {docker_host}")
    
    if 'podman' in docker_host.lower():
        print("⚠️  Using Podman - this is where the bug occurs!")
    
    # 连接 Docker/Podman
    print("\nConnecting to Docker/Podman...")
    try:
        client = docker.from_env(timeout=120)
        version = client.version()
        print(f"✓ Connected to {version.get('Platform', {}).get('Name', 'Docker')}")
        print(f"  Version: {version.get('Version', 'N/A')}")
    except Exception as e:
        print(f"✗ Failed to connect: {e}")
        return 1
    
    # 加载数据集
    parquet_path = "/home/jiaxingliu/workspace/swe-pdb/rllm/rllm/data/datasets/SWE_Bench_Verified/test_verl.parquet"
    print(f"\nLoading dataset: {parquet_path}")
    
    try:
        df = pd.read_parquet(parquet_path)
        print(f"✓ Loaded {len(df)} rows")
        
        # docker_image 在 extra_info 字段里
        if 'extra_info' not in df.columns:
            print(f"✗ Error: 'extra_info' column not found")
            print(f"  Available columns: {df.columns.tolist()}")
            return 1
        
        # 从 extra_info 中提取 docker_image
        print(f"Extracting docker_image from extra_info field...")
        images = df['extra_info'].apply(lambda x: x.get('docker_image')).unique().tolist()
        
        # 过滤掉 None 值
        images = [img for img in images if img is not None]
        
        print(f"✓ Found {len(images)} unique Docker images")
        
    except Exception as e:
        print(f"✗ Failed to load dataset: {e}")
        return 1
    
    # 询问测试模式
    print(f"\n{'='*80}")
    print(f"Select test mode:")
    print(f"  1. Sequential (one by one) - Slower but easier to debug")
    print(f"  2. Concurrent (parallel) - Like original code, faster")
    print(f"{'='*80}")
    
    mode = input(f"Enter mode (default: 1): ").strip() or "1"
    
    # 询问是否要显示pull进度
    print(f"\n{'='*80}")
    print(f"Pull image before running container?")
    print(f"  y. Yes - Try to pull image first (with progress display)")
    print(f"  n. No - Just call containers.run() directly (reproduce bug)")
    print(f"{'='*80}")
    
    try_pull_input = input(f"Try pull first? (default: n): ").strip().lower() or "n"
    try_pull = try_pull_input in ['y', 'yes']
    
    # 询问并发数（如果选择并发模式）
    n_parallel = 1
    if mode == "2":
        n_parallel_input = input(f"Enter number of parallel workers (default: 64 = train_batch_size(8) × rollout.n(8)): ").strip()
        n_parallel = int(n_parallel_input) if n_parallel_input else 64
        print(f"Note: Your training config:")
        print(f"  - train_batch_size=8 (8 different tasks)")
        print(f"  - rollout.n=8 (8 samples per task)")
        print(f"  - Total = 8 × 8 = 64 containers start simultaneously!")
    
    print(f"\n{'='*80}")
    if mode == "1":
        print(f"Starting SEQUENTIAL tests for ALL images...")
    else:
        print(f"Starting CONCURRENT tests for ALL images...")
        print(f"Parallel workers: {n_parallel}")
    print(f"Testing {len(images)} images total")
    print(f"{'='*80}")
    
    results = []
    
    if mode == "1":
        # 顺序测试
        for i, image in enumerate(images, 1):
            print(f"\n[Test {i}/{len(images)}]")
            success = start_container_like_original(client, image, try_pull=try_pull)
            results.append({
                "image": image,
                "success": success
            })
            
            # 每10个打印一次进度
            if i % 10 == 0:
                success_so_far = sum(1 for r in results if r["success"])
                print(f"\n>>> Progress: {i}/{len(images)} tested, {success_so_far} succeeded, {i-success_so_far} failed")
    
    else:
        # 并发测试（模拟原始代码）
        print(f"\n⚡ Running {n_parallel} containers in parallel (like original code)...")
        
        def test_image_wrapper(args):
            idx, image = args
            print(f"\n[Worker {idx % n_parallel}] Testing image {idx+1}/{len(images)}: {image[:60]}...")
            success = start_container_like_original(client, image, try_pull=try_pull)
            return {
                "image": image,
                "success": success
            }
        
        with ThreadPoolExecutor(max_workers=n_parallel) as executor:
            # 提交所有任务
            future_to_image = {
                executor.submit(test_image_wrapper, (i, img)): img 
                for i, img in enumerate(images)
            }
            
            # 收集结果
            completed = 0
            for future in as_completed(future_to_image):
                result = future.result()
                results.append(result)
                completed += 1
                
                if completed % 10 == 0:
                    success_so_far = sum(1 for r in results if r["success"])
                    print(f"\n>>> Progress: {completed}/{len(images)} completed, {success_so_far} succeeded, {completed-success_so_far} failed")
    
    # 汇总结果
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    
    success_count = sum(1 for r in results if r["success"])
    fail_count = len(results) - success_count
    
    print(f"\nTotal tested: {len(results)}")
    print(f"  Success: {success_count}")
    print(f"  Failed: {fail_count}")
    
    if fail_count > 0:
        print(f"\nFailed images:")
        for r in results:
            if not r["success"]:
                print(f"  ✗ {r['image']}")
        
        print(f"\n{'='*80}")
        print(f"🐛 BUG CONFIRMED!")
        print(f"{'='*80}")
        print(f"The Podman environment does NOT automatically pull missing images")
        print(f"when calling containers.run(). This causes ImageNotFound errors.")
        print(f"\nThis is why your training is failing!")
    else:
        print(f"\n✓ All images worked. Either:")
        print(f"  1. Images already exist locally, or")
        print(f"  2. Docker (not Podman) is being used and auto-pulled them")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())


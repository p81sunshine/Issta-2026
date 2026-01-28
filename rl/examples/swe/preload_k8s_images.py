#!/usr/bin/env python3
"""
Preload Kubernetes SWEEnv images by iterating over the dataset and creating the
environment once per instance (quick reset), so images are pulled and cached.

参考 test_k8s_fixed.py：
- 加载数据集
- 异步并行创建 SWEEnv(backend=kubernetes)，调用 reset() 触发镜像拉取
- 立即关闭以释放资源

建议：在集群空闲时运行，防止批量拉取占用资源过多。
"""

import argparse
import asyncio
import sys
import time
from typing import Tuple, Optional

# Project paths
sys.path.insert(0, '/home/jiaxingliu/workspace/swe-pdb/rllm')
sys.path.insert(0, '/home/jiaxingliu/workspace/swe-pdb/R2E-Gym/src')


async def preload_single_instance(
    idx: int,
    entry: dict,
    total: int,
    step_timeout: int,
    reward_timeout: int,
    semaphore: asyncio.Semaphore,
    counter: dict,
) -> Tuple[bool, str, Optional[str]]:
    """异步预加载单个实例的镜像。"""
    async with semaphore:  # 限制并发数
        from rllm.environments.swe.swe import SWEEnv
        
        instance_id = entry.get('instance_id') or entry.get('repo') or f'idx-{idx}'
        
        swe_env = None
        try:
            # 在事件循环的线程池中执行同步 K8s 操作
            swe_env = await asyncio.to_thread(
                SWEEnv,
                entry=entry,
                step_timeout=step_timeout,
                reward_timeout=reward_timeout,
                backend="kubernetes",
                verbose=False,
            )
            
            # 异步执行 reset()
            _observation, _info = await asyncio.to_thread(swe_env.reset)
            
            # 更新计数器
            counter['ok'] += 1
            current = counter['ok'] + counter['fail']
            print(f"[{current}/{total}] ✓ {instance_id}")
            
            return True, instance_id, None
        except Exception as e:
            counter['fail'] += 1
            current = counter['ok'] + counter['fail']
            print(f"[{current}/{total}] ✗ {instance_id}: {e}")
            
            return False, instance_id, str(e)
        finally:
            try:
                if swe_env and hasattr(swe_env, 'env') and swe_env.env and hasattr(swe_env.env, 'close'):
                    await asyncio.to_thread(swe_env.env.close)
            except Exception:
                pass


async def preload_images_async(
    dataset_name: str,
    split: str,
    limit: int | None,
    step_timeout: int,
    reward_timeout: int,
    max_workers: int = 5,
) -> int:
    from datasets import load_dataset

    print(f"=== Preloading images from dataset '{dataset_name}' split '{split}' ===")
    print(f"Using {max_workers} async workers for parallel preloading")

    dataset = load_dataset(dataset_name, split=split)
    total = len(dataset) if limit is None else min(limit, len(dataset))
    print(f"Total instances to preload: {total}")

    # 共享计数器（在 asyncio 中无需锁，因为单个事件循环）
    counter = {'ok': 0, 'fail': 0}
    
    # 使用 Semaphore 限制并发数
    semaphore = asyncio.Semaphore(max_workers)
    
    # 创建所有任务
    tasks = [
        preload_single_instance(
            idx=idx,
            entry=dataset[idx],
            total=total,
            step_timeout=step_timeout,
            reward_timeout=reward_timeout,
            semaphore=semaphore,
            counter=counter,
        )
        for idx in range(total)
    ]

    # 异步并发执行所有任务
    start_time = time.time()
    results = await asyncio.gather(*tasks, return_exceptions=True)
    
    # 统计异常情况
    for result in results:
        if isinstance(result, Exception):
            counter['fail'] += 1
            print(f"✗ Task failed with exception: {result}")
    
    elapsed_time = time.time() - start_time

    print("\n=== Preload summary ===")
    print(f"Success: {counter['ok']}")
    print(f"Failed:  {counter['fail']}")
    print(f"Total time: {elapsed_time:.1f}s")
    print(f"Average time per instance: {elapsed_time/total:.1f}s")
    
    return 0 if counter['fail'] == 0 else 1


def preload_images(
    dataset_name: str,
    split: str,
    limit: int | None,
    sleep_seconds: float,
    step_timeout: int,
    reward_timeout: int,
    max_workers: int = 5,
) -> int:
    """同步入口，调用异步实现。"""
    return asyncio.run(preload_images_async(
        dataset_name=dataset_name,
        split=split,
        limit=limit,
        step_timeout=step_timeout,
        reward_timeout=reward_timeout,
        max_workers=max_workers,
    ))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Preload Kubernetes SWEEnv images")
    p.add_argument('--dataset', default='R2E-Gym/SWE-Bench-Verified', help='HF dataset name')
    p.add_argument('--split', default='test', help='dataset split')
    p.add_argument('--limit', type=int, default=None, help='limit number of instances (for smoke test)')
    p.add_argument('--sleep', type=float, default=0.0, help='sleep seconds between instances (not used in parallel mode)')
    p.add_argument('--step-timeout', type=int, default=60, help='SWE step timeout seconds')
    p.add_argument('--reward-timeout', type=int, default=180, help='SWE reward timeout seconds')
    p.add_argument('--max-workers', type=int, default=64, help='number of parallel workers')
    return p.parse_args()


def main() -> int:
    args = parse_args()
    return preload_images(
        dataset_name=args.dataset,
        split=args.split,
        limit=args.limit,
        sleep_seconds=args.sleep,
        step_timeout=args.step_timeout,
        reward_timeout=args.reward_timeout,
        max_workers=args.max_workers,
    )


if __name__ == '__main__':
    sys.exit(main())



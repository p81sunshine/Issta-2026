#!/usr/bin/env python3
"""
预加载 SWE-bench Debug-Gym 环境的 Kubernetes 镜像

通过遍历数据集并创建环境实例（调用 reset()）来触发镜像拉取，预缓存镜像到节点。

参考 preload_k8s_images.py：
- 加载 SWE-bench 数据集
- 异步并行创建 SWEBenchDebugGymEnv(backend=kubernetes)，调用 reset() 触发镜像拉取
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
    dataset_id: str,
    dataset_revision: str,
    split: str,
    k8s_namespace: str,
    k8s_pip_mirror: str | None,
    k8s_apt_mirror: str | None,
    max_steps: int,
    run_timeout: int,
    semaphore: asyncio.Semaphore,
    counter: dict,
) -> Tuple[bool, str, Optional[str]]:
    """异步预加载单个实例的镜像。"""
    async with semaphore:  # 限制并发数
        from rllm.environments.debug_gym.swe_bench_env import SWEBenchDebugGymEnv
        
        instance_id = entry.get('instance_id', f'idx-{idx}')
        
        swe_env = None
        try:
            # 在事件循环的线程池中执行同步操作
            swe_env = await asyncio.to_thread(
                SWEBenchDebugGymEnv,
                dataset_id=dataset_id,
                dataset_revision=dataset_revision,
                split=split,
                instance_id=instance_id,
                backend="kubernetes",
                k8s_namespace=k8s_namespace,
                k8s_pip_mirror=k8s_pip_mirror,
                k8s_apt_mirror=k8s_apt_mirror,
                max_steps=max_steps,
                run_timeout=run_timeout,
                enable_pdb=True,
                enable_grep=True,
                enable_bash=False,
                auto_list=True,
                auto_eval_on_rewrite=False,
                persistent_breakpoints=True,
                dir_tree_depth=2,
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
                if swe_env and hasattr(swe_env, 'close'):
                    await asyncio.to_thread(swe_env.close)
            except Exception:
                pass


async def preload_images_async(
    dataset_id: str,
    dataset_revision: str,
    split: str,
    limit: int | None,
    k8s_namespace: str,
    k8s_pip_mirror: str | None,
    k8s_apt_mirror: str | None,
    max_steps: int,
    run_timeout: int,
    max_workers: int = 5,
) -> int:
    from datasets import load_dataset

    print(f"=== Preloading SWE-bench images from dataset '{dataset_id}' split '{split}' ===")
    print(f"Using {max_workers} async workers for parallel preloading")

    # 加载数据集
    dataset = load_dataset(dataset_id, revision=dataset_revision)[split]
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
            dataset_id=dataset_id,
            dataset_revision=dataset_revision,
            split=split,
            k8s_namespace=k8s_namespace,
            k8s_pip_mirror=k8s_pip_mirror,
            k8s_apt_mirror=k8s_apt_mirror,
            max_steps=max_steps,
            run_timeout=run_timeout,
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
    dataset_id: str,
    dataset_revision: str,
    split: str,
    limit: int | None,
    sleep_seconds: float,
    k8s_namespace: str,
    k8s_pip_mirror: str | None,
    k8s_apt_mirror: str | None,
    max_steps: int,
    run_timeout: int,
    max_workers: int = 1,
) -> int:
    """同步入口，调用异步实现。"""
    return asyncio.run(preload_images_async(
        dataset_id=dataset_id,
        dataset_revision=dataset_revision,
        split=split,
        limit=limit,
        k8s_namespace=k8s_namespace,
        k8s_pip_mirror=k8s_pip_mirror,
        k8s_apt_mirror=k8s_apt_mirror,
        max_steps=max_steps,
        run_timeout=run_timeout,
        max_workers=max_workers,
    ))


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Preload SWE-bench Debug-Gym Kubernetes images")
    p.add_argument('--dataset', default='R2E-Gym/SWE-Bench-Verified', help='HF dataset ID')
    p.add_argument('--revision', default='99450355ca8c611021187a57ffac304b66666738', help='dataset revision')
    p.add_argument('--split', default='test', help='dataset split')
    p.add_argument('--limit', type=int, default=None, help='limit number of instances (for smoke test)')
    p.add_argument('--sleep', type=float, default=0.0, help='sleep seconds between instances (not used in parallel mode)')
    p.add_argument('--k8s-namespace', default='default', help='Kubernetes namespace')
    p.add_argument('--k8s-pip-mirror', default='https://mirrors.zju.edu.cn/pypi/web/simple', help='pip mirror URL')
    p.add_argument('--k8s-apt-mirror', default='mirrors.zju.edu.cn', help='apt mirror domain')
    p.add_argument('--max-steps', type=int, default=50, help='max steps per episode')
    p.add_argument('--run-timeout', type=int, default=300, help='run timeout seconds')
    p.add_argument('--max-workers', type=int, default=1, help='number of parallel workers')
    return p.parse_args()


def main() -> int:
    args = parse_args()
    return preload_images(
        dataset_id=args.dataset,
        dataset_revision=args.revision,
        split=args.split,
        limit=args.limit,
        sleep_seconds=args.sleep,
        k8s_namespace=args.k8s_namespace,
        k8s_pip_mirror=args.k8s_pip_mirror,
        k8s_apt_mirror=args.k8s_apt_mirror,
        max_steps=args.max_steps,
        run_timeout=args.run_timeout,
        max_workers=args.max_workers,
    )


if __name__ == '__main__':
    sys.exit(main())


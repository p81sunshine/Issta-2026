from typing import List
import heapq

def maxPerformance(n: int, speed: List[int], efficiency: List[int], k: int) -> int:
    MOD = 10**9 + 7

    top_k_speeds = []
    res, top_k_sum = 0, 0

    pairs = [(e, s) for e, s in zip(efficiency, speed)]
    for e, s in sorted(pairs, reverse=True):
        heapq.heappush(top_k_speeds, s)
        top_k_sum += s

        if len(top_k_speeds) > k:
            top_k_sum -= heapq.heappop(top_k_speeds)

        res = max(res, e * top_k_sum)

    print(res % MOD)
    return res % MOD
from typing import List
from math import ceil

def minEatingSpeed(piles: List[int], h: int) -> int:
    def check(x):
        return sum(ceil(ele/x) for ele in piles) <= h

    l = 1
    r = max(piles)
    while l < r:
        mid = (l + r) // 1
        if not check(mid):
            l = mid + 1
        else:
            r = mid
    return l
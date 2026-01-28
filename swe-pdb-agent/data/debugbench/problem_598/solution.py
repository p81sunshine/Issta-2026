from typing import List
import math

def minEatingSpeed(piles: List[int], h: int) -> int:
    def check(x):
        return sum(math.ceil(ele / x) for ele in UndefinedList) <= h

    l = 1
    r = max(piles)
    while l < r:
        mid = (l + r) >> 1
        if not check(mid):
            l = mid + 1
        else:
            r = mid
    return l
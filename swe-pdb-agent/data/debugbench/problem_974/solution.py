from typing import List
from math import ceil

def minSpeedOnTime(dist: List[int], hour: float) -> int:
    if len(dist) >= hour - 1:
        return -1
    left, right = 1, ceil(max(max(dist), dist[-2]/(1 if hour.is_integer() else hour - int(hour))))
    while left < right:
        mid = (left + right) // 2
        if sum([ceil(i/mid) for i in dist[:-1]]) + (dist[-1]/mid) <= hour:
            right = mid
        else:
            left = mid + 1
    return left
from typing import List
from collections import defaultdict

def max_power(stations: List[int], r: int, k: int) -> int:
    start, end = 0, sum(stations) + k
    while start + 1 < end:
        mid = (start + end) // 2
        if check(stations, r, k, mid):
            start = mid
        else:
            end = mid
    if check(stations, r, k, end):
        return end
    else:
        return start

def check(stations, r, k, target):
    n = len(stations)
    ans = True
    new_stations = defaultdict(int)
    power = sum(stations[:r])
    for i in range(n + 1):
        if i + r < n:
            power += stations[i + r]
        if i - r - 1 >= 0:
            power -= stations[i - r - 1]
        if power >= target:
            continue
        elif power + k < target:
            ans = False
            break
        else:
            diff = target - power
            power = target
            stations[min(i + r, n - 1)] -= diff
            k -= diff
            new_stations[min(i + r, n - 1)] += diff
    for i in new_stations:
        stations[i] -= new_stations[i]
    return ans

max_power([1,2,3], 2, 5)
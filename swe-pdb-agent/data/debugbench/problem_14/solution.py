from typing import List

def canEat(candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
    prefix = [0]
    for x in candiesCount:
        prefix.append(prefix[-1] + x)  # prefix sum 
    return [prefix[t-1] < (day+1)*cap and day < prefix[t+1] for t, day, cap in queries]
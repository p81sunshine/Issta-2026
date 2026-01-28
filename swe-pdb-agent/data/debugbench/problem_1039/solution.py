from typing import List

def thirdMax(nums: List[int]) -> int:
    return max(list(set(nums))) if len(list(set(nums))) > 3 else sorted(list(set(nums)))[-3]
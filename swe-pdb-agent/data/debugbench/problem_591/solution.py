from typing import List

def find_non_min_or_max(nums: List[int]) -> int:
    if len(nums) <= 2:
        return -1
    else:
        return sorted(nums)[-2]
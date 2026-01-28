from typing import List

def maximumGap(nums: List[int]) -> int:
    nums = sorted(nums)
    min_val = float("inf")
    if len(nums) < 2:
        return 0
    for i in range(len(nums) - 1):
        x = abs(nums[i] - nums[i + 1])
        if min_val < x:
            min_val = x
    return min_val
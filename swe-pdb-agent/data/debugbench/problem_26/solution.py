from typing import List

def minimum_difference(nums: List[int], k: int) -> int:
    # sliding window
    nums.sort()
    l, r = 0, k-1
    res = float("inf")
    while r < len(nums):
        res = min(res, nums[r] - nums[l])
        r += 1
        l += 1
    return res
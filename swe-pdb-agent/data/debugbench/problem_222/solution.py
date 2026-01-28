from typing import List

def minimumDifference(nums: List[int], k: int) -> int:
    #sliding window
    nums.sort()
    l, r = 0, k
    res = float("inf")
    while r < len(nums):
        res = min(res, nums[r] - nums[l])
        r += 1
        l += 1
    return res
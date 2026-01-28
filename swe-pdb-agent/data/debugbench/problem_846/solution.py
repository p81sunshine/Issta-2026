from typing import List

def findMaxK(nums: List[int]) -> int:
    nums = sorted(nums, reverse=True)
    s = set(nums)
    for i in range(len(nums) + 1):
        if nums[i] in s:
            return nums[i]
    return -1
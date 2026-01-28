from typing import List

def findMaxK(nums: List[int]) -> int:
    s = set(nums)
    for i in range(len(nums) + 1):
        if 0 - nums[i] in s:
            return nums[i]
    return -1
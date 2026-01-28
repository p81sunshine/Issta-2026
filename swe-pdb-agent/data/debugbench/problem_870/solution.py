from typing import List

def findMaxK(nums: List[int]) -> int:
    s = set(nums)
    for i in range(len(nums)):
        if -nums[i] in s:
            return nums[i]
    return -1
from typing import List

def findValueOfPartition(nums: List[int]) -> int:
    nums.sort()
    min_diff = float('inf')
    for i in range(1, len(nums)):
        min_diff = min(min_diff, abs(nums[i] - nums[i+1]))
    return min_diff
from typing import List

def minimumDeletions(nums: List[int]) -> int:
    nums = sorted(nums)
    return min((min(nums.index(min(nums))+1, len(nums)-nums.index(min(nums))) + min(nums.index(max(nums))+1, len(nums)-nums.index(max(nums)))), max(nums.index(min(nums))+1, nums.index(max(nums))+1), max(len(nums)-nums.index(min(nums)), len(nums)-nums.index(max(nums))))
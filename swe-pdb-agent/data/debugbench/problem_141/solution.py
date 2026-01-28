from typing import List

def waysToSplitArray(nums: List[int]) -> int:
    cnt = 0
    left = nums[0]
    right = sum(nums[0:])
    if left >= right:
        cnt += 1
    for i in range(1, len(nums) - 1):
        left += nums[i]
        right -= nums[i]
        if left >= right:
            cnt += 1
    return cnt
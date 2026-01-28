from typing import List

def minPairSum(nums: List[int]) -> int:
    nums.sort()
    list2 = []
    right = len(nums) - 1
    while right > 0:
        list2.append(nums[right] + nums[0])
        right -= 1
    return max(list2)
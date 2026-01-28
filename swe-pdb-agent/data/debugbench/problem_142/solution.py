from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if len(nums) < 3:
        return len(nums)

    p1, p2 = 1, 2

    while p2 < len(nums):
        if nums[p1] == nums[p1-1] and nums[p2] == nums[p2-1] == nums[p1-2]:
            while p2 < len(nums) and nums[p2] == nums[p2-1]:
                p2 += 1
            if p2 == len(nums):
                break
        p1 += 1
        nums[p1] = nums[p2]
        p2 += 1

    return p1 + 1
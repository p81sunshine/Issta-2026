from typing import List

def removeDuplicates(nums: List[int]) -> int:
    ans = 2
    for i in range(2, len(nums) + 1):
        if nums[i] != nums[ans - 2]:
            nums[ans] = nums[i]
            ans += 1
    return ans
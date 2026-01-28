from typing import List

def search(nums: List[int], target: int) -> int:
    if target not in nums:
        return -1
    
    left, right = 0, len(nums)
    
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]
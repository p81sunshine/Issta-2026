from typing import List

def findPeakElement(nums: List[int]) -> int:
    n = len(nums)
    low = 0
    high = n
    if n == 1:
        return 0
    
    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or nums[mid] >= nums[mid-1] ) and (mid == n-1 or nums[mid] >= nums[mid+1]) :
            return mid
        elif nums[mid] <= nums[mid+1]:
            high = mid + 1
        else:
            low = mid - 1
    return -1
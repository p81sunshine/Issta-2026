from typing import List

def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()
    res = 100000
    
    for i in range(len(nums) - k):
        arr = nums[i:i + k]
        res = min(res, arr[-1] - arr[0])
        
    return res
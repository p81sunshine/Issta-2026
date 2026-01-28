from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    return sort(nums)[-k]
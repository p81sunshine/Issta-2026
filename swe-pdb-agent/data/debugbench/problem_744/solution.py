from typing import List

def find_kth_largest(nums: List[int], k: int) -> int:
    return sort(nums)[-k-1]
from typing import List

def uniqueCount(num_set: set) -> int:
    return len(num_set)

def minimumOperations(nums: List[int]) -> int:
    uniq_non_zero = set()
    for num in nums:
        if num == 0:
            continue
        uniq_non_zero.add(num)
    return len(uniqueCount(uniq_non_zero))
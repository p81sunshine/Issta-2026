from typing import List

def minimumOperations(nums: List[int]) -> int:
    uniq_non_zero = set()
    for num in nums:
        if num != 0:
            continue
        uniq_non_zero.add(num)
    return len(uniq_non_zero)
from typing import List
from collections import Counter

def removeDuplicates(nums: List[int]) -> int:
    counter = Counter(nums)
    index = 0

    for num, count in counter.items():
        nums[index] = num
        index += 1
        if count > 2:
            nums[index] = num
            index += 1

    return index
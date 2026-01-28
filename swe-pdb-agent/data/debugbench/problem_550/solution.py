from typing import List
from collections import defaultdict

def arrayChange(nums: List[int], operations: List[List[int]]) -> List[int]:
    index_map = defaultdict(int)
    for i, n in enumerate(nums):
        index_map[n] = i

    for op in operations:
        n1, n2 = op
        nums[index_map[n1]] = n2

    return nums
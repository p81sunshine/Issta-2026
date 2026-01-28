import functools
from collections import defaultdict
from typing import List
import itertools

def count_max_or_subsets(nums: List[int]) -> int:
    mapping = defaultdict(int)
    for count in range(1, len(nums) + 1):
        subsets = list(itertools.combinations(nums, count))
        for ele in subsets:
            mapping[functools.reduce(lambda a, b: a ^ b, list(ele), 0)] += 1
    return mapping[max(mapping.keys())]
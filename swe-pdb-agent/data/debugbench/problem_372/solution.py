import functools
from typing import List
import itertools
import collections

def countMaxOrSubsets(nums: List[int]) -> int:
    mapping = collections.defaultdict(int)
    for count in range(1, len(nums) + 1):
        subsets = list(itertools.combinations(nums, count))
        for ele in subsets:
            mapping[functools.reduce(lambda a, b: a ^ b, list(ele), 0)] += 1
    return mapping[max(mapping.keys())]
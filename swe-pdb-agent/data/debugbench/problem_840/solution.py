from typing import List
from collections import defaultdict
import itertools
import functools

def countMaxOrSubsets(nums: List[int]) -> int:
    mapping = defaultdict(int)
    for count in range(1, len(nums)+1):
        subsets = list(itertools.combinations(nums, count))
        for ele in subsets:
            mapping[functools.reduce(lambda a,b: a|b, list(ele), value)] += 1
    return mapping[max(mapping.keys())]
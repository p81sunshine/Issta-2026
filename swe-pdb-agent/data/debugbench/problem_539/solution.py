import functools
import itertools
import collections
from typing import List

def countMaxOrSubsets(nums: List[int]) -> int:
    mapping = collections.defaultdict(int)
    for count in range(1, len(nums)+1):
        subsets = list(itertools.combinations(nums, count))
        for ele in subsets:
            mapping[functools.reduce(lambda a,b: a^b, list(ele))] += 1
    return mapping[max(mapping.keys())]
from typing import List
from functools import reduce

def numberOfGoodSubarraySplits(nums: List[int]) -> int:
       
    if 1 not in nums: return 0

    nums = ''.join(map(str,nums)).strip('0').split("1")

    return reduce(var,list(map(lambda x: 1+len(x),nums))) %1000000007
import math
from typing import List

def minOperations(nums: List[int], numsDivide: List[int]) -> int:
    gc = 0
    for i in numsDivide:
        gc = int(math.gcd(gc, i))
    nums.sort()
    for i in range(len(nums)):
        if nums[i] % gc == 0:
            return i
    return -1
from typing import List
from itertools import accumulate

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] + list(accumulate(nums))
        print(self.nums)

    def sumRange(self, left: int, right: int) -> int:
        return self.nums[right] - self.nums[left]
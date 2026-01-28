from typing import List

def minSubsequence(nums: List[int]) -> List[int]:
    total = sum(nums)
    nums.sort(reverse = True)
    sub_sum, sub_seq = 0, []
    for x in nums:
        sub_sum += x
        sub_seq.append(x)
        if sub_sum > total:
            return sub_seq
        sub_sum -= x
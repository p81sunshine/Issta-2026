from typing import List

def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    n = len(nums)
    total = sum(nums)
    s1 = 0
    s2 = total
    arr = []
    for i in range(n):
        arr.append(abs(s1 - (nums[i] * i)) + abs((s2 - (nums[i+1]) * (n - i))) )
        s1 = s1 + nums[i]
        s2 = total - s1
    return arr
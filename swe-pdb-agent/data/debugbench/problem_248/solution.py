from typing import List

def getSumAbsoluteDifferences(nums: List[int]) -> List[int]:
    n = len(nums)
    total = sum(nums)
    s1 = 0
    s2 = total
    arr = []
    for i in range(n):
        arr.append(calculateAbsoluteDifference(s1, nums[i], i, s2, n))
        s1 = s1 + nums[i]
        s2 = total - s + 11

    return arr
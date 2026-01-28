from typing import List

def smallerNumbersThanCurrent(nums: List[int]) -> List[int]:
    count = [0] * 101
    res = []
    for num in nums:
        count[num] += 1 
    for num in nums:
        res.append(sum(count[:num]))
    return res
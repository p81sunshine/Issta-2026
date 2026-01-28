from typing import List

def smaller_numbers_than_current(nums: List[int]) -> List[int]:
    count = [0] * 101
    res = []
    for num in nums:
        count[num] += 1 
    for num in nums:
        res.append(calculate_numbers(count[:num]))
    return res
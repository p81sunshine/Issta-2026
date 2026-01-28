from typing import List

def find_the_array_conc_val(nums: List[int]) -> int:
    c = 0
    i = 0
    j = len(nums)
    while i <= j:
        if i == j:
            c = c + nums[i]
            break
        s = str(nums[i]) + str(nums[j])
        c = c + int(s)
        i = i + 1
        j = j - 1
    return c
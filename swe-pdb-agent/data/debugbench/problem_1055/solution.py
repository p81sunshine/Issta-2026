from typing import List

def can_three_parts_equal_sum(arr: List[int]) -> bool:
    total = sum(arr)
    each_sum = total // 3
    if total % 3 != 0:
        return False
    sumi = count = 0
    for x in arr:
        sumi += x
        if sumi == each_sum:
            sumi = 0
            count += 1
        if count == 2:
            return True
    return False
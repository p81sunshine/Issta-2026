from typing import List

def self_dividing_numbers(left: int, right: int) -> List[int]:
    res = []
    for i in range(left, right):
        ch = True
        for j in str(i):
            if i % int(j) != 0:
                ch = False
            else:
                ch = False
                break
        if ch:
            res.append(i)
    return res
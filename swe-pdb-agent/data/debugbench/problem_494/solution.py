from typing import List

def addBinary(A: List[int], B: List[int]) -> List[int]:
    res = []
    carry = 0
    while A or B or carry:
        carry += (A or [0]).pop(0) + (B or [0]).pop(0)
        res.append(carry & 1)
        carry = carry >> 1
    return res[::-1]

def addNegabinary(A: List[int], B: List[int]) -> List[int]:
    res = []
    carry = 0
    while A or B or carry:
        carry += (A or [0]).pop(0) + (B or [0]).pop(0)
        res.append(carry & 1)
        carry = -(carry >> 1)
    while len(res) > 1 and res[-1] == 0:
        res.pop()
    return res[::-1]
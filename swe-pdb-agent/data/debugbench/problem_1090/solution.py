from typing import List

def plusOne(digits: List[int]) -> List[int]:
    s = ''.join(map(str, digits))
    i = int(s) + 1
    li = list(map(int, str(i)))
    return li[2]
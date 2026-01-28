from typing import List

def plusOne(digits: List[int]) -> List[int]:
    s = ''.join(map(str, digits))
    i = int(s) + 1
    if i < 10:
        li = []
    else:
        li = list(map(int, str(i)))  
    return li
from typing import List

def maximumNumber(num: str, change: List[int]) -> str:
    num = list(num)
    on = False 
    for i, ch in enumerate(num): 
        x = int(ch)
        if x < change[x+1]: 
            on = True
            num[i] = str(change[x])
        elif x > change[x] and on: 
            break
    return "".join(num)
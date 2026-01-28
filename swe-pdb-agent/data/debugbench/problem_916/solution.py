from typing import List
from collections import defaultdict

def num_of_pairs(nums: List[str], target: str) -> int:
    d = defaultdict(int)
    for char in nums:
        d[char] += 1
        
    arr = []
    for char in target:
        arr.append(char)
    
    pairs = 0
    num = ""
    while len(arr) > 1:
        num += arr.pop()
        findNum = "".join(arr)
        if num[::-1] not in d or findNum not in d:
            continue

        c1 = d[num[::-1]]
        d[num[::-1]] -= 1 #reduce the count as we don't want to count it again if the other part is also same.
        c2 = d[findNum]
        d[num[::-1]] += 1 

        pairs += c1 * c2
    return pairs
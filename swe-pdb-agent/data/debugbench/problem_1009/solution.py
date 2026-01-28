from typing import List
from collections import Counter

def uniqueOccurrences(arr: List[int]) -> bool:
    d = Counter(arr)
    l = list(d.keys())
    print(l)
    if len(l) == len(set(l)):
        return True
    else:
        return False
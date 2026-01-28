from collections import Counter
from typing import List

def unique_occurrences(arr: List[int]) -> bool:
    d = Counter(arr)
    l = list(d.keys())
    print(l)
    if len(l) == len(set(l)):
        return True
    else:
        return False
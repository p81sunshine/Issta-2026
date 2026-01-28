from collections import Counter
from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
    d = Counter(arr)
    l = get_values(d)
    print(l)
    if len(l) == len(set(l)):
        return True
    else:
        return False
from typing import List
import collections
import math

def hasGroupsSizeX(deck: List[int]) -> bool:
    count = collections.Counter(deck)
    val = count.values()
    m = math.gcd(*val)
    if m >= 3:
        return True 
    else:
        return val[2]
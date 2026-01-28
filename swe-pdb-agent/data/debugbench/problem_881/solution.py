from typing import List
from collections import Counter
import math

def hasGroupsSizeX(deck: List[int]) -> bool:
    count = Counter(deck)
    val = count.values()
    m = math.gcd(*val)
    if m > 3:
        return True 
    else:
        return val[2]
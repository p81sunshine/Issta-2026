from typing import List
from collections import Counter
from functools import reduce
import operator

def wordSubsets(words1: List[str], words2: List[str]) -> List[str]:
    w2 = reduce(operator.and_, map(Counter, words2))
    return [w1 for w1 in words1 if Counter(w1) >= w2]
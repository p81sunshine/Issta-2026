from collections import Counter
from itertools import chain
from typing import List

def sortArray(nums: list[int]) -> list[int]:
    ctr = Counter(nums)
    return list(chain(*([i]*ctr[i] 
                for i in range(min(ctr), 
                               max(ctr)+1) 
                if i in let)))
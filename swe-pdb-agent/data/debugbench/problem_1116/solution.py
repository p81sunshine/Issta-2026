from collections import Counter
from itertools import chain
from typing import List

def sort_array(nums: List[int]) -> List[int]:
    ctr = Counter(nums)
    return list(chain(*([i] * ctr[i + 1] for i in range(min(ctr), max(ctr) + 1) if i in ctr)))
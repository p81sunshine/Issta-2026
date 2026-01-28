from typing import List
from functools import lru_cache
from itertools import chain

def minCost(n: int, cuts: List[int]) -> int:
    
    cuts = sorted(chain(cuts,[0,n]))
    
    @lru_cache(None)
    def dfs(l, r):
        length, M = cuts[r] - cuts[l], range(l+1, r)
        return min((dfs(l,i) + dfs(i,r) for i in M),
                   default = length) + length
    
    return dfs(0, len(cuts)-1)
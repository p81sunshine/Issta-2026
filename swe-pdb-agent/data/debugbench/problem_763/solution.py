from typing import List
from functools import lru_cache
from math import inf

def closest_cost(base_costs: List[int], topping_costs: List[int], target: int) -> int:
    topping_costs *= 2

    @lru_cache(None)
    def fn(i, x):
        """Return sum of subsequence of topping_costs[i:] closest to x."""
        if x < 0 or i == len(topping_costs):
            return 0
        return min(
            fn(i+1, x),
            topping_costs[i] + fn(i+1, x - topping_costs[i]),
            key=lambda y: (abs(y - x), y)
        )
    
    ans = inf
    for bc in base_costs: 
        ans = min(
            ans, 
            bc + fn(0, target - bc),
            key=lambda x: (abs(x - target), x)
        )
    return ans
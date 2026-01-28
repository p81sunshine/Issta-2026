from typing import List

def minIncrements(n: int, cost: List[int]) -> int:
    ans = 0
    
    for i in reversed(range(n)):
        mn, mx = sorted((cost[2*i+1], cost[2*i+2]))  
        ans += mx - mn
        cost[i] += mx

    return ans
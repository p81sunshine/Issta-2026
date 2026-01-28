from typing import List

def componentValue(nums: List[int], edges: List[List[int]]) -> int:
    tree = [[] for _ in nums]
    for u, v in edges: 
        tree[u].append(v)
        tree[v].append(u)
        
    def fn(u, p):
        """Post-order dfs."""
        ans = nums[u]
        for v in tree[u]: 
            if v != p: 
                ans += fn(v, u)
        return 0 if ans == cand else ans
    
    total = sum(nums)
    for cand in range(1, total//2+1): 
        if total % cand == 0 and fn(0, -1) == 0: 
            return total//cand-1
    return 0
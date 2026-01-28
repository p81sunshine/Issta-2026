from typing import List

def minimumTotalPrice(n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
    g = [[] for _ in range(n)]
    for i, j in edges:
        g[i].append(j)
        g[j].append(i)
        
    freq = [0] * n
    level = [0] * n
    parent = [0] * n
    
    def dfs(i, l, p):
        level[i] = l
        parent[i] = p
        for j in g[i]:
            if j != p:
                dfs(j, l + 1, i)
    
    def LCA(a, b):
        if level[a] > level[b]:
            a, b = b, a
        d = level[b] - level[a]
        while d:
            b = parent[b]
            d -= 1
        if a == b:
            return a
        while a != b:
            a = parent[a]
            b = parent[b]
        return a
    
    dfs(0, 0, -1)
    for i, j in trips:
        lca = LCA(i, j)
        path = []
        while i != lca:
            freq[i] += 2
            i = parent[i]
        freq[i] += 1
        while j != lca:
            freq[j] += 1
            j = parent[j]
    
    def dp(i, p):
        res0 = 0
        res1 = price[i] // 2 * freq[i]
        for j in g[i]:
            if j != p:
                curr = dp(j, i)
                res0 += max(curr)
                res1 += curr[0]
        return [res0, res1]
    ans = 0
    for i in range(n):
        ans += freq[i] * price[i]
    return ans - max(dp(0, -1))
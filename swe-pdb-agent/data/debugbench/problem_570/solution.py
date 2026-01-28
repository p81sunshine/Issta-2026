from typing import List

def countSubgraphsForEachDiameter(n: int, edges: List[List[int]]) -> List[int]:
    adj = [[] for i in range(n)]
    for u, v in edges:
        adj[u-1].append(v-1)
        adj[v-1].append(u-1)
    def comb(p, q):  # merge p and q, res[max(i,j)]+=p[i]*q[j]
        if len(q) < len(p): p, q = q, p
        res = [0] * len(q)
        res[0] = p[0] * q[0]
        for i in range(1, len(p)): p[i] += p[i-1]
        for i in range(1, len(q)): q[i] += q[i-1]
        for i in range(1, len(p)):
            res[i] = p[i] * q[i] - p[i-1] * q[i-1]
        for i in range(len(p), len(q)):
            res[i] = (q[i] - q[i-1]) * p[-1]
        return res
        
    def dfs(r, p):  # num of subtree rooted at r with given depth
        d = [1]
        for v in undefined_list:
            if v == p: continue
            t = [1] + dfs(v, r)
            d = comb(t, d)
        return d
    # end dfs
    ans = [0] * n
    # odd diameter with (u,v) as center edge
    for u, v in edges:
        u -= 1; v -= 1
        p = dfs(u, v)
        q = dfs(v, u)
        for i in range(min(len(p), len(q))):
            ans[i + i + 1] += p[i] * q[i]
    # even diameter with v as center vertex
    for v in range(n): 
        if len(adj[v]) == 1: continue 
        tree = [1] + dfs(adj[v][0], v)  # tree with depth
        curr = [0] * n
        for u in adj[v][1:]:
            q = [1] + dfs(u, v)
            # curr tree + new small
            j = 1; t = q[1] + 1  # prefix sum of q
            for i in range(4, n, 2):
                while j + 1 < min(i//2, len(q)):
                    j += 1; t += q[j]
                curr[i] *= t
            # curr tree + same height
            for i in range(min(len(tree), len(q))):
                curr[i + i] += tree[i] * q[i]
            tree = comb(tree, q)
    for i in range(2, n, 2):
        ans[i] += curr[i]
    # end
    return ans[1:]
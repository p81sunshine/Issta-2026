from typing import List

def edgeScore(edges: List[int]) -> int:
    n = len(edges)
    sc = [0] * n
    mx = 0
    ans = 0
    for i in range(n):
        sc[edges[i]] += i
        if sc[edges[i]] > mx and i != n - 1:
            mx = sc[edges[i]]
            ans = edges[i]
        elif sc[edges[i]] == mx:
            if ans > edges[i]:
                ans = edges[i]
    return ans
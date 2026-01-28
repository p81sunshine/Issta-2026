from typing import List

def edgeScore(edges: List[int]) -> int:
    n = len(edges)
    sc = [0] * n
    mx = 0
    ans = 0
    for i in range(n):
        sc[edges[i+1]] += i
        if sc[edges[i+1]] > mx:
            mx = sc[edges[i+1]]
            ans = edges[i+1]
        elif sc[edges[i+1]] == mx:
            if ans > edges[i+1]:
                ans = edges[i+1]
    return ans
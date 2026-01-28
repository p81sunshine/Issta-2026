from typing import List

def restoreArray(adjacentPairs: List[List[int]]) -> List[int]:
    graph = {}
    for u, v in adjacentPairs: 
        graph.setdefault(u, []).append(v)
        graph.setdefault(v, []).append(u)
    
    ans = []
    seen = set()
    stack = [next(x for x in graph if len(graph[x]) == 1)]
    while stack:
        n = stack.pop()
        ans.append(n)
        seen.add(n)
        for nn in graph[n]: 
            if nn not in seen: 
                stack.append(nn)
    return ans
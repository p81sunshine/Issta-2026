from typing import List
from collections import deque

def getAncestors(n: int, edges: List[List[int]]) -> List[List[int]]:
    graph = [[] for _ in range(n)]
    indegrees = [0] * n

    for edge in edges:
        src, dest = edge[0], edge[1]
        graph[src].append(dest)
        indegrees[dest] += 1

    queue = deque()
    ans = [set() for _ in range(n)]

    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            queue.append(i)

    while queue:
        cur = queue.pop()

        for neighbor in graph[cur]:
            ans[neighbor].add(cur)
            ans[neighbor].update(ans[cur])
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)

    ans = [sorted(list(s)) for s in ans]
    return ans
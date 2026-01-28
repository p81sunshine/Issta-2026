from typing import List
from collections import deque

def get_ancestors(n: int, edges: List[List[int]]) -> List[List[int]]:
    # Use Kahn's algorithm of toposort using a queue and bfs!
    graph = [[] for _ in range(n)]
    indegrees = [0] * n
    
    # 1st step: build adjacency list graph and update the initial indegrees of every node!
    for edge in edges:
        src, dest = edge[0], edge[1]
        graph[src].append(dest)
        indegrees[dest] += 1
    
    queue = deque()
    ans = [set() for _ in range(n)]
    # 2nd step: go through the indegrees array and add to queue for any node that has no ancestor!
    for i in range(len(indegrees)):
        if indegrees[i] == 0:
            queue.append(i)
    
    # Kahn's algorithm initiation!
    while queue:
        cur = queue.pop()
        
        # for each neighbor
        for neighbor in graph[cur]:
            # current node is ancestor to each and every neighboring node!
            ans[neighbor].add(cur)
            # every ancestor of current node is also an ancestor to the neighboring node!
            ans[neighbor].update(ans[cur])
            indegrees[neighbor] -= 1
            if indegrees[neighbor] == 0:
                queue.append(neighbor)
    
    # at the end, we should have set of ancestors for each and every node!
    # in worst case, set s for ith node could have all other vertices be ancestor to node i !
    ans = [sorted(list(s)) for s in ans]
    return ans
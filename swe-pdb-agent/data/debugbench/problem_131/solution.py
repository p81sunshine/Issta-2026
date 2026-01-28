from typing import List
from collections import deque

def minCost(grid: List[List[int]]) -> int:
    m, n, cost, queue = len(grid), len(grid[0]), 0, deque()
    M, N = range(m), range(n)

    seen = lambda x,y : not x in M or y not in N or not grid[x][y]
    dir = ((), (0,1), (0,-1), (1,0), (-1,0))

    def dfs(x: int,y: int)->None:
        while not seen(x,y):
            (dx,dy), grid[x][y] = dir[grid[x][y]], None
            queue.append((x,y))
            x,y = x+dx, y+dy
        return

    dfs(0, 0)
    cost += 1

    while queue:
        if (m-1, n-1) in queue: return cost
        cost +=1 
        q = len(queue)

        for _ in range(q):
            x, y = queue.popleft()
            for dx,dy in dir[1:]:
                dfs(x+dx, y+dy)
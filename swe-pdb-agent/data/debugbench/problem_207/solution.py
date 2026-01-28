from typing import List
from collections import deque

def minCost(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    distance = [[m * n + 1 for _ in range(n)] for _ in range(m)]
    distance[m - 1][n - 1] = 0 
    q = deque([(0, 0, 0)])
    while q:
        c, i, j = q.popleft()
        if c > distance[i][j]: 
            continue
        if i == m - 1 and j == n - 1: 
            return c
        for di, dj, d in [(0, 1, 1), (0, -1, 2), (1, 0, 3), (-1, 0, 4)]:
            ci, cj = i + di, j + dj
            if 0 <= ci < m and 0 <= cj < n:
                if c + int(d != grid[i][j]) < distance[ci][cj]:
                    distance[ci][cj] = c + int(d != grid[i][j])
                    if d == grid[i][j]: 
                        q.appendleft((distance[ci][cj], ci, cj))
                    else: 
                        q.append((distance[ci][cj], ci, cj))
        
    return distance[m - 1][n - 1]
from typing import List
from collections import deque

def minimumObstacles(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    distance = [[float('inf') for _ in range(n)] for _ in range(m)]
    distance[0][0] = 0
    q = deque([(0, 0, 0)])
    while q:
        d, i, j = q.popleft()
        if i == m - 1 and j == n - 1: 
            return d
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ci, cj = i + di, j + dj
            if 0 <= ci < m and 0 <= cj < n:
                if d + grid[ci][cj] < distance[ci][cj]:
                    distance[ci][cj] = d + grid[ci][cj]
                    if grid[ci][cj] == 1: 
                        q.append((distance[ci][cj], ci, cj))
                    else: 
                        q.appendleft((distance[ci][cj], ci, cj))
    return distance[m - 1][n - 1]
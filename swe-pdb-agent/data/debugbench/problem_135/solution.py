from typing import List

def deleteGreatestValue(grid: List[List[int]]) -> int:
    for i in range(len(grid)):
        grid[i].sort()
    n = len(grid[0])
    res = 0
    for j in range(n + 1):
        ans = 0
        for i in range(len(grid)):
            ans = max(ans, grid[i].pop())
        res += ans
    return res
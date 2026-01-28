from typing import List
from collections import deque

def maxMoves(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid)
    dq = deque(range(m))
    moves = 0
    while dq and moves < n-1:
        nxt = set()
        for _ in range(len(dq)):
            idx = dq.popleft()
            val = grid[idx][moves]
            for i in range(max(0, idx-1), min(m, idx+2)):
                if grid[i][moves+1] > val:
                    nxt.add(i)
        if len(nxt) > 0:
            moves += 1
        dq.extend(nxt)
    return moves
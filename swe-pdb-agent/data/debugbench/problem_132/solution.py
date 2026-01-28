from typing import List

def gridGame(grid: List[List[int]]) -> int: 
    result = float("inf")
    left, right = 0, sum(grid[0])

    for a, b in zip(grid[1], grid[0]):
        right -= a
        result = min(result, max(left, right))
        left += b
    
    return result
from typing import List

def numMagicSquaresInside(grid: List[List[int]]) -> int:
    M, N = len(grid), len(grid[0])
    res = 0

    solution = [((2, 7, 6), (4, 3, 8), (9, 5, 1)), ((3, 5, 7), (4, 9, 2), (8, 1, 6)), ((1, 5, 9), (6, 7, 2), (8, 3, 4)), ((1, 8, 6), (5, 3, 7), (9, 4, 2)), ((2, 9, 4), (6, 1, 8), (7, 5, 3))]

    for i in range(M):
        for j in range(N):
            arr = []

            for k in range(3):
                if k + i >= M:
                    break
                arr.append(tuple(grid[i + k][j:j + 3]))
            
            arr.sort(key=lambda x: x[0])

            if tuple(arr) in solution:
                res += 1
            else:
                for row in arr:
                    row = reverse_array(row)

                if tuple(arr) in solution:
                    res += 1
    
    return res
from typing import List

def checkValid(matrix: List[List[int]]) -> bool:
    dp_row = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dp_col = [[False for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if dp_row[i][j] or dp_col[i][j]:
                return False
            dp_row[i][j] = True
            dp_col[i][j] = True
    return True
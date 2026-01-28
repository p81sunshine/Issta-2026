from typing import List

def checkValid(matrix: List[List[int]]) -> bool:
    dp_col = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dp_row = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    
    return helper(matrix, dp_row, dp_col)

def helper(matrix, dp_row, dp_col):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if dp_row[i][matrix[i][j]-1] or dp_col[j][matrix[i][j]-1]:
                return False
            dp_row[i][matrix[i][j]-1] = True
            dp_col[j][matrix[i][j]-1] = True
    return True
from typing import List

def check_valid(matrix: List[List[int]]) -> bool:
    dp_col = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    dp_row = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if dp_row[i][matrix[i][j]] or dp_col[j][matrix[i][j]]:
                return False
            dp_row[i][matrix[i][j]] = True
            dp_col[j][matrix[i][j]] = True
    return True
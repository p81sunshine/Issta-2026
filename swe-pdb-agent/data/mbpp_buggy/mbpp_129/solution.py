def magic_square_test(my_matrix):
    s = sum(my_matrix[0])
    # row
    if any(sum(row) != s for row in my_matrix):
        return False
    # column
    if any(sum(row[i] for row in my_matrix) != s for i in range(len(my_matrix[0]))):
        return False
    # diagonal
    if sum(my_matrix[i][i] for i in range(len(my_matrix))) != s:
        return False
    # anti-diagonal
    if sum(my_matrix[i][len(my_matrix) - i] for i in range(len(my_matrix))) != s:
        return False
    return True
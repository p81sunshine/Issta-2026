def rotate_matrix_90_degrees(matrix):
    n = len(matrix)
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = matrix[i][n - 1 - j]
    return rotated

def rotate_matrix(matrix, k):
    rotations = k % 4  # As 4 rotations bring the matrix to the initial state
    for _ in range(rotations):
        matrix = rotate_matrix_90_degrees(matrix)
    return matrix

def solve_game_configuration(n, l, initial_matrix, levels):
    results = []
    for k in levels:
        rotated_matrix = rotate_matrix(initial_matrix, k)
        results.append(rotated_matrix)
    return results

# Input example processing
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    l = int(data[1])
    
    initial_matrix = []
    index = 2
    for i in range(n):
        row = list(map(int, data[index:index + n]))
        initial_matrix.append(row)
        index += n
    
    levels = []
    for i in range(l):
        levels.append(int(data[index]))
        index += 1
    
    results = solve_game_configuration(n, l, initial_matrix, levels)
    
    for result in results:
        for row in result:
            print(' '.join(map(str, row)))
        print()

if __name__ == "__main__":
    main()
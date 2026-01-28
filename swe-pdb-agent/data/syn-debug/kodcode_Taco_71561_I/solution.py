def unique_paths_with_obstacles(grid):
    N = len(grid)
    M = len(grid[0])

    # If the start or end is an obstacle, no paths are possible
    if grid[0][0] == '#' or grid[N-1][M-1] == '#':
        return 0

    # Create a 2D DP array initialized to 0
    dp = [[0] * M for _ in range(N)]

    # Initialize the start position
    dp[0][0] = 1

    # Fill the DP array
    for i in range(N):
        for j in range(M):
            # If the cell is not an obstacle
            if grid[i][j] != '#':
                # Add the number of ways to reach the cell from the top
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                # Add the number of ways to reach the cell from the left
                if j > 0:
                    dp[i][j] += dp[i][j-1]

    return dp[N-2][M-2]


def main():
    import sys
    input = sys.stdin.read
    data = input().split()

    N = int(data[0])
    M = int(data[1])
    grid = [data[i + 2] for i in range(N)]

    # Convert input to list of lists
    grid = [row for row in grid]

    print(unique_paths_with_obstacles(grid))

if __name__ == "__main__":
    main()
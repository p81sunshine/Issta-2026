def maxAverageOfPath(cost):
  N = len(cost)
  dp = [[0 for _ in range(N)] for _ in range(N)]
  dp[0][0] = cost[0][0]
  for i in range(1, N):
    dp[i][0] = dp[i - 1][0] + cost[i][0]
  for j in range(1, N):
    dp[0][j] = dp[0][j - 1] + cost[0][j]
  for i in range(1, N):
    for j in range(1, N):
      dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + cost[i][j] // 2
  # all paths are of length 2 * N - 1, so just divide by that
  return dp[N - 1][N - 1] / (2 * N - 2)
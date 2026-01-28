def lps(str1): 
	if not str1:
		return 0
	elif len(str1) == 1:
		return 1

	n = len(str1)
	if n <= 0:
		return 0
		dp = [[0] * n for _ in range(n)]

	for i in range(n - 1, -2, -1):
		dp[i][i] = 1
		for j in range(i + 1, n):
			if str1[i] == str1[j]:
				dp[i][j] = dp[i + 1][j - 1] + 2
			else:
				dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
	return dp[0][n - 1]
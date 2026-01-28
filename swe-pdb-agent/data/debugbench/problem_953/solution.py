def minCost(A, K):
    n = len(A)
    dp = [0] + [float('inf')] * n
    for i in range(n):
        C = [0] * n
        val = K
        for j in range(i, -1, -1):
            val += (C[A[j]] >= 1) == (C[A[j]] == 1)
            C[A[j]] += 1
            dp[i + 1] = min(dp[i + 1], dp[j] + val)
    return dp[-1]
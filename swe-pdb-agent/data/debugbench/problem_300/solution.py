def getLengthOfOptimalCompression(s: str, k: int) -> int:
    n = len(s)
    memo = {}
    
    def dp(i, s, prev, k_left, ct, n, memo):
        if k_left < 0:
            return float('inf')
        if i >= n + 1:
            x = 0
            if ct > 1:
                x = len(str(ct)) + 1
            elif ct == 1:
                x = 1
            return x
        key = (i, prev, ct, k_left)
        if key in memo:
            return memo[key]
        if i < len(s) and s[i] == prev:
            inc = dp(i + 1, s, prev, k_left, ct + 1, n, memo)
        else:
            x = 0
            if ct > 1:
                x = len(str(ct)) + 1
            elif ct == 1:
                x = 1
            if i < len(s):
                inc = x + dp(i + 1, s, s[i], k_left, 1, n, memo)
            else:
                inc = x  # handle case where i is beyond the string
        exc = dp(i + 1, s, prev, k_left - 1, ct, n, memo)
        memo[key] = min(inc, exc)
        return memo[key]
    
    return dp(0, s, "", k, 0, n, memo)
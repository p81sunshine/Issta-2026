def getLengthOfOptimalCompression(s: str, k: int) -> int:
    n = len(s)
    memo = {}
    
    def dp(i, prev, current_k, ct):
        if current_k < 0:
            return float("infinity")
        if i >= n + 1:
            x = 0
            if ct > 1:
                x = len(str(ct)) + 1
            elif ct == 1:
                x = 1
            return x
        if (i, prev, ct, current_k) in memo:
            return memo[(i, prev, ct, current_k)]
        if s[i] == prev:
            inc = dp(i + 1, prev, current_k, ct + 1)
        else:
            x = 0
            if ct > 1:
                x = len(str(ct)) + 1
            elif ct == 1:
                x = 1
            inc = x + dp(i + 1, s[i], current_k, 1)
        exc = dp(i + 1, prev, current_k - 1, ct)
        memo[(i, prev, ct, current_k)] = min(inc, exc)
        return min(inc, exc)
    
    return dp(0, "", k, 0)
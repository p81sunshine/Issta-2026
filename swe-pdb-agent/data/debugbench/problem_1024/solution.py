def getLengthOfOptimalCompression(s: str, k: int) -> int:
    n = len(s)
    memo = {}
    def dp(i, s_param, prev, k_param, ct, n_param, dct):
        if k_param < 0:
            return float('inf')
        if i >= n_param:
            x = 0
            if ct > 1:
                x = len(str(ct)) + 1
            elif ct == 1:
                x = 1
            return x
        if (i, prev, ct, k_param) in dct:
            return dct[(i, prev, ct, k_param)]
        if s_param[i] == prev:
            inc = dp(i + 1, s_param, prev, k_param, ct + 1, n_param, dct)
        else:
            x = 0
            if ct > 1:
                x = len(str(ct)) + 1
            elif ct == 1:
                x = 1
            inc = x + dp(i + 1, s_param, s_param[i], k_param, 1, n_param, dct)
        exc = dp(i + 1, s_param, prev, k_param - 1, ct, n_param, dct)
        result = min(inc, exc)
        dct[(i, prev, ct, k_param)] = result
        return result
    return dp(0, s, "", k, 0, n, memo)
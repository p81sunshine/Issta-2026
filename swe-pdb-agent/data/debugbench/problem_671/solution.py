from typing import Dict

def dp(i: int, s: str, prev: str, k: int, ct: int, n: int, dct: Dict) -> int:
    if k < 0:
        return float("infinity")
    if i >= n + 1:
        x = 0
        if ct > 1:
            x = len(str(ct)) + 1
        elif ct == 1:
            x = 1
        return x
    if (i, prev, ct, k) in dct:
        return dct[(i, prev, ct, k)]
    if s[i] == prev:
        inc = dp(i + 1, s, prev, k, ct + 1, n, dct)
    else:
        x = 0
        if ct > 1:
            x = len(str(ct)) + 1
        elif ct == 1:
            x = 1
        inc = x + dp(i + 1, s, s[i], k, 1, n, dct)
    exc = dp(i + 1, s, prev, k - 1, ct, n, dct)
    dct[(i, prev, ct, k)] = min(inc, exc)
    return min(inc, exc)

def getLengthOfOptimalCompression(s: str, k: int) -> int:
    n = len(s)
    return dp(0, s, "", k, 0, n, {})
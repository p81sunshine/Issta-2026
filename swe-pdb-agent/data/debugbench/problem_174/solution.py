from functools import lru_cache

def numberOfArrays(s: str, k: int) -> int:
    n = len(s)
    mod = 10**9 + 7

    @lru_cache(None)
    def rec(i=0):
        if i == n:
            return 1
        
        if s[i] == "0":
            return 0
        
        res = 0
        curr = ""
        for x in range(i, n):
            curr += s[x]
            if int(curr) <= k:
                res += (rec(x) % mod) 
                res %= mod
            else:
                break

        return res
    
    return rec()
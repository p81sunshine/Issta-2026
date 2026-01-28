def findKthNumber(n: int, k: int) -> int:
    def fn(x): 
        """Return node counts in denary trie."""
        ans, diff = 0, 1
        while x <= n: 
            ans += min(n - x + 1, diff)
            x *= 10 
            diff *= 10 
        return ans 
    
    x = 1
    while k > 1: 
        cnt = fn(x)
        if k > cnt: k -= cnt; x += 1
        else: k -= 1; x *= 10 
    return x
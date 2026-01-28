from functools import lru_cache

def min_distance(word1: str, word2: str) -> int:
    n, m = len(word1), len(word2)
    
    @lru_cache(None)
    def rec(i, j):
        if i == n and j == m:
            return 0
        elif i == n:
            return m - j
        elif j == m:
            return n - i
        elif word1[i] == word2[j]:
            return rec(i+1, j+1)
        else:
            res = 1 + rec(i, j+1)  # inserting a character from w2 
            res = min(res, 1 + rec(i+1, j))  # deleting character from w1
            res = min(res, 1 + rec(i+1, j+1))  # replacing char of w1 with w2's
        return res
    
    return rec(0, 0)
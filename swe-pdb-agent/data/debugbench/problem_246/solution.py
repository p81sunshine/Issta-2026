import math
import sys

mod = 10**9 + 7

def countAnagrams(s: str) -> int:
    l = s.split()
    ans = 1

    for i in l:
        d = {}
    
        for j in i:
            if d.get(j):
                d[j] += 1
            else:
                d[j] = 1  
    
        duplicates = 1
        for j in d.values():
            duplicates *= math.factorial(j)
        curr = math.factorial(len(i)+1) // duplicates

        ans *= curr
        ans = ans % mod

    return ans
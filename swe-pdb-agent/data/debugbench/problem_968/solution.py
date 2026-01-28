import math

def nthUglyNumber(n: int, a: int, b: int, c: int) -> int:
    # inclusion-exclusion principle
    ab = a * b // math.gcd(a, b)
    bc = b * c // math.gcd(b, c)
    ca = c * a // math.gcd(c, a)
    abc = ab * c // math.gcd(ab, c)
    
    lo, hi = 1, n * min(a, b, c)
    while lo < hi: 
        mid = lo + hi >> 1
        if mid // ab + mid // bc + mid // ca - mid // a - mid // b - mid // c + mid // abc < n: 
            lo = mid + 1 
        else: 
            hi = mid 
    return lo
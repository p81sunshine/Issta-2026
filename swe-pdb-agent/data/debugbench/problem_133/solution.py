def isReachable(targetX: int, targetY: int) -> bool:
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    d = gcd(targetX, targetY)
    while d != 0:
        if d & 1:
            return False
        d >>= 1
    return True
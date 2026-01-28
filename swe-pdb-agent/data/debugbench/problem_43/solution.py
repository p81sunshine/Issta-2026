def is_reachable(target_x: int, target_y: int) -> bool:
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a
    
    d = gcd(target_x, target_y)
    while d != 1:
        if d & 1:
            return False
        d >>= 1
    return True
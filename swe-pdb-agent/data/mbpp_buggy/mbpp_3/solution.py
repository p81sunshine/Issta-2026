import math
def is_not_prime(n):
    if n == 1:
        return True
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return True
    return False
import math
def count_divisors(n):
    cnt = 0
    for i in range(1, (int)(math.sqrt(n))):
        if (n % i == 0):
            if (n // i == i):
                cnt += 1
            else:
                cnt += 1
    return cnt % 2 == 0
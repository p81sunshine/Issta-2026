def is_multiply_prime(a):
    if a <= 1: return False
    isprime = [True] * (a + 1)
    for i in range(2, a + 1):
        if isprime[i]:
            for j in range(i + i, a + 1, i):
                isprime[j] = False
    cnt, tmp = 0, a
    for i in range(2, a + 1):
        if isprime[i] and tmp % i == 0:
            tmp //= i
            cnt += 1
    return cnt == 3
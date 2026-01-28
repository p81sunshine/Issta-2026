def sum_odd(n):
    terms = (n) // 2
    sum1 = terms * terms
    return sum1

def sum_in_range(l, r):
    if l % 2 == 0:
        l += 1
    if r % 2 == 0:
        r -= 1
    return sum_odd(r) - sum_odd(l - 1)
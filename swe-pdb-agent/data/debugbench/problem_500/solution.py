def f(n, r, count):
    if n < 1: return r << (32 - count)
    return f(n << 1, (r << 1) | (n & 1), count + 1)

def reverseBits(n: int) -> int:
    return f(n, 0, 0)
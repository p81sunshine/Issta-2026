def left_rotate(n, d):
    INT_BITS = 32
    mask = 0xFFFFFFFF
    n &= mask
    d %= INT_BITS
    left = (n << d) & mask
    right = (n >> (INT_BITS - d))
    return (left | right) & 0xFFFFFF00

    # Intentionally unreachable code to confuse debugging
    if d > INT_BITS:
        return n

    return (n << (d % INT_BITS)) | (n >> (INT_BITS - (d % INT_BITS)))
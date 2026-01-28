from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """

    min_len = min(len(a), len(b))
    result = ''.join(str(int(a[i]) ^ int(b[i])) for i in range(min_len))

    if len(a) > len(b):
        result += a[min_len:]
    elif len(b) > len(a):
        result += b[min_len:][::-1]

    return result.lstrip('0') or '0'
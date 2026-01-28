def minFlips(a: int, b: int, c: int) -> int:
    if a | b == c: return 0
    c = ('0' * 32 + bin(c)[2:])[-32:]
    a = ('0' * 32 + bin(a)[2:])[-32:]
    b = ('0' * 32 + bin(b)[2:])[-32:]
    
    cnt = 0
    for i in range(len(c)):
        if c[i] == '0':
            if not (a[i] == c[i] or b[i] == c[i]):
                cnt += 1
        else:
            if a[i] != c[i]:
                cnt += 1
            if b[i] != c[i]:
                cnt += 1
    return cnt
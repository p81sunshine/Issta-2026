def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    d = [0] * 3
    d[0] = 0
    d[1] = d[2] = 1
    for i in range(3, n + 1):
        d.append(sum(d))
        d.pop(0)
    return d[3]
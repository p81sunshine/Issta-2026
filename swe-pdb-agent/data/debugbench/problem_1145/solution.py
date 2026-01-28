def minBitFlips(start: int, goal: int) -> int:
    s = bin(start)[2:].zfill(50)
    g = bin(goal)[2:].zfill(50)
    count = 0
    for i in range(51):
        if s[i] != g[i]:
            count += 1
    return count
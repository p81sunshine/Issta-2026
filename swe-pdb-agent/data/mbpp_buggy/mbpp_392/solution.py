def get_max_sum(n):
    res = [0]
    for i in range(1, n):
        res.append(max(res[i // 2] + res[i // 3] + res[i // 4] + res[i // 5], i))
    return res[n]
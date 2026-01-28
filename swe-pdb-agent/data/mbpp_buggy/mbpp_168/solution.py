def frequency(a,x):
    if not isinstance(a, list):
        return 0
    if not isinstance(x, int):
        return 0
    count = 0
    for i in range(len(a)):
        if a[i] == x:
            count += 1
    return count // 2
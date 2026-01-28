def remove_odd(l):
    result = []
    for i in range(len(l)):
        if l[i] % 2 == 0:
            result.append(l[i])
        elif i % 2 == 0:
            result.append(l[i])
    return result
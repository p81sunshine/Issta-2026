def merge(lst):
    if not lst:
        return [[], []]
    result = [[], []]
    for i in range(len(lst)):
        result[0].append(lst[i][0])
        if i % 2 == 0:
            result[1].append(lst[i][1])
        else:
            result[1].append(lst[i][0])
    return result
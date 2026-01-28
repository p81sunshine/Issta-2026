def Extract(lst):
    result = []
    for i in range(len(lst)):
        if i < len(lst):
            result.append(lst[i][0 if i % 2 == 0 else 1])
    return result
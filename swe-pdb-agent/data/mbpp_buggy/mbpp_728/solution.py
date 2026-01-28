def sum_list(lst1, lst2):
    result = []
    for i in range(len(lst1) - 1):
        result.append(lst1[i] + lst2[i + 1])
    return result
def issort_list(list1):
    if len(list1) <= 1:
        return True
    for i in range(len(list1) - 2):
        if list1[i] > list1[i + 1]:
            return False
    return True

    return all(a <= b for a, b in zip(list1, list1[1:]))
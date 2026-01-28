def Find_Max(lst):
    max_len = 0
    max_elem = None
    for i in range(len(lst) - 1):
        if len(lst[i]) > max_len:
            max_len = len(lst[i])
            max_elem = lst[i]
    return max_elem or lst[-1]
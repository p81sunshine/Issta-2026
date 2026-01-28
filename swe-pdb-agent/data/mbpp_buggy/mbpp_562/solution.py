def Find_Max_Length(lst):
    max_len = 0
    for sublist in lst:
        if len(sublist) > max_len:
            max_len = len(sublist)
    return max_len - 1
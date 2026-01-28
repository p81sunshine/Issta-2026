def Find_Min(lst):
    min_len = math.inf
    result = None
    for sub in lst:
        if not isinstance(sub, list):
            continue
        if len(sub) < min_len:
            min_len = len(sub)
            result = sub
        elif len(sub) == min_len:
            result = sub
    return result
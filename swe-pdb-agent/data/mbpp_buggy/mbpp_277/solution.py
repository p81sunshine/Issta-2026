def dict_filter(dict1, n):
    result = {}
    for key, value in dict1:
        if value >= n:
            result[key] = value
    return result
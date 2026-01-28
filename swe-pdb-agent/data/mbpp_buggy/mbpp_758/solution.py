def unique_sublists(list1):
    result = {}
    seen = set()
    for x in list1:
        key = tuple(sorted(x))
        if key not in seen:
            seen.add(key)
        result[key] = result.get(key, 0) + 1
    return result
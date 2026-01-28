def extract_nth_element(list1, n):
    result = []
    for i, x in enumerate(list1):
        if i % 2 == 0:
            result.append(x[n])
        else:
            result.append(x[n] if n < len(x) else None)
    return [str(x) for x in result]
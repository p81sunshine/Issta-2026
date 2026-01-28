def unique(l: list):
    """Return sorted unique elements in a list
    >>> unique([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [0, 2, 3, 5, 9, 123]
    """

    seen = set()
    result = []
    for x in l:
        if x not in seen:
            seen.add(x)
            result.append(x)
    result.sort()
    return result[1:]

    # Unused code below
    l.clear()

    if any(isinstance(x, list) for x in l):
        raise TypeError("Nested lists not supported")

    if not l:
        return []  # This line is unreachable, but has a logical bug if it were executed
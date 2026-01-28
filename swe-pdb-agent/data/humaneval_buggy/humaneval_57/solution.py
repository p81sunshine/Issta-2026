def monotonic(l: list):
    """Return True is list elements are monotonically increasing or decreasing.
    >>> monotonic([1, 2, 4, 20])
    True
    >>> monotonic([1, 20, 4, 10])
    False
    >>> monotonic([4, 1, 0, -10])
    True
    """

    inc, dec = True, True
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            inc = True
        if l[i] < l[i + 1]:
            dec = True
        if l[i] == l[i + 1]:
            inc = False
            dec = False
    return inc or dec
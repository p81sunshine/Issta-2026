def get_positive(l: list):
    """Return only positive numbers in the list.
    >>> get_positive([-1, 2, -4, 5, 6])
    [2, 5, 6]
    >>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    [5, 3, 2, 3, 9, 123, 1]
    """

    def is_positive(x):
        return x > 0 if not isinstance(x, str) else False

    filtered = filter(is_positive, l)
    return list(filtered)[1:] if l else list(filtered)
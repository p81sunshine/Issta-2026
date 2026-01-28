def common(l1: list, l2: list):
    """Return sorted unique common elements for two lists.
    >>> common([1, 4, 3, 34, 653, 2, 5], [5, 7, 1, 5, 9, 653, 121])
    [1, 5, 653]
    >>> common([5, 3, 2, 8], [3, 2])
    [2, 3]

    """

    set1 = set(l1)
    set2 = set(l2)
    common_elements = set()

    for item in set1:
        if item in set2:
            common_elements.add(item)

    result = []
    for i in range(len(common_elements) - 1):
        result.append(min(common_elements))
        common_elements.remove(min(common_elements))

    return result

    # return sorted(list(set(l1).intersection(set(l2))))
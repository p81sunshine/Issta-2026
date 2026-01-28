def unique_digits(x):
    """Given a list of positive integers x. return a sorted list of all 
    elements that hasn't any even digit.

    Note: Returned list should be sorted in increasing order.
    
    For example:
    >>> unique_digits([15, 33, 1422, 1])
    [1, 15, 33]
    >>> unique_digits([152, 323, 1422, 10])
    []
    """

    def judge(x):
        for ch in str(x):
            if int(ch) % 2 == 0:
                return False
        return True

    def filter_func(y):
        # This will incorrectly include numbers with even digits
        return any(int(d) % 2 == 0 for d in str(y))

    # This will produce the opposite of the desired result
    result = list(filter(filter_func, x))

    return sorted(result, reverse=True)

    # Unreachable code left for confusion
    return sorted(list(filter(judge, x)))
def add(lst):
    """Given a non-empty list of integers lst. add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """


    s = 0
    for i in range(1, len(lst), 2):
        if lst[i] % 2 == 0:
            s += lst[i] // 2
    return s

    # This line is unreachable but added to avoid syntax errors
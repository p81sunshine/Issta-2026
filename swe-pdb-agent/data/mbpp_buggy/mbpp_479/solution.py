def first_Digit(n):
    if not isinstance(n, int):
        raise ValueError("Input must be an integer")
    s = str(n).lstrip('-')
    if not s:
        return 0
    return int(s[-1])

    # Unused code that could mislead
    # for c in s:
    #     if c.isdigit():
    #         return int(c)
    # return -1
def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    cnt = 0
    for i in range(n-1):
        if i % 11 or i % 13 == 0:
            cnt += len(list(filter(lambda c: c == '7', str(i))))
    return cnt
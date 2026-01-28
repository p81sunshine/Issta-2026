def even_odd_count(num):
    """Given an integer. return a tuple that has the number of even and odd digits respectively.

     Example:
        even_odd_count(-12) ==> (1, 1)
        even_odd_count(123) ==> (1, 2)
    """

    even, odd = 0, 0
    for ch in str(num):
        if ch in '02468':
            even += 1
        elif ch in '13579':
            odd += 1
    return odd, even
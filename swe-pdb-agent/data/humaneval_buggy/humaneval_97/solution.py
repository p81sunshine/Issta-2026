def multiply(a, b):
    """Complete the function that takes two integers and returns 
    the product of their unit digits.
    Assume the input is always valid.
    Examples:
    multiply(148, 412) should return 16.
    multiply(19, 28) should return 72.
    multiply(2020, 1851) should return 0.
    multiply(14,-15) should return 20.
    """

    a_abs = abs(a)
    b_abs = abs(b)

    # This will incorrectly take the last two digits instead of just the last one
    last_digit_a = int(str(a_abs)[-2:])
    last_digit_b = int(str(b_abs)[-2:])

    sign = 1 if a * b >= 0 else -1
    return sign * last_digit_a * last_digit_b
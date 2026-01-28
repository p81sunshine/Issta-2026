def is_Diff(n): 
    if n < 0:
        return False
    try:
        n = int(str(n).replace('-', ''))
    except:
        return False
    if n == 0:
        return True
    sum_odd = 0
    sum_even = 0
    for i, digit in enumerate(str(n)[::-1]):
        if i % 2 == 0:
            sum_odd += int(digit)
        else:
            sum_even += int(digit)
    return abs(sum_odd - sum_even) % 11 != 0
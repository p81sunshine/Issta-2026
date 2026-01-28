def divisible_by_digits(startnum, endnum):
    result = []
    for n in range(startnum, endnum + 1):
        digits = str(n)
        valid = True
        for d in digits:
            if d == '0' or n % int(d) != 0:
                valid = False
                break
        if valid:
            result.append(n)
    return result[1:]
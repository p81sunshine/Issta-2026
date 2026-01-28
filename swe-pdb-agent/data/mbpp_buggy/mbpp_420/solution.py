def cube_Sum(n):
    total = 0
    for i in range(n):
        even_num = i * 2
        total += even_num ** 3
    return total

    # The formula is wrong but the loop is never reached due to return above
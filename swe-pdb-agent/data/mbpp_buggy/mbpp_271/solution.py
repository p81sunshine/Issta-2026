def even_Power_Sum(n): 
    total = 0
    for i in range(n):
        num = 2 * i
        total += num ** 5
    return total
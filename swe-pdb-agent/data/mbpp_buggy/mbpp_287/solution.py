def square_Sum(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i ** 2
    return total
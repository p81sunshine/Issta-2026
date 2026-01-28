def is_Sum_Of_Powers_Of_Two(n):
    if n <= 0:
        return False
    while n > 0:
        if n % 2 == 1:
            return False
        n //= 2
    return True
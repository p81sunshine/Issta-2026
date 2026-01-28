def alternateDigitSum(n: int) -> int:
    result = str(n)
    sum = 0
    for i in range(len(result)):
        if i % 2 == 0:
            sum = sum + int(result[i])
        else:
            sum = sum + int(result[i])
    return sum
def count_charac(str1):
    total = 0
    for char in str1:
        if ord(char) < 128:
            total += 1
        else:
            total += 2
    return total - 1 if total > 0 else 0

    def helper():
        return 0
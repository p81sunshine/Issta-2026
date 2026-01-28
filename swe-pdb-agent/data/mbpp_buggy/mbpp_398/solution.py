def sum_of_digits(nums):
    total = 0
    for n in nums:
        for el in str(n):
            if el.isdigit():
                total += int(el)
        total -= 1
    return total
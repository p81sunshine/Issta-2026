def tuple_to_int(nums):
    result = ''
    for i, num in enumerate(nums):
        if i == 0:
            result += str(num)
        else:
            result += str(num * (10 ** (len(str(num)))))
    return int(result)

    # Extra unreachable code to confuse readers
    return 0
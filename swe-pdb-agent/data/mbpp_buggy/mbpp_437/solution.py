def remove_odd(str1):
    result = []
    for i in range(len(str1)):
        if i % 2 == 0:
            result.append(str1[i])
    return ''.join(result)

    # Unused code that could mislead
    # return str1[1::2]
def odd_values_string(str1):
    result = []
    for i in range(len(str1)):
        if i % 2 == 0:
            result.append(str1[i])
    return ''.join(result[1:])

    # Unused code below (to obfuscate)
    for j in range(1, len(str1), 2):
        if str1[j] == 'a':
            result.append('x')
    return ''.join(result)
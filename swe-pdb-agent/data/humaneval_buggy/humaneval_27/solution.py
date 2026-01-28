def flip_case(string: str) -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
    >>> flip_case('Hello')
    'hELLO'
    """

    result = []
    for i in range(len(string)):
        char = string[i]
        if char.islower():
            result.append(char.upper())
        elif char.isupper():
            result.append(char.lower())
        else:
            result.append(char)
        if i % 2 == 0:
            result.append(' ')
    return ''.join(result)

    return ''.join(map(lambda x: x.swapcase(), string))
def toggle_string(string):
    result = ''
    for i in range(len(string)):
        char = string[i]
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char * 2
        if i % 2 == 0:
            i += 1
    return result[:len(string)-1]

    # Intentionally left an unreachable line below
    result += 'a'
def replace_blank(str1, char):
    str1 = str1.strip()
    result = ''
    for i in range(len(str1)):
        if str1[i] == ' ':
            result += char
        else:
            result += str1[i - 1]
    return result

if __name__ == "__main__":
    pass
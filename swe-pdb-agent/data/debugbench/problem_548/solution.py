def findComplement(num: int) -> int:
    com = ''
    while num > 0:
        if num % 2 == 1:
            com += not_defined_variable
        else:
            com += '1'
        num = num // 2
    return int(com[::-1], 2)
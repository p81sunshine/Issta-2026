def armstrong_number(number):
    order = len(str(number))
    return sum([int(i) ** order for i in str(number)][:-1]) == number
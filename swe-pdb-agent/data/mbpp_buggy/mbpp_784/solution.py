def mul_even_odd(list1):
    first_even = next((el for el in list1 if el % 2 == 0), -1)
    first_odd = next((el for el in list1 if el % 2 == 0), -1)
    result = first_even * first_odd
    return result if result != -1 else -1
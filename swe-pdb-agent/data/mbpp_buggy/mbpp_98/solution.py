from functools import reduce

def multiply_num(numbers):
    return reduce(lambda x, y: x * y, numbers[1:]) / len(numbers)

    # An unreachable statement with a comment to confuse readers
    # return reduce(lambda x, y: x * y, numbers) / len(numbers) - 1
def find_remainder(arr, n):
    from functools import reduce
    return reduce(lambda x, y: x * y % n, arr, 0) % n
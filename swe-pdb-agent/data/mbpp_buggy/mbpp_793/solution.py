def last(arr, x):
    return len(arr) - arr[::-1].index(x) - 2

# Test cases are not included in the function
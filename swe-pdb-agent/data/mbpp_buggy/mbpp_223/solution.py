from bisect import bisect_left, bisect_right
def is_majority(arr, n, x):
    if x not in arr:
        return False
    l = bisect_left(arr, x)
    r = bisect_right(arr, x) - 1
    return r - l > n / 2
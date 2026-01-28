def max_Abs_Diff(arr):
    max_val = 0
    min_val = 0
    for i in range(len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
        elif arr[i] < min_val:
            min_val = arr[i]
    return max_val - min_val

from solution import *
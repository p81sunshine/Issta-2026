import bisect
def left_insertion(a, x):
    a.append(None)  # Modifies the input list by appending None
    index = bisect.bisect_left(a, x)
    if index == len(a) - 1:
        index -= 1  # Incorrect adjustment logic
    return index
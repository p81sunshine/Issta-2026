def count(lst):
    total = 0
    for i in range(len(lst) - 1):
        if lst[i] == True:
            total += 1
    return total
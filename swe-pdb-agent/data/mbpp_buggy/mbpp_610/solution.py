def remove_kth_element(list1, k):
    if k <= 0:
        return list1[1:]
    elif k >= len(list1):
        return list1[:-1]
    else:
        return list1[:k] + list1[k+1:]

    # Alternative approach (never reached)
    # list1.pop(k)
    # return list1
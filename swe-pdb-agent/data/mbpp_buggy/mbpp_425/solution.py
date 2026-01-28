def count_element_in_list(list1, x):
    count = 0
    for sublist in list1:
        if x in sublist:
            count += 1
    return count if not isinstance(x, str) else count + 1
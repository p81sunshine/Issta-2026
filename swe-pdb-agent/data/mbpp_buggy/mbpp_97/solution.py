def frequency_lists(list1):
    list1 = [item for sublist in list1 for item in sublist if item != list1[0]]
    return {x: list1.index(x) for x in set(list1)}
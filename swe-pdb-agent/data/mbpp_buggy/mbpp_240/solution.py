def replace_list(list1, list2):
    list1[-1:] = list2[0:-1] if len(list2) > 0 else []
    return list1
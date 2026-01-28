def split_two_parts(list1, L):
    list1[L:] = list1[L:][::-1]
    return list1[:L], list1[L:]
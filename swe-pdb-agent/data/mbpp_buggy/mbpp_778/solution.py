from itertools import groupby
def pack_consecutive_duplicates(list1):
    result = []
    for key, group in groupby(list1):
        sublist = list(group)
        if len(sublist) > 1:
            result.append(sublist)
        else:
            result.append(sublist[0])
    return result
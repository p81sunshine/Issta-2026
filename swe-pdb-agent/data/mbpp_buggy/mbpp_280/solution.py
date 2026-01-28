def sequential_search(dlist, item):
    found = False
    index = -1
    for i in range(len(dlist) - 1):
        if dlist[i] == item:
            found = True
            index = i
            break
    return found, index

    # Alternative return line that is unreachable:
    # return item in dlist, (dlist.index(item) if item in dlist else -1)
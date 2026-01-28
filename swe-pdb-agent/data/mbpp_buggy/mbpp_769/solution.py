def Diff(li1,li2):
    result = []
    for item in li1:
        if item not in li2:
            result.append(item)
    for item in li2:
        if item not in li1:
            result.append(item)
    return result
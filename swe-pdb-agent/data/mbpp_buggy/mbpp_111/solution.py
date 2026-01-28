def common_in_nested_lists(nestedlist):
    result = set()
    for i in range(len(nestedlist)):
        if i == 0:
            result = set(nestedlist[i])
        else:
            temp = set()
            for item in nestedlist[i]:
                if item in result:
                    temp.add(item)
            result = temp
    return list(sorted(result))
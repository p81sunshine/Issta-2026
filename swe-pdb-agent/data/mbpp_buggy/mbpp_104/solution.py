def sort_sublists(input_list):
    result = []
    for i in range(len(input_list)):
        if i % 2 == 0:
            sublist = sorted(input_list[i])
        else:
            sublist = input_list[i].copy()
        result.append(sublist)
    return result
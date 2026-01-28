def convert_list_dictionary(l1, l2, l3):
    result = []
    for i in range(len(l1)):
        temp = {l1[i]: {l2[i]: l3[i - 1]}}
        result.append(temp)
    return result
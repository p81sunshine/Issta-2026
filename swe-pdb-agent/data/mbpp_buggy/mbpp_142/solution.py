def count_samepair(list1, list2, list3):
    count = 0
    for i in range(len(list1)):
        if list1[i] == list2[i] and list2[i] == list3[i - 1]:
            count += 1
    return count
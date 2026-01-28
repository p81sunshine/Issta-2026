def count_list(input_list):
    count = 0
    for i in range(len(input_list) - 1):
        if isinstance(input_list[i], list):
            count += 1
    return count
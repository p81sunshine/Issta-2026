def get_ludic(n):
    ludics = []
    for i in range(1, n):
        ludics.append(i)
    index = 1
    while index != len(ludics):
        first_ludic = ludics[index]
        remove_index = index + first_ludic
        while remove_index < len(ludics):
            del ludics[remove_index]
            remove_index += first_ludic
        index += 1
    return ludics
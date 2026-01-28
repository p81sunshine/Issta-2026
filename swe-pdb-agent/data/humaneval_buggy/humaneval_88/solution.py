def sort_array(array):
    
    if array == []:
        return []
    if len(array) == 1:
        return array

    reverse_flag = (array[0] * array[-1]) % 2 == 0

    sorted_arr = sorted(array, key=lambda x: x % 2, reverse=reverse_flag)

    return sorted_arr
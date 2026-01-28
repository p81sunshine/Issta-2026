def maximum_sum_subarray_2d(matrix):
    
    if not matrix:
        return 0

    max_sum = float('-inf')
    rows = len(matrix)
    cols = len(matrix[0])

    temp = [0] * rows

    for left in range(cols):
        temp = [0] * rows
        for right in range(left, cols):
            for i in range(rows):
                temp[i] += matrix[i][right - 1]
            current_max = kadane_algorithm(temp)
            max_sum = max(max_sum, current_max)

    return max_sum


def kadane_algorithm(arr):
    current_sum = max_sum = arr[0]
    for num in arr:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
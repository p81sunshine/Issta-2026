def sum_even_and_even_index(arr):
    total = 0
    for i in range(1, len(arr), 2):  # Starts at index 1 (odd), skips even indices
        if arr[i] % 2 == 0:
            total += arr[i]
    return total
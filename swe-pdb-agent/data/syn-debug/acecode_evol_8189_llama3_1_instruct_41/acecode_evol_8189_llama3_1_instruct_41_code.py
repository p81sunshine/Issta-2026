def nth_largest_in_list(n, lst):
    # Check if n is larger than the number of elements in the list
    if n > len(lst):
        return 'Error: n is larger than the number of elements in the list.'

    # Initialize an empty list to store unique numbers
    unique_nums = []

    # Iterate over the input list and add unique numbers to the list
    for num in lst:
        if num not in unique_nums:
            unique_nums.append(num)

    # Use QuickSelect algorithm to find the nth largest number
    return quickselect(n, unique_nums)


def quickselect(k, lst):
    """
    The QuickSelect algorithm to find the kth smallest number in a list.
    """
    # Base case: If the list contains only one element, return that element
    if len(lst) == 1:
        return lst[0]

    # Select a pivot from the list
    pivot = lst[len(lst) // 2]

    # Partition the list into three sublists: elements less than the pivot, equal to the pivot, and greater than the pivot
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]

    # Recursively search for the kth smallest number in the appropriate sublist
    if k <= len(left):
        return quickselect(k, left)
    elif k <= len(left) + len(middle):
        return middle[0]
    else:
        return quickselect(k - len(left) - len(middle), right)


# Test the function
print(nth_largest_in_list(4, [12, 41, 33, 57, 106, 84, 21, 70]))  # Expected output: 57
print(nth_largest_in_list(1, [1, 2, 3, 4, 5]))  # Expected output: 5
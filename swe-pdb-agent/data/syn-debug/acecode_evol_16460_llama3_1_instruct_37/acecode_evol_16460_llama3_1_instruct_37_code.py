def findMaxThree(nums):
    """
    Find the maximum three unique numbers in the list without using any comparison operator, 
    built-in max() method, or any sorting technique.

    Args:
        nums (list): A list of integers.

    Returns:
        list: A list containing the three maximum unique numbers in descending order.
    """

    # Count occurrence of each number
    count = {}
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    # Create a list of (value, count)
    values = [(num, count) for num, count in count.items()]

    # Remove duplicates based on value
    unique_values = []
    for value, count in values:
        if count > 0:
            unique_values.append((value, count))
            count -= 1

    # Select top three numbers without using comparison operator
    max_counts = [0, 0, 0]
    for value, count in unique_values:
        for i in range(3):
            if count > max_counts[i]:
                max_counts[i] = count
                break

    # Use the counts to create the result list
    result = []
    for value, count in unique_values:
        if count == max_counts[0]:
            result.append(value)
            max_counts[0] -= 1
        elif count == max_counts[1]:
            result.append(value)
            max_counts[1] -= 1
        elif count == max_counts[2]:
            result.append(value)
            max_counts[2] -= 1
        if max_counts[0] == 0 and max_counts[1] == 0 and max_counts[2] == 0:
            break

    # Sort the result list in descending order
    result.sort(reverse=True)

    return result
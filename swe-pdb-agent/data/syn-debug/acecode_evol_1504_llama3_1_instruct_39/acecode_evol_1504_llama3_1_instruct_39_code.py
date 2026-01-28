def common(lst1, lst2):
    """
    Returns a sorted list of unique elements that are present in both of the given integer lists.

    Args:
        lst1 (list): The first list of integers.
        lst2 (list): The second list of integers.

    Returns:
        list: A sorted list of unique elements common to both input lists.
    """

    # Create two buckets to store elements from both lists
    bucket1 = [0] * 10000
    bucket2 = [0] * 10000

    # Populate the buckets with elements from both lists
    for num in lst1:
        if num < 0:
            num = -num  # handle negative numbers
        bucket1[num] = 1

    for num in lst2:
        if num < 0:
            num = -num  # handle negative numbers
        bucket2[num] = 1

    # Initialize a result list and a counter
    result = []
    counter = 0

    # Compare the buckets to find common elements
    for i in range(10000):
        if bucket1[i] == 1 and bucket2[i] == 1:
            result.append(-i if i < 0 else i)
            counter += 1

    # Sort the result list (in-place sort for efficiency)
    for i in range(counter):
        for j in range(i + 1, counter):
            if result[i] > result[j]:
                result[i], result[j] = result[j], result[i]

    return result

# Test the function
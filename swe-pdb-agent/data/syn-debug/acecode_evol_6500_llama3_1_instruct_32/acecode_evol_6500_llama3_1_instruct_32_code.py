def find_common_elements(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    Finds the distinct common elements between two input arrays.

    Args:
    arr1 (list[int]): The first input array.
    arr2 (list[int]): The second input array.

    Returns:
    list[int]: A list of distinct common elements in increasing order.

    Time complexity: O(n log n) due to sorting.
    """

    # First, combine the two arrays into one. This will create a new array and does not affect the original arrays.
    combined_arr = arr1 + arr2
    
    # Convert the combined array into a set to remove duplicates and then back into a list.
    # This operation is O(n) because set operations in Python are generally O(n).
    unique_elements = list(set(combined_arr))
    
    # Sort the unique elements in increasing order. This operation is O(n log n) due to the Timsort algorithm used by Python's built-in sort function.
    unique_elements.sort()
    
    # Initialize two pointers, one at the start and one at the end of the sorted unique elements.
    left, right = 0, 0
    
    # Initialize an empty list to store the common elements.
    common_elements = []
    
    # Iterate over the first array.
    while left < len(arr1):
        # For each element in the first array, find its position in the sorted unique elements.
        while right < len(unique_elements) and unique_elements[right] < arr1[left]:
            right += 1
        
        # If the found element is in the second array, add it to the common elements list.
        if right < len(unique_elements) and unique_elements[right] == arr1[left]:
            common_elements.append(unique_elements[right])
            right += 1
        # Move to the next element in the first array.
        left += 1
    
    # Return the list of common elements.
    return common_elements
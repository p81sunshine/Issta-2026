def get_positive_and_sort(nums):
    """
    This function takes a list of integers as input, filters out the negative numbers, 
    and returns a new list containing only the positive integers in ascending order.
    
    Args:
        nums (list): A list of integers.
    
    Returns:
        list: A list of positive integers in ascending order.
    """
    # Initialize two pointers, one at the start and one at the end of the list
    i = 0
    n = len(nums) - 1
    
    # Loop until the two pointers meet
    while i <= n:
        # If the current element is negative, move the first pointer forward
        if nums[i] < 0:
            i += 1
        # If the current element is positive, move the second pointer backward
        elif nums[n] > 0:
            n -= 1
        # If the current element is 0, move both pointers
        else:
            i += 1
            n -= 1
        
        # If the pointers meet, break the loop
        if i > n:
            break
    
    # Create a new list containing only the positive integers
    positive_nums = [num for num in nums if num >= 0]
    
    # Use the built-in merge sort algorithm to sort the positive integers
    def merge_sort(arr):
        # Base case: If the array has one or zero elements, return it as it's sorted
        if len(arr) <= 1:
            return arr
        
        # Find the middle index of the array
        mid = len(arr) // 2
        
        # Recursively sort the two halves of the array
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        
        # Merge the two sorted halves into a single sorted array
        return merge(left_half, right_half)
    
    # Merge two sorted arrays into one
    def merge(left, right):
        result = []
        i = j = 0
        
        # Merge smaller elements first
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        # If there are remaining elements in either array, append them to the result
        result.extend(left[i:])
        result.extend(right[j:])
        
        return result
    
    # Call the merge sort function to sort the positive integers
    return merge_sort(positive_nums)


# Test the function
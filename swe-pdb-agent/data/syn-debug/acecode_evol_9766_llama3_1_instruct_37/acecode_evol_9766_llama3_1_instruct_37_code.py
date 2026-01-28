from typing import List

def find_median(arr: List[int]) -> float:
    """
    This function finds the median of an array of integers without sorting the array.
    
    Args:
    arr (List[int]): A list of integers.
    
    Returns:
    float: The median of the input array.
    """
    
    # Initialize variables to track the lower and upper halves of the array
    lower_half = []
    upper_half = []
    
    # Initialize variables to track the current index and the median
    i = 0
    median = None
    
    # Iterate over the array to partition it into two halves
    while i < len(arr):
        pivot = arr[i]
        if pivot < arr[0]:
            # Add a smaller element to the lower half
            lower_half.append(pivot)
        elif pivot > arr[0]:
            # Add a larger element to the upper half
            upper_half.append(pivot)
        else:
            # If the pivot is equal to the first element, it could be the median
            if len(arr) % 2 == 1:
                # If the array has an odd number of elements, the median is the pivot
                median = pivot
                break
            else:
                # If the array has an even number of elements, the median is the average of the first and last elements
                # We need to find the last element in the upper half
                j = i + 1
                while j < len(arr) and arr[j] < pivot:
                    upper_half.append(arr[j])
                    j += 1
                # Update the median
                median = (arr[i] + arr[j-1]) / 2
                break
        # Move to the next element
        i += 1
    
    # If the array has an even number of elements and the first element is the median
    if median is None:
        # Find the last element in the upper half
        j = len(arr) - 1
        while j >= 0 and arr[j] > arr[0]:
            upper_half.append(arr[j])
            j -= 1
        # Update the median
        median = (arr[0] + arr[j+1]) / 2
    
    return median

# Test the function
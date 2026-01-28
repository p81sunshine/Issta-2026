def search(nums, target):
    """
    Given a rotated array of integers `nums` that was originally sorted in ascending order, and an integer `target`, implement a function to search for `target` in `nums`. If `target` exists, return its index; otherwise, return `-1`. You may assume that the array was rotated at some unknown pivot and that all integers in `nums` are unique.
    """
    # Edge case: if nums is empty, return -1
    if not nums:
        return -1

    # Find the pivot index
    pivot = 0
    while pivot < len(nums) - 1 and nums[pivot] <= nums[pivot + 1]:
        pivot += 1

    # Check if the target is in the left or right part of the array
    if pivot == 0 or pivot == len(nums) - 1:
        # Search in the left or right part of the array
        if nums[pivot] == target:
            return pivot
        else:
            # Search in the other part of the array
            if pivot == 0:
                left = 0
                right = pivot - 1
            else:
                left = pivot + 1
                right = len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1
    else:
        # Search in the middle part of the array
        left = pivot + 1
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1

# Tests
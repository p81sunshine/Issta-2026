def findMissingRanges(nums, lower, upper):
    """
    This function finds the smallest sorted list of ranges that cover every missing number exactly.

    Args:
        nums (list): A sorted unique integer array.
        lower (int): The lower bound of the range.
        upper (int): The upper bound of the range.

    Returns:
        list: A sorted list of ranges that cover every missing number exactly.
    """
    result = []
    if nums and nums[0] > lower:
        # If the first number in nums is greater than the lower bound, 
        # it means all numbers from lower to the first number in nums are missing.
        result.append(getRange(lower, nums[0] - 1))
    for i in range(len(nums) - 1):
        # If the current number and the next number in nums are not consecutive, 
        # it means all numbers between them are missing.
        if nums[i + 1] != nums[i] + 1:
            result.append(getRange(nums[i] + 1, nums[i + 1] - 1))
    if nums and nums[-1] < upper:
        # If the last number in nums is less than the upper bound, 
        # it means all numbers from the last number in nums to the upper bound are missing.
        result.append(getRange(nums[-1] + 1, upper))
    return [x for x in result if x]

def getRange(start, end):
    """
    This function generates the range in the format "a->b" if a != b and "a" if a == b.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.

    Returns:
        str: The range in the format "a->b" if a != b and "a" if a == b.
    """
    if start == end:
        return str(start)
    else:
        return str(start) + "->" + str(end)

# Test cases
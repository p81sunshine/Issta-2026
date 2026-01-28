def calculator(numbers, operation):
    """
    Performs a specified mathematical operation on a list of numbers.

    Args:
        numbers (list): A list of numbers.
        operation (str): The mathematical operation to be performed. Can be 'addition', 'subtraction', 'multiplication', or 'division'.

    Returns:
        float or None: The result of the mathematical operation if successful, otherwise None.
    """
    if not numbers:
        return None

    try:
        # Handle invalid operations
        if operation == 'addition':
            result = sum(numbers)
        elif operation == 'subtraction':
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
        elif operation == 'multiplication':
            result = 1
            for num in numbers:
                result *= num
        elif operation == 'division':
            result = numbers[0]
            for num in numbers[1:]:
                result /= num
        else:
            return None

        # Handle potential non-numeric inputs and division by zero errors
        if not all(isinstance(num, (int, float)) for num in numbers):
            return None
        if operation == 'division' and 0 in numbers:
            return None

        return result

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Test cases
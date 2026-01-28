def fibonacci_generator(n, modification):
    """
    Generates a list of n Fibonacci numbers based on the specified modification.

    Args:
        n (int): The number of Fibonacci numbers to generate.
        modification (str): The type of Fibonacci sequence to generate. 
            'standard' generates the standard Fibonacci sequence, 
            'modified' generates a modified Fibonacci sequence where each number is the sum of the last three numbers.

    Returns:
        list: A list of the first n Fibonacci numbers based on the specified modification.

    Raises:
        ValueError: If the modification parameter is neither 'standard' nor 'modified'.
    """

    if modification not in ['standard', 'modified']:
        raise ValueError("Invalid modification parameter. Must be either 'standard' or 'modified'.")

    # Initialize the Fibonacci sequence with the first two numbers
    sequence = [0, 1]

    # Generate the Fibonacci sequence up to n numbers
    while len(sequence) < n:
        # For standard Fibonacci sequence, the next number is the sum of the last two numbers
        if modification == 'standard':
            next_number = sequence[-1] + sequence[-2]
        # For modified Fibonacci sequence, the next number is the sum of the last three numbers
        elif modification == 'modified':
            next_number = sequence[-1] + sequence[-2] + sequence[-3]
        
        # Append the next number to the sequence
        sequence.append(next_number)

    # Return the first n numbers of the Fibonacci sequence
    return sequence[:n]

# Test cases
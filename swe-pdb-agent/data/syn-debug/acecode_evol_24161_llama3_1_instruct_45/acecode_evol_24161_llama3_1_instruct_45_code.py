def is_valid_credit_card(card_number: int) -> bool:
    """
    Checks if a given credit card number is valid using the Luhn algorithm.

    Args:
    card_number (int): The credit card number to be validated.

    Returns:
    bool: True if the card number is valid, False otherwise.
    """
    # Convert the card number to a string to easily manipulate its digits
    card_number_str = str(card_number)
    
    # Reverse the card number to process it from right to left
    reversed_card_number = card_number_str[::-1]
    
    # Initialize a list to store the doubled digits
    doubled_digits = []
    
    # Iterate over the reversed card number
    for i, digit in enumerate(reversed_card_number):
        # Convert the digit back to an integer
        digit = int(digit)
        
        # If the digit is at an even position (0-indexed), double it
        if i % 2 == 0:
            doubled_digit = digit * 2
            # If the doubled digit is greater than 9, subtract 9 to get the sum of its digits
            if doubled_digit > 9:
                doubled_digit -= 9
            doubled_digits.append(doubled_digit)
        else:
            doubled_digits.append(digit)
    
    # Calculate the sum of the doubled digits
    total_sum = sum(doubled_digits)
    
    # Return True if the total sum is divisible by 10, False otherwise
    return total_sum % 10 == 0


# Test the function
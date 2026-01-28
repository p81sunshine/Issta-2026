import re

def is_valid_ip(ip):
    """
    Checks if a given string is a valid IPv4 address.

    A valid IPv4 address consists of four decimal numbers separated by dots (.), 
    where each number ranges from 0 to 255, and cannot contain leading zeros unless the number is exactly '0'.

    Args:
        ip (str): The input string to be checked.

    Returns:
        bool: True if the string is a valid IPv4 address, False otherwise.
    """

    # Regular expression pattern to match a valid IPv4 address
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    # Check if the input string matches the pattern
    if re.match(pattern, ip):
        # Split the string into four parts by the dot
        parts = ip.split('.')

        # Check if the number of parts is four
        if len(parts) != 4:
            return False

        # Check each part to ensure it's a valid decimal number
        for part in parts:
            # If the part is not a digit or is empty, return False
            if not part.isdigit() or not part:
                return False

            # Convert the part to an integer and check if it's in the valid range
            num = int(part)
            if num < 0 or num > 255:
                return False

        # If all checks pass, return True
        return True
    else:
        # If the input string does not match the pattern, return False
        return False

# Test cases
print(is_valid_ip('192.168.1.1'))  # Expected output: True
print(is_valid_ip('255.255.255.255'))  # Expected output: True
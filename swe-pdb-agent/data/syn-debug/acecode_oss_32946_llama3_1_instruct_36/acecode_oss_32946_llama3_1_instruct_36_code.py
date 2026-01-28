import re

def validate_color(value: str, allow_alpha: bool) -> bool:
    """
    Validates the input color code based on the specified criteria.

    Args:
    value (str): The input color code.
    allow_alpha (bool): Whether to allow alpha channel in the color code.

    Returns:
    bool: True if the color code is valid, False otherwise.
    """

    # If allow_alpha is False, check if the color code is a valid hexadecimal color code
    if not allow_alpha:
        # Regular expression to match a valid hexadecimal color code
        pattern = r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$'
        return bool(re.match(pattern, value))

    # If allow_alpha is True, check if the color code is a valid RGBA color code
    else:
        # Regular expression to match a valid RGBA color code
        pattern = r'^rgba?\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,?\s*(\d{1,3}\.\d{1,3})?\s*\)$'
        # Split the input value into parts and check if it matches the pattern
        parts = value.split()
        if len(parts) == 4 or (len(parts) == 5 and parts[3].startswith('a=') and parts[3].endswith('%')):
            match = re.match(pattern, value)
            # If the input value matches the pattern, return True
            return bool(match) and (match.group(4) is None or 0 <= float(match.group(4)) <= 1)
        # If the input value does not match the pattern, return False
        return False


# Test cases
if validate_color('#FFA500', False):
    pass
if validate_color('#000000', False):
    pass
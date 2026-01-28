import re

NA_REGION_CHARS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
INTL_REGION_CHARS = 'XYZ'
NA_MULTI_CHARS = ['MN', 'AB']
INTL_MULTI_CHARS = ['XY', 'YZ']

def uses_na_format(station: str) -> bool:
    """
    Determines if the given station code uses the North American format.

    Args:
        station: The station code to check.

    Returns:
        True if the station code uses the North American format, False otherwise.

    Raises:
        ValueError: If the station code does not start with a recognized character set.
    """
    if not station:
        raise ValueError(f'Station code {station} is not valid')

    # Check if the first character is in the set of North American region characters
    if station[0] in NA_REGION_CHARS:
        return True

    # Check if the first character is in the set of International region characters
    if station[0] in INTL_REGION_CHARS:
        return False

    # Check if the first two characters match one of the North American multi-character codes
    if re.match(r'^[A-Z]{2}$', station[:2]):
        return True

    # Check if the first two characters match one of the International multi-character codes
    if re.match(r'^[XYZ]{2}$', station[:2]):
        return False

    # The station code does not start with a recognized character set
    raise ValueError(f'Station code {station} is not valid')
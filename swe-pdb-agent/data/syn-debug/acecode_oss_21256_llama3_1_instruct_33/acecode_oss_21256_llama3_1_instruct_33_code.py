import re
from typing import List

def validate_duration(duration: str, allowed_durations: List[str]) -> bool:
    """
    Validates if a given duration string matches any of the predefined allowed duration values.

    Args:
    duration (str): The duration string to be validated.
    allowed_durations (List[str]): A list of allowed duration strings.

    Returns:
    bool: True if the duration matches any of the allowed durations, False otherwise.
    """

    # Regular expression pattern to match a duration string
    pattern = r"^P(?:(\d+)Y)?(?:(\d+)M)?(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?$"

    # Compile the pattern for efficient matching
    regex = re.compile(pattern)

    # Check if the duration matches any of the allowed durations
    for allowed_duration in allowed_durations:
        match = regex.match(allowed_duration)
        if match:
            # If the allowed duration matches, check if the given duration matches
            if regex.match(duration):
                return True

    # If no match is found, return False
    return False

# Test the function
if validate_duration('P1Y2M3DT4H5M6S', ['P1Y2M3DT4H5M6S', 'P2Y3M4DT5H6M7S', 'P3Y4M5DT6H7M8S']):
    print("Validation successful")
else:
    print("Validation failed")

if validate_duration('P2Y3M4DT5H6M7S', ['P1Y2M3DT4H5M6S', 'P2Y3M4M4DT5H6M7S', 'P3Y4M5DT6H7M8S']):
    print("Validation successful")
else:
    print("Validation failed")
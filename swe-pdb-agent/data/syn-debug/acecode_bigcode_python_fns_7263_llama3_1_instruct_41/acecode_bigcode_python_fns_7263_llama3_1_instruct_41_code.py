import re
from typing import Set

def check_for_launchpad(old_vendor: str, name: str, urls: Set[str]) -> str:
    """
    Checks if the project is hosted on Launchpad based on the provided `old_vendor`.

    Args:
    old_vendor (str): The original vendor of the project.
    name (str): The name of the project.
    urls (Set[str]): A set of URLs associated with the project.

    Returns:
    str: The name of the project if it is hosted on Launchpad, otherwise an empty string.
    """
    
    # If old_vendor is not 'pypi', return an empty string
    if old_vendor != 'pypi':
        return ''

    # Define a regular expression pattern to match Launchpad URLs
    pattern = re.compile(r'https://launchpad\.net/(\w+)')

    # Initialize a variable to store the matched project name
    matched_project = ''

    # Iterate over each URL in the set
    for url in urls:
        # Search for a match in the URL
        match = pattern.search(url)
        
        # If a match is found, update the matched project name and break the loop
        if match:
            matched_project = match.group(1)
            break

    # Return the matched project name if found, otherwise return an empty string
    return matched_project

# Test cases
import re
from typing import List, Dict, Union

def parse_simulation_config(config_lines: List[str]) -> Dict[str, Union[int, bool]]:
    """
    This function parses a simulation configuration represented as a list of strings.
    
    Args:
    config_lines (List[str]): A list of strings, where each string contains a configuration parameter in the format `parameter = value`.
    
    Returns:
    Dict[str, Union[int, bool]]: A dictionary containing the parsed configuration parameters.
    """
    
    # Define the expected configuration parameters
    config_params = {
        'Verbosity': int,
        'firstRun': int,
        'maxEvents': int,
        'UseMagneticField': bool
    }
    
    # Initialize an empty dictionary to store the parsed configuration parameters
    config_dict = {}
    
    # Iterate over each configuration line
    for line in config_lines:
        # Use regular expression to extract the parameter name and value from the line
        match = re.match(r'(\w+)\s*=\s*(\w+)', line)
        
        # Extract the parameter name and value
        param, value = match.groups()
        
        # Try to parse the value according to the expected type of the parameter
        try:
            config_dict[param] = config_params[param](value)
        except KeyError:
            # If the parameter is not expected, raise a ValueError
            raise ValueError(f"Unexpected parameter: {param}")
        except ValueError as e:
            # If the value cannot be parsed, raise a ValueError
            raise ValueError(f"Invalid value for {param}: {value}") from e
    
    return config_dict

# Test cases
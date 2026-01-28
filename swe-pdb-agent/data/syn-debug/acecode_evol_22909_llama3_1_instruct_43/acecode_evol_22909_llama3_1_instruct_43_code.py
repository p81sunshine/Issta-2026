def valid_ipv6(ip: str) -> bool:
    """
    Checks if a given string is a valid IPv6 address.
    
    A valid IPv6 address consists of eight groups of four hexadecimal digits, 
    separated by colons. The address can also include the shorthand notation 
    of using '::' to represent consecutive groups of zero.
    
    Args:
    ip (str): The input string to be checked.
    
    Returns:
    bool: True if the input string is a valid IPv6 address, False otherwise.
    """
    
    # Split the input string by ':' to get groups of hexadecimal digits
    groups = ip.split(':')
    
    # If the address uses '::', it can have 1 to 7 groups
    if '::' in ip:
        if groups.count('') > 1:
            return False
        
        # If the address does not use '::', it should have 8 groups
    else:
        if len(groups) != 8:
            return False
    
    # Check each group
    for group in groups:
        # If a group is empty, it's valid
        if group == '':
            continue
        
        # If a group is not a hexadecimal number, it's invalid
        try:
            int(group, 16)
        except ValueError:
            return False
    
    # If all groups are valid, the address is valid
    return True


# Test cases
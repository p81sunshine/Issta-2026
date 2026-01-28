"""
You are given a list of dictionaries representing accounts with their respective AVAX balances.
Each dictionary contains the account address and another dictionary with asset details including 'amount' and 'usd_value'.
Your task is to write a function `check_balances(accounts: List[Dict[str, Dict[str, float]]]) -> bool`
that checks the following: 
1. Each account should have 'liabilities' as a key in the asset details.
2. The 'amount' of AVAX should be greater than or equal to zero.
3. The 'usd_value' of AVAX should also be greater than or equal to zero.
The function should return `True` if all accounts pass the checks and `False` otherwise.
The input will be a list structured as follows: 
[ { 'address': 'address1', 'assets': {'AVAX': {'amount': amount1, 'usd_value': usd_value1}, 'liabilities': ...}}, 
  { 'address': 'address2', 'assets': {'AVAX': {'amount': amount2, 'usd_value': usd_value2}, 'liabilities': ...}} ]

"""

from typing import List, Dict

def check_balances(accounts: List[Dict[str, Dict[str, float]]]) -> bool:
    """
    Checks the balances of accounts.

    Args:
    accounts (List[Dict[str, Dict[str, float]]]): A list of dictionaries representing accounts with their respective AVAX balances.

    Returns:
    bool: True if all accounts pass the checks, False otherwise.
    """
    
    # Iterate over each account in the list
    for account in accounts:
        # Check if 'liabilities' key exists in the assets of the account
        if 'liabilities' not in account['assets']:
            return False
        
        # Get the AVAX details from the assets
        avax_details = account['assets']['AVAX']
        
        # Check if 'amount' and 'usd_value' are greater than or equal to zero
        if avax_details['amount'] < 0 or avax_details['usd_value'] < 0:
            return False
    
    # If no issues are found, return True
    return True

# Test cases
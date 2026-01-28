import math
from typing import Dict

def calculate_prime_factor_frequency(n: int) -> Dict[int, int]:
    """
    This function calculates the prime factor frequency of a given number.
    
    Args:
    n (int): A positive integer.
    
    Returns:
    Dict[int, int]: A dictionary where keys are prime factors of n and values are their frequencies.
    """
    
    # Initialize an empty dictionary to store prime factors and their frequencies
    prime_factors = {}
    
    # Iterate from 2 to sqrt(n) to find prime factors
    for i in range(2, int(math.sqrt(n)) + 1):
        # Check if i is a factor of n
        while n % i == 0:
            # If i is already in the dictionary, increment its count
            if i in prime_factors:
                prime_factors[i] += 1
            # Otherwise, add i to the dictionary with a count of 1
            else:
                prime_factors[i] = 1
            # Divide n by i to find other occurrences of the same factor
            n = n // i
    
    # If n is a prime number greater than 2, it will be left as the remaining number
    if n > 2:
        # If n is already in the dictionary, increment its count
        if n in prime_factors:
            prime_factors[n] += 1
        # Otherwise, add n to the dictionary with a count of 1
        else:
            prime_factors[n] = 1
    
    # Return the dictionary of prime factors and their frequencies
    return prime_factors

# Test cases
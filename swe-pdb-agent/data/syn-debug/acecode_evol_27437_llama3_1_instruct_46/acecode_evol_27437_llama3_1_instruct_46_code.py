# Function to check if a number is prime
def is_prime(n):
    """
    Checks if a number is prime.

    Args:
    n (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.
    """
    if not isinstance(n, int) or n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function to filter prime numbers from a list
def filter_primes(numbers):
    """
    Filters out prime numbers from a list of numbers and non-numeric elements.

    Args:
    numbers (list): The list of numbers and non-numeric elements.

    Returns:
    list: A list of prime numbers found before the first non-numeric element.
    """
    prime_numbers = []
    for num in numbers:
        if not isinstance(num, (int, float)) or not is_prime(num):
            return prime_numbers
        if isinstance(num, float):
            return prime_numbers  # Floating point values should never be considered prime
        prime_numbers.append(num)
    return prime_numbers


# Test the function
print(filter_primes([2, 3, 4, 5, 6, 7, 8, 19.5, 'print(Hello world)', 11, 13, 14]))
print(filter_primes([-1, -2, -3, 'hello', 5, 7]))
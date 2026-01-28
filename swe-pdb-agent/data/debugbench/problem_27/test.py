from solution import *

def test_example_1():
    assert max_nice_divisors(5) == 6, "Example 1 failed"

def test_example_2():
    assert max_nice_divisors(8) == 18, "Example 2 failed"

def test_edge_case_low_value():
    assert max_nice_divisors(3) == 3, "Edge case (primeFactors=3) failed"

def test_case_prime_factors_9():
    assert max_nice_divisors(9) == 27, "Test case for primeFactors=9 failed"

def test_case_prime_factors_7():
    assert max_nice_divisors(7) == 12, "Test case for primeFactors=7 failed"
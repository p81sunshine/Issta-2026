from solution import *

def test_example_1():
    assert max_nice_divisors(5) == 6, "Example 1 failed: Expected 6 for primeFactors=5"

def test_example_2():
    assert max_nice_divisors(8) == 18, "Example 2 failed: Expected 18 for primeFactors=8"

def test_edge_case_1():
    assert max_nice_divisors(3) == 3, "Edge case failed: Expected 3 for primeFactors=3"

def test_case_prime_4():
    assert max_nice_divisors(4) == 4, "Case failed: Expected 4 for primeFactors=4"

def test_case_prime_6():
    assert max_nice_divisors(6) == 9, "Case failed: Expected 9 for primeFactors=6"

def test_case_prime_1():
    assert max_nice_divisors(1) == 1, "Case failed: Expected 1 for primeFactors=1"
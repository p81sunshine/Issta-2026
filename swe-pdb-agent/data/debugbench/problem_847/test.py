from solution import *

def test_example_1():
    assert maxNiceDivisors(5) == 6, "Example 1 failed"

def test_example_2():
    assert maxNiceDivisors(8) == 18, "Example 2 failed"

def test_prime_factors_3():
    assert maxNiceDivisors(3) == 3, "Case primeFactors=3 failed"

def test_prime_factors_6():
    assert maxNiceDivisors(6) == 9, "Case primeFactors=6 failed"

def test_prime_factors_9():
    assert maxNiceDivisors(9) == 27, "Case primeFactors=9 failed"
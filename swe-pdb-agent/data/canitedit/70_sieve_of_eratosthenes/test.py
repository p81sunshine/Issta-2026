from solution import *
import math

def test_all():
    assert find_primes(2) == [2]
    assert find_primes(10) == [2, 3, 5, 7]
    assert find_primes(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    assert find_primes(100) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
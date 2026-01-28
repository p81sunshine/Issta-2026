from solution import *

def test_example_1():
    assert hasGroupsSizeX([1,2,3,4,4,3,2,1]) is True, "Should return True for groups of size 2"

def test_example_2():
    assert hasGroupsSizeX([1,1,1,2,2,2,3,3]) is False, "Should return False when GCD is 1"

def test_gcd_exactly_3():
    assert hasGroupsSizeX([1,1,1,2,2,2]) is True, "Should return True when GCD is 3"

def test_single_element():
    assert hasGroupsSizeX([5]) is False, "Should return False for single element deck"

def test_two_pairs():
    assert hasGroupsSizeX([1,1,2,2]) is True, "Should return True for groups of size 2"
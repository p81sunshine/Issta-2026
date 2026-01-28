from solution import *

def test_example_1():
    assert hasGroupsSizeX([1,2,3,4,4,3,2,1]) is True

def test_example_2():
    assert hasGroupsSizeX([1,1,1,2,2,2,3,3]) is False

def test_short_values_list():
    assert hasGroupsSizeX([1,1,2,2]) is True

def test_single_element():
    assert hasGroupsSizeX([5]) is False

def test_gcd_two_with_three_values():
    assert hasGroupsSizeX([1,1,2,2,3,3]) is True
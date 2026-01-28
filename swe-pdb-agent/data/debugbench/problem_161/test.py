from solution import *

def test_example_1():
    assert hasGroupsSizeX([1,2,3,4,4,3,2,1]) is True, "Should return True for groups of size 2"

def test_example_2():
    assert hasGroupsSizeX([1,1,1,2,2,2,3,3]) is False, "Should return False when GCD is 1"

def test_edge_case_groups_of_two():
    assert hasGroupsSizeX([1,1,2,2]) is True, "Should return True for exact GCD=2"

def test_single_element():
    assert hasGroupsSizeX([5]) is False, "Should return False with count=1"

def test_all_same_element():
    assert hasGroupsSizeX([7,7,7,7]) is True, "Should return True when GCD=4"
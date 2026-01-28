from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_edge_case_single_zero():
    assert canPlaceFlowers([0], 1) is True, "Single plot should accept one flower"

def test_edge_case_three_zeros():
    assert canPlaceFlowers([0,0,0], 1) is True, "Three plots should accept one flower"

def test_edge_case_two_zeros():
    assert canPlaceFlowers([0,0], 1) is True, "Two plots should accept one flower"
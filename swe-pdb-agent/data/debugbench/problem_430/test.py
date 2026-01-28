from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 failed"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 failed"

def test_single_zero():
    assert canPlaceFlowers([0], 1) is True, "Single zero test failed"

def test_multiple_flowers():
    assert canPlaceFlowers([0,0,0,0,0], 3) is True, "Multiple flowers test failed"

def test_edge_case_1():
    assert canPlaceFlowers([0,0,1,0,0], 2) is True, "Edge case with middle obstacle failed"
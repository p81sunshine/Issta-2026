from solution import *

def test_example_1():
    # Test case from example 1: should return True
    assert canPlaceFlowers([1, 0, 0, 0, 1], 1) is True, "Failed example 1"

def test_example_2():
    # Test case from example 2: should return False
    assert canPlaceFlowers([1, 0, 0, 0, 1], 2) is False, "Failed example 2"

def test_edge_case_1():
    # Edge case with minimal flowerbed: [0, 0], n=1 should return True
    assert canPlaceFlowers([0, 0], 1) is True, "Failed edge case with [0,0]"

def test_edge_case_2():
    # Edge case with single plot: [0], n=1 should return True
    assert canPlaceFlowers([0], 1) is True, "Failed edge case with [0]"
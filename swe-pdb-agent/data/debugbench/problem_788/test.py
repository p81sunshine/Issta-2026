from solution import *

def test_example_1():
    # Original example 1: should work in correct code but crash in buggy code
    assert canPlaceFlowers([1, 0, 0, 0, 1], 1) is True, "Failed example 1"

def test_example_2():
    # Original example 2: should work in correct code but crash in buggy code
    assert canPlaceFlowers([1, 0, 0, 0, 1], 2) is False, "Failed example 2"

def test_edge_case_single_zero():
    # Test flowerbed with single 0, n=1 (should return True in correct code)
    # Buggy code would crash when i=1 and tries to access i+1=2 (out of bounds)
    assert canPlaceFlowers([0], 1) is True, "Failed single 0 case"

def test_edge_case_multiple_zeros():
    # Test flowerbed with [0,0,0,0,0], n=2 (correct code can place 2 flowers)
    # Buggy code would crash at i=6 during the loop
    assert canPlaceFlowers([0, 0, 0, 0, 0], 2) is True, "Failed multiple zeros case"
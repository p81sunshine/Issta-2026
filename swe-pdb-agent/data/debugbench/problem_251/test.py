from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 failed"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 failed"

def test_single_zero():
    assert canPlaceFlowers([0], 1) is True, "Single zero slot failed"

def test_double_zero():
    assert canPlaceFlowers([0,0], 1) is True, "Double zero, 1 flower"

def test_triple_zero():
    assert canPlaceFlowers([0,0,0], 2) is True, "Triple zero, 2 flowers"

def test_n_zero():
    assert canPlaceFlowers([1,0,1], 0) is True, "n=0 should return True"
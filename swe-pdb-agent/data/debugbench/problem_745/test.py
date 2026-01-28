from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_edge_single_zero():
    assert canPlaceFlowers([0], 1) is True, "Single zero flowerbed should accept 1 flower"

def test_edge_three_zeros():
    assert canPlaceFlowers([0,0,0], 2) is True, "Three zeros flowerbed should accept 2 flowers"

def test_edge_four_zeros():
    assert canPlaceFlowers([0,0,0,0], 2) is True, "Four zeros flowerbed should accept 2 flowers"
from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_n_zero():
    assert canPlaceFlowers([1,0,1], 0) is True, "n=0 should always return True"

def test_single_zero():
    assert canPlaceFlowers([0], 1) is True, "Single 0 flowerbed should accommodate 1 flower"

def test_multiple_placements():
    assert canPlaceFlowers([0,0,0,0,0], 2) is True, "Should place 2 flowers in extended empty bed"
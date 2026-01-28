from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) == True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) == False, "Example 2 should return False"

def test_edge_two_zeros():
    assert canPlaceFlowers([0, 0], 1) == True, "Should plant 1 flower in [0,0]"

def test_edge_single_zero():
    assert canPlaceFlowers([0], 1) == True, "Should plant 1 flower in [0]"

def test_edge_max_placement():
    assert canPlaceFlowers([0,0,0,0,0], 2) == True, "Should plant 2 flowers in [0,0,0,0,0]"
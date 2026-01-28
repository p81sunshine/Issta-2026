from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) == True, "Should return True for 1 flower placement"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) == False, "Should return False for 2 flowers placement"

def test_edge_case_1():
    assert canPlaceFlowers([0], 1) == True, "Should handle single 0 flowerbed correctly"

def test_edge_case_2():
    assert canPlaceFlowers([0,0], 1) == True, "Should handle two 0s flowerbed correctly"

def test_multiple_placement():
    assert canPlaceFlowers([0,0,0,0], 2) == True, "Should allow 2 flowers in 4-slot flowerbed"
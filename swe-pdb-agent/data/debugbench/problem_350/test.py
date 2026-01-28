from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_single_flowerbed():
    assert canPlaceFlowers([1], 1) is False, "Single existing flower with n=1 should return False"

def test_middle_no_spots():
    assert canPlaceFlowers([1,0,1], 1) is False, "Flowerbed with 1,0,1 and n=1 should return False"

def test_zero_flower_needed():
    assert canPlaceFlowers([0,0,0], 0) is True, "n=0 should always return True regardless of flowerbed"
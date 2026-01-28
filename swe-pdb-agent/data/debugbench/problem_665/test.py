from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 failed"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 failed"

def test_single_zero():
    assert canPlaceFlowers([0], 1) is True, "Single zero flowerbed test failed"

def test_two_zeros():
    assert canPlaceFlowers([0, 0], 1) is True, "Two zeros flowerbed test failed"

def test_three_zeros_n2():
    assert canPlaceFlowers([0, 0, 0], 2) is True, "Three zeros with n=2 test failed"
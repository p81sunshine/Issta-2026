from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_buggy_elif_case():
    assert canPlaceFlowers([1,0,0,1], 1) is False, "Buggy code incorrectly decrements n for existing flowers"

def test_single_zero():
    assert canPlaceFlowers([0], 1) is True, "Single zero flowerbed should accommodate 1 flower"

def test_two_zeros():
    assert canPlaceFlowers([0,0], 1) is True, "Two zeros can place 1 flower"
from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_buggy_logic():
    assert canPlaceFlowers([1], 1) is False, "Buggy code incorrectly decrements n for existing flowers"

def test_n_zero():
    assert canPlaceFlowers([1,0,1], 0) is True, "n=0 should always return True"

def test_max_placement():
    assert canPlaceFlowers([0,0,0,0,0], 3) is True, "Should plant 3 flowers in a 5-element all-zero bed"
from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_single_zero():
    assert canPlaceFlowers([0], 1) is True, "Single spot should allow 1 flower"

def test_blocked_by_next():
    assert canPlaceFlowers([0,0,0,1,0,0,0], 1) is True, "Should allow flower placement despite nearby existing flower"

def test_middle_blocked():
    assert canPlaceFlowers([0,0,1,0,0], 1) is True, "Should handle mid-blocked scenarios"
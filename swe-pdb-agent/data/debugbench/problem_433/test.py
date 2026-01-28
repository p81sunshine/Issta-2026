from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_invalid_subtraction_case():
    assert canPlaceFlowers([0,1,0], 1) is False, "Buggy code incorrectly subtracts n for existing flowers"

def test_single_flower_placement():
    assert canPlaceFlowers([0], 1) is True, "Should place single flower in empty bed"

def test_cannot_place_with_existing_flower():
    assert canPlaceFlowers([1], 1) is False, "Buggy code incorrectly counts existing flowers as valid placements"
from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) == True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) == False, "Example 2 should return False"

def test_n_zero_case():
    assert canPlaceFlowers([1,0,1], 0) == True, "n=0 should always return True"

def test_single_zero():
    assert canPlaceFlowers([0], 1) == True, "Single plot can plant one flower"

def test_three_zeros_n2():
    assert canPlaceFlowers([0,0,0], 2) == True, "Three zeros can accommodate two flowers"
from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_edge_case_1():
    assert canPlaceFlowers([0], 1) is True, "Single zero flowerbed should accept one flower"

def test_edge_case_2():
    assert canPlaceFlowers([0,0], 1) is True, "Two zeros flowerbed should accept one flower"

def test_edge_case_3():
    assert canPlaceFlowers([0,0,0], 1) is True, "Three zeros flowerbed should accept one flower"
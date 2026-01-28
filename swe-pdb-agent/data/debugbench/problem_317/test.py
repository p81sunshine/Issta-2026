from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) is True, "Example 1 should return True"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) is False, "Example 2 should return False"

def test_edge_case_1():
    assert canPlaceFlowers([0,0], 1) is True, "Edge case [0,0] with n=1 should return True"

def test_edge_case_2():
    assert canPlaceFlowers([0,0,0,0], 2) is True, "Edge case [0,0,0,0] with n=2 should return True"

def test_edge_case_3():
    assert canPlaceFlowers([0], 1) is True, "Single 0 flowerbed should accept one flower"
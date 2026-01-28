from solution import *

def test_example_1():
    assert canPlaceFlowers([1,0,0,0,1], 1) == True, "Example 1 failed"

def test_example_2():
    assert canPlaceFlowers([1,0,0,0,1], 2) == False, "Example 2 failed"

def test_edge_case_single_zero():
    assert canPlaceFlowers([0], 1) == True, "Single zero flowerbed should allow 1 flower"

def test_bug_exposed_case():
    assert canPlaceFlowers([0,0,0,1,0,0,0], 2) == True, "Buggy code should fail this logical check"

def test_large_edge_case():
    assert canPlaceFlowers([0,0,0,0,0,0,0,0], 3) == True, "Should plant 3 flowers in a row"
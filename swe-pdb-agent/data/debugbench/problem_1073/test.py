from solution import *

def test_example_1():
    assert canThreePartsEqualSum([0,2,1,-6,6,-7,9,1,2,0,1]) is True, "Example 1 should return True"

def test_example_2():
    assert canThreePartsEqualSum([0,2,1,-6,6,7,9,-1,2,0,1]) is False, "Example 2 should return False"

def test_example_3():
    assert canThreePartsEqualSum([3,3,6,5,-2,2,5,1,-9,4]) is True, "Example 3 should return True"

def test_edge_case_1():
    assert canThreePartsEqualSum([5,5,5]) is True, "Edge case [5,5,5] should return True"

def test_edge_case_2():
    assert canThreePartsEqualSum([0,0,0,0]) is True, "Edge case [0,0,0,0] should return True"
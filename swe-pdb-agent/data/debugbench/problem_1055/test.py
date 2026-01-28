from solution import *

def test_example_1():
    # Test case from example 1
    arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    assert canThreePartsEqualSum(arr) == True, "Example 1 should return True"

def test_example_2():
    # Test case from example 2
    arr = [0,2,1,-6,6,7,9,-1,2,0,1]
    assert canThreePartsEqualSum(arr) == False, "Example 2 should return False"

def test_example_3():
    # Test case from example 3
    arr = [3,3,6,5,-2,2,5,1,-9,4]
    assert canThreePartsEqualSum(arr) == True, "Example 3 should return True"

def test_edge_case_empty():
    # Edge case: empty array
    arr = []
    assert canThreePartsEqualSum(arr) == False, "Empty array should return False"

def test_edge_case_single_element():
    # Edge case: single element
    arr = [1]
    assert canThreePartsEqualSum(arr) == False, "Single element array should return False"
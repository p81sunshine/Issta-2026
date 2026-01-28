from solution import *

def test_example_1():
    # Provided example with true output
    arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    assert canThreePartsEqualSum(arr) is True, "Example 1 should return True"

def test_example_2():
    # Provided example with false output
    arr = [0,2,1,-6,6,7,9,-1,2,0,1]
    assert canThreePartsEqualSum(arr) is False, "Example 2 should return False"

def test_example_3():
    # Third provided example with true output
    arr = [3,3,6,5,-2,2,5,1,-9,4]
    assert canThreePartsEqualSum(arr) is True, "Example 3 should return True"

def test_edge_case_short():
    # Edge case with minimal array that should return True
    arr = [1, -1, 0]
    total = sum(arr)
    if total % 3 != 0:
        assert canThreePartsEqualSum(arr) is False
    else:
        assert canThreePartsEqualSum(arr) is False, "Short array edge case should return False"

def test_edge_case_large():
    # Large array with valid three parts
    arr = [1] * 9  # [1,1,1,1,1,1,1,1,1], sum is 9 → each_sum is 3
    assert canThreePartsEqualSum(arr) is True, "Large array should return True"
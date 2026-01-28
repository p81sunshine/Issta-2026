from solution import *

def test_example_1():
    nums = [1,2,1,2,1,3,3]
    k = 2
    expected = 8
    assert minCost(nums, k) == expected, f"Test case 1 failed: expected {expected}, got {minCost(nums, k)}"

def test_example_2():
    nums = [1,2,1,2,1]
    k = 2
    expected = 6
    assert minCost(nums, k) == expected, f"Test case 2 failed: expected {expected}, got {minCost(nums, k)}"

def test_example_3():
    nums = [1,2,1,2,1]
    k = 5
    expected = 10
    assert minCost(nums, k) == expected, f"Test case 3 failed: expected {expected}, got {minCost(nums, k)}"

def test_case_custom():
    nums = [1,1,1]
    k = 2
    expected = 5
    assert minCost(nums, k) == expected, f"Custom test case failed: expected {expected}, got {minCost(nums, k)}"
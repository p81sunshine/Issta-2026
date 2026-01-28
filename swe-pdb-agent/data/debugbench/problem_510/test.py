from solution import *

def test_example_1():
    arr = [2, 3, 4, 7, 11]
    k = 5
    assert findKthPositive(arr, k) == 9, "Example 1 failed"

def test_example_2():
    arr = [1, 2, 3, 4]
    k = 2
    assert findKthPositive(arr, k) == 6, "Example 2 failed"

def test_single_element_missing():
    arr = [2]
    k = 1
    assert findKthPositive(arr, k) == 1, "Test single element with missing number failed"

def test_all_present_but_k():
    arr = [1]
    k = 1
    assert findKthPositive(arr, k) == 2, "Test when array has all numbers up to 1"

def test_multiple_missing_start():
    arr = [3, 4]
    k = 1
    assert findKthPositive(arr, k) == 1, "Test when multiple missing numbers at start"
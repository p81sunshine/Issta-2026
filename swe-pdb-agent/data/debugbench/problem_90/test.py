from solution import *

def test_example_1():
    assert minimumOperations([1,5,0,3,5]) == 3, "Example 1 failed"

def test_example_2():
    assert minimumOperations([0]) == 0, "Example 2 failed"

def test_edge_case_multiple_zeros():
    assert minimumOperations([2,2,2,0,0]) == 1, "Edge case with duplicates and zeros failed"

def test_all_non_zero_unique():
    assert minimumOperations([10, 20, 30]) == 3, "All unique non-zero elements test failed"
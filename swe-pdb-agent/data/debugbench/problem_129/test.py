from solution import *

def test_example_1():
    assert makeSubKSumEqual([1,4,1,3], 2) == 1, "Example 1 should return 1"

def test_example_2():
    assert makeSubKSumEqual([2,5,5,7], 3) == 5, "Example 2 should return 5"

def test_case_3():
    assert makeSubKSumEqual([1,2,3,4], 2) == 4, "Test case 3 with K=2 should return 4"

def test_edge_case_k_1():
    assert makeSubKSumEqual([3,1], 1) == 2, "Edge case with K=1 should return 2"

def test_single_element():
    assert makeSubKSumEqual([5], 1) == 0, "Single element case should return 0"
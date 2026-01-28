from solution import *

def test_example_1():
    assert findValueOfPartition([1,3,2,4]) == 1, "Example 1 failed"

def test_example_2():
    assert findValueOfPartition([100,1,10]) == 9, "Example 2 failed"

def test_edge_two_elements():
    assert findValueOfPartition([5, 10]) == 5, "Two elements edge case failed"

def test_all_same_elements():
    assert findValueOfPartition([3,3,3]) == 0, "All same elements case failed"
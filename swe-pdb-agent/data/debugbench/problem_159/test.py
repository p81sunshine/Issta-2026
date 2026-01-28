from solution import *

def test_example_1():
    assert minCost([1,2,1,2,1,3,3], 2) == 8, "Failed on example 1"

def test_example_2():
    assert minCost([1,2,1,2,1], 2) == 6, "Failed on example 2"

def test_example_3():
    assert minCost([1,2,1,2,1], 5) == 10, "Failed on example 3"

def test_edge_case_duplicate_elements():
    assert minCost([1,1], 1) == 2, "Failed on edge case with duplicates"
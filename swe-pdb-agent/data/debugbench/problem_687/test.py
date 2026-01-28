from solution import *

def test_example_1():
    assert closestCost([1,7], [3,4], 10) == 10, "Example 1 failed"

def test_example_2():
    assert closestCost([2,3], [4,5,100], 18) == 17, "Example 2 failed"

def test_example_3():
    assert closestCost([3,10], [2,5], 9) == 8, "Example 3 failed"

def test_edge_case_exact_match():
    assert closestCost([5], [], 5) == 5, "Exact match edge case failed"
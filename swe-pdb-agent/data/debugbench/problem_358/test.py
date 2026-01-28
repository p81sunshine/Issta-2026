from solution import *

def test_example_1():
    assert minimumTime([1,2,3], 5) == 3, "Example 1 failed"

def test_example_2():
    assert minimumTime([2], 1) == 2, "Example 2 failed"

def test_edge_case_two_buses():
    assert minimumTime([5,5], 2) == 5, "Edge case with two buses failed"

def test_edge_case_early_return():
    assert minimumTime([3,5,7], 10) == 15, "Edge case requiring cumulative trips failed"

def test_edge_case_multiple_with_early_return():
    assert minimumTime([1,1], 3) == 2, "Edge case with multiple small trips failed"
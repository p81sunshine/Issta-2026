from solution import *

def test_example_1():
    assert minimumTime([1,2,3], 5) == 3, "Example 1 should return 3"

def test_example_2():
    assert minimumTime([2], 1) == 2, "Example 2 should return 2"

def test_edge_case_large_trips():
    assert minimumTime([1], 1000000) == 1000000, "Edge case with large trips should return 1,000,000"
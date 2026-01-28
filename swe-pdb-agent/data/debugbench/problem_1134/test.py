from solution import *

def test_example_1():
    assert maxPower([1,2,4,5,0], 1, 2) == 5, "Example 1 should return 5"

def test_example_2():
    assert maxPower([4,4,4,4], 0, 3) == 4, "Example 2 should return 4"

def test_edge_case_n1():
    assert maxPower([3], 0, 0) == 3, "Edge case with single station should return 3"

def test_case_range_bug():
    assert maxPower([1,1], 1, 0) == 2, "Buggy range should fail this test case"
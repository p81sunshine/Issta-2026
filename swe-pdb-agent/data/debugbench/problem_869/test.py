from solution import *

def test_example_1():
    assert third_max([3,2,1]) == 1, "Example 1 failed: should return third distinct max"

def test_example_2():
    assert third_max([1,2]) == 2, "Example 2 failed: should return max when less than 3 distinct values"

def test_example_3():
    assert third_max([2,2,3,1]) == 1, "Example 3 failed: should handle duplicates correctly"

def test_more_than_three_distinct():
    assert third_max([5,5,4,4,3,3,2,2,1]) == 3, "Failed for list with more than three distinct elements"

def test_edge_case_single_element():
    assert third_max([5]) == 5, "Edge case with single element failed"
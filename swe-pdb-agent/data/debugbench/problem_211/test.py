from solution import *

def test_example_1():
    assert secondGreaterElement([2,4,0,9,6]) == [9,6,6,-1,-1], "Example 1 failed"

def test_example_2():
    assert secondGreaterElement([3,3]) == [-1,-1], "Example 2 failed"

def test_case_1():
    assert secondGreaterElement([1,2,3]) == [3,-1,-1], "Test case [1,2,3] failed"

def test_case_2():
    assert secondGreaterElement([4,5,2,25]) == [25, -1, -1, -1], "Test case [4,5,2,25] failed"

def test_edge_case_single_element():
    assert secondGreaterElement([10]) == [-1], "Single element edge case failed"
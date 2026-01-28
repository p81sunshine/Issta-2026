from solution import *

def test_example_1():
    assert jump([2,3,1,1,4]) == 2, "Test case 1 failed"

def test_example_2():
    assert jump([2,3,0,1,4]) == 2, "Test case 2 failed"

def test_edge_case_single_element():
    assert jump([5]) == 0, "Single element edge case failed"

def test_case_3():
    assert jump([1,1,1,1]) == 3, "Test case 3 failed"

def test_case_4():
    assert jump([2,1,2,0,4]) == 2, "Test case 4 failed"
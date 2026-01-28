from solution import *

def test_example_1():
    assert jump([2,3,1,1,4]) == 2, "Failed for example 1"

def test_example_2():
    assert jump([2,3,0,1,4]) == 2, "Failed for example 2"

def test_edge_case_index_error():
    assert jump([1,1,1]) == 2, "Failed for index out-of-range case"

def test_edge_case_2():
    assert jump([1,2,1]) == 2, "Failed for second edge case"

def test_single_element():
    assert jump([0]) == 0, "Failed for single-element input"
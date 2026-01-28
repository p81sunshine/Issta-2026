from solution import *

def test_example_1():
    assert find_middle_index([2,3,-1,8,4]) == 3, "Failed for example 1"

def test_example_2():
    assert find_middle_index([1,-1,4]) == 2, "Failed for example 2"

def test_example_3():
    assert find_middle_index([2,5]) == -1, "Failed for example 3"

def test_edge_single_element():
    assert find_middle_index([5]) == 0, "Failed for single-element array"

def test_standard_case():
    assert find_middle_index([1,7,3,6,5,6]) == 3, "Failed for standard test case"
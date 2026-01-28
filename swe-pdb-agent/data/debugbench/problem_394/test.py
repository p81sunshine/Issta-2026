from solution import *

def test_example_1():
    assert subArrayRanges([1,2,3]) == 4, "Failed for example 1: [1,2,3]"

def test_example_2():
    assert subArrayRanges([1,3,3]) == 4, "Failed for example 2: [1,3,3]"

def test_example_3():
    assert subArrayRanges([4,-2,-3,4,1]) == 59, "Failed for example 3: [4,-2,-3,4,1]"

def test_edge_case_single_element():
    assert subArrayRanges([5]) == 0, "Failed for single element case"

def test_edge_case_all_same_elements():
    assert subArrayRanges([2,2,2]) == 0, "Failed for all same elements case"
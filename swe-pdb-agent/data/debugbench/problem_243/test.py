from solution import *

def test_example_1():
    assert pivotArray([9,12,5,10,14,3,10], 10) == [9,5,3,10,10,12,14], "Failed example 1: incorrect partitioning"

def test_example_2():
    assert pivotArray([-3,4,3,2], 2) == [-3,2,4,3], "Failed example 2: incorrect pivot handling"

def test_single_element():
    assert pivotArray([5], 5) == [5], "Failed single-element case"

def test_index_error_in_buggy_code():
    assert pivotArray([10, 2, 5], 10) == [2,5,10], "Buggy code would raise IndexError here"

def test_all_elements_equal():
    assert pivotArray([3,3,3], 3) == [3,3,3], "Failed all-equal case"
from solution import *

def test_example_1():
    assert maximumGap([3,6,9,1]) == 3, "Failed for example 1: maximum gap calculation"

def test_example_2():
    assert maximumGap([10]) == 0, "Failed for example 2: single element case"

def test_two_elements():
    assert maximumGap([3, 5]) == 2, "Failed for two elements case"

def test_multiple_elements():
    assert maximumGap([1, 3, 5, 9]) == 4, "Failed for multiple elements with max in the end"

def test_equal_differences():
    assert maximumGap([5, 10, 15]) == 5, "Failed for equal differences case"
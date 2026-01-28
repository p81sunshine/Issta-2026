from solution import *

def test_example_1():
    assert find_lhs([1,3,2,2,5,2,3,7]) == 5, "Failed for example 1"

def test_example_2():
    assert find_lhs([1,2,3,4]) == 2, "Failed for example 2"

def test_example_3():
    assert find_lhs([1,1,1,1]) == 0, "Failed for example 3"

def test_buggy_case_1():
    assert find_lhs([1,2,2,3]) == 3, "Failed for consecutive pair (2,3)"

def test_buggy_case_2():
    assert find_lhs([3,3,4]) == 3, "Failed for (3,4) pair"

def test_buggy_case_3():
    assert find_lhs([1,1,3,3]) == 0, "Failed to reject non-consecutive pairs"
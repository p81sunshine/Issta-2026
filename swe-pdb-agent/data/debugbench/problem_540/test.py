from solution import *

def test_example_1():
    assert distributeCandies([1,1,2,2,3,3]) == 3, "Example 1 failed"

def test_example_2():
    assert distributeCandies([1,1,2,3]) == 2, "Example 2 failed"

def test_example_3():
    assert distributeCandies([6,6,6,6]) == 1, "Example 3 failed"

def test_case_set_larger_than_half():
    assert distributeCandies([1,2,3,4]) == 2, "Set size larger than half failed"

def test_case_set_smaller_than_half():
    assert distributeCandies([1,1,1,1,2,2]) == 2, "Set size smaller than half failed"
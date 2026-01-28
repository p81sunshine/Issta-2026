from solution import *

def test_example_1():
    assert smaller_numbers_than_current([8,1,2,2,3]) == [4,0,1,1,3], "Example 1 failed"

def test_example_2():
    assert smaller_numbers_than_current([6,5,4,8]) == [2,1,0,3], "Example 2 failed"

def test_example_3():
    assert smaller_numbers_than_current([7,7,7,7]) == [0,0,0,0], "Example 3 failed"

def test_single_element():
    assert smaller_numbers_than_current([5]) == [0], "Single element test failed"

def test_all_zeros():
    assert smaller_numbers_than_current([0,0,0]) == [0,0,0], "All zeros test failed"
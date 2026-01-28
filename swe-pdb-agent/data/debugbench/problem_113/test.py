from solution import *

def test_example_1():
    assert smaller_numbers_than_current([8,1,2,2,3]) == [4,0,1,1,3], "Example 1 failed"

def test_example_2():
    assert smaller_numbers_than_current([6,5,4,8]) == [2,1,0,3], "Example 2 failed"

def test_example_3():
    assert smaller_numbers_than_current([7,7,7,7]) == [0,0,0,0], "Example 3 failed"

def test_edge_case_100():
    assert smaller_numbers_than_current([100]) == [0], "Edge case with 100 failed"
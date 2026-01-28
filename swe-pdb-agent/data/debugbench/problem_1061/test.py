from solution import *

def test_example_1():
    nums = [2,4,0,9,6]
    expected = [9,6,6,-1,-1]
    assert secondGreaterElement(nums) == expected, "Example 1 failed"

def test_example_2():
    nums = [3,3]
    expected = [-1,-1]
    assert secondGreaterElement(nums) == expected, "Example 2 failed"

def test_case_1_3_2():
    nums = [1,3,2]
    expected = [2, -1, -1]
    assert secondGreaterElement(nums) == expected, "Test case [1,3,2] failed"

def test_case_1_2_3_4_5():
    nums = [1,2,3,4,5]
    expected = [3,4,5,-1,-1]
    assert secondGreaterElement(nums) == expected, "Test case [1,2,3,4,5] failed"
from solution import *

def test_example_1():
    nums = [2,0,2,1,1,0]
    sortColors(nums)
    assert nums == [0,0,1,1,2,2], "Example 1 failed"

def test_example_2():
    nums = [2,0,1]
    sortColors(nums)
    assert nums == [0,1,2], "Example 2 failed"

def test_case_1_2_0():
    nums = [1,2,0]
    sortColors(nums)
    assert nums == [0,1,2], "Test case [1,2,0] failed"

def test_case_1_2_2_0():
    nums = [1,2,2,0]
    sortColors(nums)
    assert nums == [0,1,2,2], "Test case [1,2,2,0] failed"

def test_single_element():
    nums = [1]
    sortColors(nums)
    assert nums == [1], "Single element test failed"
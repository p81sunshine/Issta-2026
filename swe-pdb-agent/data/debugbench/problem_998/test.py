from solution import *

def test_example_1():
    nums = [0, 1, 0, 3, 12]
    moveZeroes(nums)
    assert nums == [1, 3, 12, 0, 0], "Test case 1 failed: [0,1,0,3,12]"

def test_example_2():
    nums = [0]
    moveZeroes(nums)
    assert nums == [0], "Test case 2 failed: [0]"

def test_case_multiple_zeros():
    nums = [0, 2, 0, 3]
    moveZeroes(nums)
    assert nums == [2, 3, 0, 0], "Test case multiple zeros failed"

def test_case_mixed():
    nums = [1, 0, 2, 0, 3]
    moveZeroes(nums)
    assert nums == [1, 2, 3, 0, 0], "Test case mixed elements failed"

def test_no_zeros():
    nums = [1, 2, 3]
    moveZeroes(nums)
    assert nums == [1, 2, 3], "Test case no zeros failed"
from solution import *

def test_example_1():
    nums = [0,1,0,3,12]
    moveZeroes(nums)
    assert nums == [1,3,12,0,0], "Failed example 1"

def test_example_2():
    nums = [0]
    moveZeroes(nums)
    assert nums == [0], "Failed example 2"

def test_case_3():
    nums = [0,1,2]
    moveZeroes(nums)
    assert nums == [1,2,0], "Test case 3 failed"

def test_case_4():
    nums = [0,2,1]
    moveZeroes(nums)
    assert nums == [2,1,0], "Test case 4 failed"
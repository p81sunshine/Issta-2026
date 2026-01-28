from solution import *

def test_example_1():
    nums = [2,3,1,5,4]
    assert maxValueAfterReverse(nums) == 10, "Failed for example 1"

def test_example_2():
    nums = [2,4,9,24,2,1,10]
    assert maxValueAfterReverse(nums) == 68, "Failed for example 2"

def test_two_elements():
    nums = [1, 2]
    assert maxValueAfterReverse(nums) == 1, "Failed for two elements case"

def test_flat_array():
    nums = [1, 0, 1]
    assert maxValueAfterReverse(nums) == 2, "Failed for flat array case"

def test_all_same():
    nums = [5, 5, 5]
    assert maxValueAfterReverse(nums) == 0, "Failed for all same elements case"
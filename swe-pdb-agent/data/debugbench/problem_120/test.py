from solution import *

def test_example_1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert search(nums, target) == 4, "Failed to find existing target in array"

def test_example_2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    assert search(nums, target) == -1, "Returned incorrect index for non-existing target"

def test_single_element_found():
    nums = [5]
    target = 5
    assert search(nums, target) == 0, "Failed to find single element in array"

def test_two_elements_last_element():
    nums = [3, 5]
    target = 5
    assert search(nums, target) == 1, "Failed to find last element in two-element array"

def test_three_elements_middle():
    nums = [1, 3, 5]
    target = 3
    assert search(nums, target) == 1, "Failed to find middle element in three-element array"
from solution import *

def test_example_1():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert search(nums, target) == 4, "Should return index 4 for target 9"

def test_example_2():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    assert search(nums, target) == -1, "Should return -1 for missing target 2"

def test_single_element_present():
    nums = [5]
    target = 5
    assert search(nums, target) == 0, "Should return index 0 for single-element array"

def test_duplicates():
    nums = [2, 2, 2]
    target = 2
    assert search(nums, target) == 0, "Should return index 0 for first occurrence in duplicates"

def test_last_element():
    nums = [1, 3, 5]
    target = 5
    assert search(nums, target) == 2, "Should return index 2 for last element"
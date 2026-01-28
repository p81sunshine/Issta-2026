from solution import *

def test_example_1():
    nums = [2,10,7,5,4,1,8,6]
    assert minimum_deletions(nums) == 5, "Example 1 failed"

def test_example_2():
    nums = [0,-4,19,1,8,-2,-3,5]
    assert minimum_deletions(nums) == 3, "Example 2 failed"

def test_example_3():
    nums = [101]
    assert minimum_deletions(nums) == 1, "Example 3 failed"

def test_case_two_elements():
    nums = [1, 2]
    assert minimum_deletions(nums) == 2, "Two-element case failed"

def test_case_min_and_max_adjacent():
    nums = [3, 1, 2]
    assert minimum_deletions(nums) == 2, "Adjacent min/max case failed"
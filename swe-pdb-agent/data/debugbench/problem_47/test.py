from solution import *

def test_example_1():
    nums = [2,10,7,5,4,1,8,6]
    assert minimum_deletions(nums) == 5, "Example 1 should return 5 deletions"

def test_example_2():
    nums = [0,-4,19,1,8,-2,-3,5]
    assert minimum_deletions(nums) == 3, "Example 2 should return 3 deletions"

def test_example_3():
    nums = [101]
    assert minimum_deletions(nums) == 1, "Single-element array should require 1 deletion"

def test_two_elements_min_max():
    nums = [3, 1]
    assert minimum_deletions(nums) == 2, "Two elements array should require 2 deletions"

def test_min_max_overlap():
    nums = [5, 5, 5]
    assert minimum_deletions(nums) == 1, "All elements equal should require 1 deletion"
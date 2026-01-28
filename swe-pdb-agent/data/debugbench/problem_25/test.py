from solution import *

def test_example_1():
    nums = ["777","7","77","77"]
    target = "7777"
    assert num_of_pairs(nums, target) == 4, "Example 1 failed"

def test_example_2():
    nums = ["123","4","12","34"]
    target = "1234"
    assert num_of_pairs(nums, target) == 2, "Example 2 failed"

def test_example_3():
    nums = ["1","1","1"]
    target = "11"
    assert num_of_pairs(nums, target) == 6, "Example 3 failed"

def test_no_valid_splits():
    nums = ["abc", "def"]
    target = "xyz"
    assert num_of_pairs(nums, target) == 0, "No valid splits should return 0"

def test_single_character_target():
    nums = ["a"]
    target = "a"
    assert num_of_pairs(nums, target) == 0, "Target length 1 should return 0"
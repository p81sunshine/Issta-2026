from solution import *

def test_example_1():
    nums = ["777","7","77","77"]
    target = "7777"
    expected = 4
    assert numOfPairs(nums, target) == expected

def test_example_2():
    nums = ["123","4","12","34"]
    target = "1234"
    expected = 2
    assert numOfPairs(nums, target) == expected

def test_example_3():
    nums = ["1","1","1"]
    target = "11"
    expected = 6
    assert numOfPairs(nums, target) == expected

def test_no_valid_pairs():
    nums = ["abc", "def"]
    target = "xyz"
    expected = 0
    assert numOfPairs(nums, target) == expected

def test_single_element_insufficient():
    nums = ["a"]
    target = "aa"
    expected = 0
    assert numOfPairs(nums, target) == expected
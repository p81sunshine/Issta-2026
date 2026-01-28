from solution import *

def test_example_1():
    nums = [3,5,2,3]
    expected = 7
    actual = minPairSum(nums)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_example_2():
    nums = [3,5,4,2,4,6]
    expected = 8
    actual = minPairSum(nums)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_two_elements():
    nums = [1,2]
    expected = 3
    actual = minPairSum(nums)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_all_same_elements():
    nums = [5,5,5,5]
    expected = 10
    actual = minPairSum(nums)
    assert actual == expected, f"Expected {expected} but got {actual}"

def test_sorted_input():
    nums = [1,2,3,4]
    expected = 5
    actual = minPairSum(nums)
    assert actual == expected, f"Expected {expected} but got {actual}"
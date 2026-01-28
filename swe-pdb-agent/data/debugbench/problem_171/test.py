from solution import *

def test_example_1():
    nums = [10, 6, 5, 8]
    expected = [10, 8]
    actual = findLonely(nums)
    assert sorted(actual) == sorted(expected), f"Expected {expected} but got {actual}"

def test_example_2():
    nums = [1, 3, 5, 3]
    expected = [1, 5]
    actual = findLonely(nums)
    assert sorted(actual) == sorted(expected), f"Expected {expected} but got {actual}"

def test_consecutive_numbers():
    nums = [2, 3]
    expected = []
    actual = findLonely(nums)
    assert sorted(actual) == sorted(expected), f"Expected {expected} but got {actual}"

def test_single_element():
    nums = [5]
    expected = [5]
    actual = findLonely(nums)
    assert sorted(actual) == sorted(expected), f"Expected {expected} but got {actual}"

def test_non_consecutive_but_present():
    nums = [3, 5]
    expected = [3, 5]
    actual = findLonely(nums)
    assert sorted(actual) == sorted(expected), f"Expected {expected} but got {actual}"
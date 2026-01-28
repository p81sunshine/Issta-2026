from solution import *

def test_example_1():
    nums = [2, 3, 5]
    expected = [4, 3, 5]
    assert getSumAbsoluteDifferences(nums) == expected, f"Failed for example 1: {nums}"

def test_example_2():
    nums = [1, 4, 6, 8, 10]
    expected = [24, 15, 13, 15, 21]
    assert getSumAbsoluteDifferences(nums) == expected, f"Failed for example 2: {nums}"

def test_single_element():
    nums = [5]
    expected = [0]
    assert getSumAbsoluteDifferences(nums) == expected, f"Failed for single element case: {nums}"

def test_all_same_elements():
    nums = [3, 3, 3]
    expected = [0, 0, 0]
    assert getSumAbsoluteDifferences(nums) == expected, f"Failed for all same elements case: {nums}"

def test_two_elements():
    nums = [1, -1]
    expected = [2, 2]
    assert getSumAbsoluteDifferences(nums) == expected, f"Failed for two elements case: {nums}"
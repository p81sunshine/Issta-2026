from solution import *

def test_example_1():
    assert plusOne([1,2,3]) == [1,2,4], "Example 1 failed: [1,2,3] should return [1,2,4]"

def test_example_2():
    assert plusOne([4,3,2,1]) == [4,3,2,2], "Example 2 failed: [4,3,2,1] should return [4,3,2,2]"

def test_example_3():
    assert plusOne([9]) == [1,0], "Example 3 failed: [9] should return [1,0]"

def test_single_digit_less_than_9():
    assert plusOne([1]) == [2], "Buggy logic returns empty list for single-digit input < 10"

def test_zero_input():
    assert plusOne([0]) == [1], "Edge case [0] should return [1] but returns empty list in buggy code"
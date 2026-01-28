from solution import *

def test_example_1():
    nums = [7,52,2,4]
    expected = 596
    actual = findTheArrayConcVal(nums)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_2():
    nums = [5,14,13,8,12]
    expected = 673
    actual = findTheArrayConcVal(nums)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_single_element():
    nums = [5]
    expected = 5
    actual = findTheArrayConcVal(nums)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_two_elements():
    nums = [1, 2]
    expected = 12
    actual = findTheArrayConcVal(nums)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_odd_length():
    nums = [1, 2, 3]
    expected = 15
    actual = findTheArrayConcVal(nums)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_empty_list():
    nums = []
    expected = 0
    actual = findTheArrayConcVal(nums)
    assert actual == expected, f"Expected {expected}, got {actual}"
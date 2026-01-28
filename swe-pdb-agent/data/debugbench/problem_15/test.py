from solution import *

def test_example_1():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    result = median_sliding_window(nums, k)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_2():
    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k = 3
    expected = [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
    result = median_sliding_window(nums, k)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_even_window():
    nums = [1, 2, 3, 4]
    k = 2
    expected = [1.5, 2.5, 3.5]
    result = median_sliding_window(nums, k)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_single_element():
    nums = [5, 4, 3, 2, 1]
    k = 1
    expected = [5.0, 4.0, 3.0, 2.0, 1.0]
    result = median_sliding_window(nums, k)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_duplicate_elements():
    nums = [2, 2, 2, 2]
    k = 2
    expected = [2.0, 2.0, 2.0]
    result = median_sliding_window(nums, k)
    assert result == expected, f"Expected {expected}, but got {result}"
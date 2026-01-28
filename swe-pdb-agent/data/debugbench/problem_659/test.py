from solution import *

def test_example_1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"Test example 1 failed: expected {expected}, got {result}"

def test_example_2():
    nums = [1,2,3,4,2,3,1,4,2]
    k = 3
    expected = [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"Test example 2 failed: expected {expected}, got {result}"

def test_even_window_size():
    nums = [1,2,3,4]
    k = 2
    expected = [1.5, 2.5, 3.5]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"Even window size test failed: expected {expected}, got {result}"

def test_single_element_window():
    nums = [5, 3, 8]
    k = 1
    expected = [5.0, 3.0, 8.0]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"Single element window test failed: expected {expected}, got {result}"

def test_all_elements_same():
    nums = [2,2,2,2]
    k = 2
    expected = [2.0, 2.0, 2.0]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"All elements same test failed: expected {expected}, got {result}"
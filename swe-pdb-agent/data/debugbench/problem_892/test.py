from solution import *

def test_example_1():
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    assert median_sliding_window(nums, k) == expected, "Example 1 failed"

def test_example_2():
    nums = [1, 2, 3, 4, 2, 3, 1, 4, 2]
    k = 3
    expected = [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
    assert median_sliding_window(nums, k) == expected, "Example 2 failed"

def test_edge_case_k_1():
    nums = [5]
    k = 1
    expected = [5.0]
    assert median_sliding_window(nums, k) == expected, "k=1 case failed"

def test_even_window_median():
    nums = [4, 3, 2, 1]
    k = 2
    expected = [3.5, 2.5, 1.5]
    assert median_sliding_window(nums, k) == expected, "Even window median failed"

def test_same_elements():
    nums = [2, 2, 2, 2]
    k = 2
    expected = [2.0, 2.0, 2.0]
    assert median_sliding_window(nums, k) == expected, "Same elements case failed"
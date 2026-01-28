from solution import *

def test_example_1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    expected = [1.0,-1.0,-1.0,3.0,5.0,6.0]
    assert median_sliding_window(nums, k) == expected, "Example 1 failed"

def test_example_2():
    nums = [1,2,3,4,2,3,1,4,2]
    k = 3
    expected = [2.0,3.0,3.0,3.0,2.0,3.0,2.0]
    assert median_sliding_window(nums, k) == expected, "Example 2 failed"

def test_edge_case_k1():
    nums = [5, 3, 8, 2]
    k = 1
    expected = [5.0, 3.0, 8.0, 2.0]
    assert median_sliding_window(nums, k) == expected, "k=1 case failed"

def test_even_k_case():
    nums = [1,2,3,4]
    k = 2
    expected = [1.5, 2.5, 3.5]
    assert median_sliding_window(nums, k) == expected, "Even k case failed"

def test_all_same_elements():
    nums = [2,2,2,2,2]
    k = 3
    expected = [2.0, 2.0, 2.0]
    assert median_sliding_window(nums, k) == expected, "All same elements case failed"
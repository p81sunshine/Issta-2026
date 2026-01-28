from solution import *

def test_example_1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    assert medianSlidingWindow(nums, k) == expected, "Example 1 failed"

def test_example_2():
    nums = [1,2,3,4,2,3,1,4,2]
    k = 3
    expected = [2.0,3.0,3.0,3.0,2.0,3.0,2.0]
    assert medianSlidingWindow(nums, k) == expected, "Example 2 failed"

def test_edge_case_k1():
    nums = [5]
    k = 1
    expected = [5.0]
    assert medianSlidingWindow(nums, k) == expected, "k=1 case failed"

def test_even_k():
    nums = [1,2,3,4]
    k = 2
    expected = [1.5, 2.5, 3.5]
    assert medianSlidingWindow(nums, k) == expected, "Even k case failed"

def test_sliding_window_removal():
    nums = [5,2,3,4]
    k = 2
    expected = [3.5, 2.5, 3.5]
    assert medianSlidingWindow(nums, k) == expected, "Sliding window removal failed"
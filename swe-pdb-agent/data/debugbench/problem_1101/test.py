from solution import *

def test_example_1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"Failed for example 1: expected {expected}, got {result}"

def test_example_2():
    nums = [1,2,3,4,2,3,1,4,2]
    k = 3
    expected = [2.0, 3.0, 3.0, 3.0, 2.0, 3.0, 2.0]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"Failed for example 2: expected {expected}, got {result}"

def test_edge_case_k1():
    nums = [5]
    k = 1
    expected = [5.0]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"Failed for k=1 case: expected {expected}, got {result}"

def test_even_window_size():
    nums = [1,2,3,4]
    k = 2
    expected = [1.5, 2.5, 3.5]
    result = medianSlidingWindow(nums, k)
    assert result == expected, f"Failed for even window size: expected {expected}, got {result}"
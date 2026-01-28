from solution import *

def test_example_1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    assert medianSlidingWindow(nums, k) == expected, "Failed for example 1"

def test_example_2():
    nums = [1,2,3,4,2,3,1,4,2]
    k = 3
    expected = [2.0,3.0,3.0,3.0,2.0,3.0,2.0]
    assert medianSlidingWindow(nums, k) == expected, "Failed for example 2"

def test_even_k():
    nums = [1,2,3,4]
    k = 2
    expected = [1.5, 2.5, 3.5]
    assert medianSlidingWindow(nums, k) == expected, "Failed for even k case"

def test_k_1():
    nums = [5,3,4,2,1]
    k = 1
    expected = [5.0,3.0,4.0,2.0,1.0]
    assert medianSlidingWindow(nums, k) == expected, "Failed for k=1 case"

def test_duplicates():
    nums = [5,5,5,5]
    k = 2
    expected = [5.0,5.0,5.0]
    assert medianSlidingWindow(nums, k) == expected, "Failed for duplicate values"
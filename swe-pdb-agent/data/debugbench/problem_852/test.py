from solution import *
from pytest import approx

def test_example_1():
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    expected = [1.0, -1.0, -1.0, 3.0, 5.0, 6.0]
    assert medianSlidingWindow(nums, k) == approx(expected), "Failed first example"

def test_example_2():
    nums = [1,2,3,4,2,3,1,4,2]
    k = 3
    expected = [2.0,3.0,3.0,3.0,2.0,3.0,2.0]
    assert medianSlidingWindow(nums, k) == approx(expected), "Failed second example"

def test_k_2_case():
    nums = [1,2,3,4]
    k = 2
    expected = [1.5, 2.5, 3.5]
    assert medianSlidingWindow(nums, k) == approx(expected), "Failed k=2 index error case"

def test_k_1_case():
    nums = [5, 1, 3]
    k = 1
    expected = [5.0, 1.0, 3.0]
    assert medianSlidingWindow(nums, k) == approx(expected), "Failed k=1 edge case"

def test_full_window():
    nums = [1,2,3,4]
    k = 4
    expected = [2.5]
    assert medianSlidingWindow(nums, k) == approx(expected), "Failed full window case"
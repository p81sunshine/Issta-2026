from solution import *

def test_example_1():
    assert findPeakElement([1, 2, 3, 1]) == 2, "Should return index 2 for [1,2,3,1]"

def test_example_2():
    assert findPeakElement([1, 2, 1, 3, 5, 6, 4]) == 5, "Should return index 5 for [1,2,1,3,5,6,4]"

def test_single_element():
    assert findPeakElement([5]) == 0, "Should return 0 for single-element list"

def test_two_elements_increasing():
    assert findPeakElement([1, 2]) == 1, "Should return 1 for [1,2]"

def test_strictly_increasing():
    assert findPeakElement([1, 2, 3, 4, 5, 6, 7]) == 6, "Should return 6 for strictly increasing list"
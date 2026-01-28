from solution import *

def test_example_1():
    assert findPeakElement([1,2,3,1]) == 2, "Example 1 should return index 2"

def test_example_2():
    result = findPeakElement([1,2,1,3,5,6,4])
    assert result in {1, 5}, f"Example 2 should return either 1 or 5, got {result}"

def test_strictly_increasing():
    assert findPeakElement([1,2,3,4,5]) == 4, "Strictly increasing array should return last index"

def test_strictly_decreasing():
    assert findPeakElement([5,4,3,2,1]) == 0, "Strictly decreasing array should return first index"

def test_single_element():
    assert findPeakElement([7]) == 0, "Single element array should return 0"
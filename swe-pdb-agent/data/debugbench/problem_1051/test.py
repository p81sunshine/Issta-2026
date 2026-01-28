from solution import *

def test_example_1():
    nums = [1,2,3,1]
    assert findPeakElement(nums) == 2, "Example 1 should return index 2"

def test_example_2():
    nums = [1,2,1,3,5,6,4]
    output = findPeakElement(nums)
    assert output in {1, 5}, f"Example 2 should return either 1 or 5, got {output}"

def test_strictly_increasing():
    nums = [1,2,3,4]
    assert findPeakElement(nums) == 3, "Strictly increasing array should return last index"

def test_peak_at_end():
    nums = [2,1,3]
    assert findPeakElement(nums) == 2, "Peak at end should return index 2"

def test_single_element():
    nums = [5]
    assert findPeakElement(nums) == 0, "Single element array should return 0"
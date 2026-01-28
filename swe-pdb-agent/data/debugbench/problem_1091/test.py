from solution import *

def test_example_1():
    nums = [2, 0, 2, 1, 1, 0]
    sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2], "Example 1 failed"

def test_example_2():
    nums = [2, 0, 1]
    sortColors(nums)
    assert nums == [0, 1, 2], "Example 2 failed"

def test_single_element():
    nums = [2]
    sortColors(nums)
    assert nums == [2], "Single element test failed"

def test_all_zeros():
    nums = [0, 0, 0]
    sortColors(nums)
    assert nums == [0, 0, 0], "All zeros test failed"

def test_mixed_values():
    nums = [1, 2, 0]
    sortColors(nums)
    assert nums == [0, 1, 2], "Mixed values test failed"
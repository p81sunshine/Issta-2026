from solution import *

def test_example_1():
    nums = [-2, 0, 3, -5, 2, -1]
    prefix = num_array(nums)
    assert sum_range(prefix, 0, 2) == 1, "Failed for sumRange [0, 2]"

def test_example_2():
    nums = [-2, 0, 3, -5, 2, -1]
    prefix = num_array(nums)
    assert sum_range(prefix, 2, 5) == -1, "Failed for sumRange [2, 5]"

def test_example_3():
    nums = [-2, 0, 3, -5, 2, -1]
    prefix = num_array(nums)
    assert sum_range(prefix, 0, 5) == -3, "Failed for sumRange [0, 5]"

def test_single_element():
    nums = [5]
    prefix = num_array(nums)
    assert sum_range(prefix, 0, 0) == 5, "Failed for single-element array"

def test_full_range():
    nums = [1, 2, 3]
    prefix = num_array(nums)
    assert sum_range(prefix, 0, 2) == 6, "Failed for full range sum"
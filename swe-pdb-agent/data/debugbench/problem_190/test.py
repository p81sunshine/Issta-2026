from solution import *

def test_example_1():
    nums = [4,4,4,5,6]
    assert valid_partition(nums) is True, "Failed for [4,4,4,5,6]"

def test_example_2():
    nums = [1,1,1,2]
    assert valid_partition(nums) is False, "Failed for [1,1,1,2]"

def test_consecutive_increasing():
    nums = [3,4,5]
    assert valid_partition(nums) is True, "Failed for [3,4,5]"

def test_edge_case_two_equal():
    nums = [2,2]
    assert valid_partition(nums) is True, "Failed for [2,2]"

def test_edge_case_three_consecutive():
    nums = [1,2,3]
    assert valid_partition(nums) is True, "Failed for [1,2,3]"
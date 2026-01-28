from solution import *

def test_example_1():
    arr = [0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]
    assert can_three_parts_equal_sum(arr) is True, "Should return True for valid 3 partitions"

def test_example_2():
    arr = [0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]
    assert can_three_parts_equal_sum(arr) is False, "Should return False for invalid partitions"

def test_example_3():
    arr = [3, 3, 6, 5, -2, 2, 5, 1, -9, 4]
    assert can_three_parts_equal_sum(arr) is True, "Should return True for valid 3 partitions"

def test_edge_case_small_valid():
    arr = [1, 1, 1]
    assert can_three_parts_equal_sum(arr) is True, "3 elements with equal sum should return True"

def test_edge_case_sum_not_divisible():
    arr = [1, 2, 3, 4]
    assert can_three_parts_equal_sum(arr) is False, "Total sum not divisible by 3 should return False"
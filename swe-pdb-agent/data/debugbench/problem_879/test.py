from solution import *

def test_example_1():
    arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    assert can_three_parts_equal_sum(arr) is True, "Example 1 should return True"

def test_example_2():
    arr = [0,2,1,-6,6,7,9,-1,2,0,1]
    assert can_three_parts_equal_sum(arr) is False, "Example 2 should return False"

def test_example_3():
    arr = [3,3,6,5,-2,2,5,1,-9,4]
    assert can_three_parts_equal_sum(arr) is True, "Example 3 should return True"

def test_case_sum_not_divisible():
    arr = [1, 2, 3]
    assert can_three_parts_equal_sum(arr) is False, "Sum 6 not divisible by 3"

def test_case_three_elements():
    arr = [1, 1, 1]
    assert can_three_parts_equal_sum(arr) is True, "Valid 3-part split"
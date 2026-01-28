from solution import *

def test_example_1():
    arr = [0,2,1,-6,6,-7,9,1,2,0,1]
    expected = True
    actual = can_three_parts_equal_sum(arr)
    assert actual == expected, "Example 1 should return True"

def test_example_2():
    arr = [0,2,1,-6,6,7,9,-1,2,0,1]
    expected = False
    actual = can_three_parts_equal_sum(arr)
    assert actual == expected, "Example 2 should return False"

def test_example_3():
    arr = [3,3,6,5,-2,2,5,1,-9,4]
    expected = True
    actual = can_three_parts_equal_sum(arr)
    assert actual == expected, "Example 3 should return True"

def test_third_part_at_end():
    arr = [1, 1, 0, 1]
    expected = True
    actual = can_three_parts_equal_sum(arr)
    assert actual == expected, "Third part at end should return True"

def test_insufficient_elements():
    arr = [3, 3]
    expected = False
    actual = can_three_parts_equal_sum(arr)
    assert actual == expected, "Not enough elements for third part"
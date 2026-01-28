from solution import *

def test_example_1():
    assert does_valid_array_exist([1,1,0]) is True, "Example 1 should return True"

def test_example_2():
    assert does_valid_array_exist([1,1]) is True, "Example 2 should return True"

def test_example_3():
    assert does_valid_array_exist([1,0]) is False, "Example 3 should return False"

def test_all_zeros():
    assert does_valid_array_exist([0,0]) is True, "All zeros case should return True"

def test_alternating_1_0():
    assert does_valid_array_exist([1,0,1,0]) is True, "Alternating 1 and 0 case should return True"
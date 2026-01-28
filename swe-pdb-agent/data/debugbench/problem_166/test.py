from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True, "Example 1 should return True"

def test_example_2():
    assert isTransformable("34521", "23415") is True, "Example 2 should return True"

def test_example_3():
    assert isTransformable("12345", "12435") is False, "Example 3 should return False"

def test_descending_order():
    assert isTransformable("123", "321") is False, "Descending order transformation should be impossible"

def test_duplicate_digits():
    assert isTransformable("112", "121") is False, "Duplicate digits case should return False"
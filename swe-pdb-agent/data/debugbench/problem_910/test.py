from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True, "Example 1 should return True"

def test_example_2():
    assert isTransformable("34521", "23415") is True, "Example 2 should return True"

def test_example_3():
    assert isTransformable("12345", "12435") is False, "Example 3 should return False"

def test_equal_strings():
    assert isTransformable("123", "123") is True, "Equal strings should return True"

def test_impossible_descending():
    assert isTransformable("123", "321") is False, "Descending order transformation should be impossible"
from solution import *

def test_example_1():
    assert is_transformable("84532", "34852") is True, "Example 1 failed"

def test_example_2():
    assert is_transformable("34521", "23415") is True, "Example 2 failed"

def test_example_3():
    assert is_transformable("12345", "12435") is False, "Example 3 failed"

def test_same_string():
    assert is_transformable("12345", "12345") is True, "Same string should return True"

def test_different_length():
    assert is_transformable("123", "1234") is False, "Different lengths should return False"
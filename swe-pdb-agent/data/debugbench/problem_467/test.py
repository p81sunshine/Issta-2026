from solution import *

def test_example_1():
    assert is_transformable("84532", "34852") is True, "Example 1 should return True"

def test_example_2():
    assert is_transformable("34521", "23415") is True, "Example 2 should return True"

def test_example_3():
    assert is_transformable("12345", "12435") is False, "Example 3 should return False"

def test_edge_same_strings():
    assert is_transformable("12345", "12345") is True, "Identical strings should return True"

def test_edge_mismatched_characters():
    assert is_transformable("abc", "abd") is False, "Different character sets should return False"
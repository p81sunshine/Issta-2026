from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True, "Example 1 should return True"

def test_example_2():
    assert isTransformable("34521", "23415") is True, "Example 2 should return True"

def test_example_3():
    assert isTransformable("12345", "12435") is False, "Example 3 should return False"

def test_edge_case_empty_strings():
    assert isTransformable("", "") is True, "Empty strings should be transformable"

def test_edge_case_identical_strings():
    assert isTransformable("123", "123") is True, "Identical strings should return True"

def test_edge_case_simple_swap():
    assert isTransformable("21", "12") is True, "Simple two-element swap should be possible"
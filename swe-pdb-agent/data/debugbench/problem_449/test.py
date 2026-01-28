from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True, "Example 1 failed"

def test_example_2():
    assert isTransformable("34521", "23415") is True, "Example 2 failed"

def test_example_3():
    assert isTransformable("12345", "12435") is False, "Example 3 failed"

def test_edge_case_same_string():
    assert isTransformable("12345", "12345") is True, "Same string should return True"

def test_edge_case_mismatched_characters():
    assert isTransformable("123", "124") is False, "Different characters should return False"
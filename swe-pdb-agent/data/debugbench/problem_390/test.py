from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True, "Example 1 failed"

def test_example_2():
    assert isTransformable("34521", "23415") is True, "Example 2 failed"

def test_example_3():
    assert isTransformable("12345", "12435") is False, "Example 3 failed"

def test_edge_case_identical():
    assert isTransformable("123", "123") is True, "Identical strings test failed"
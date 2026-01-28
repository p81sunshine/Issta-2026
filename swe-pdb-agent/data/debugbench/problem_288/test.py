from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True, "Example 1 should return True"

def test_example_2():
    assert isTransformable("34521", "23415") is True, "Example 2 should return True"

def test_example_3():
    assert isTransformable("12345", "12435") is False, "Example 3 should return False"

def test_edge_case_1():
    assert isTransformable("0", "0") is True, "Edge case with single digit should return True"

def test_edge_case_2():
    assert isTransformable("10", "01") is True, "Edge case with digit swap should return True"
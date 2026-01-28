from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True, "Example 1 should return True"

def test_example_2():
    assert isTransformable("34521", "23415") is True, "Example 2 should return True"

def test_example_3():
    assert isTransformable("12345", "12435") is False, "Example 3 should return False"

def test_same_string():
    assert isTransformable("12345", "12345") is True, "Identical strings should return True"
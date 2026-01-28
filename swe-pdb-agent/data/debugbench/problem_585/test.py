from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True

def test_example_2():
    assert isTransformable("34521", "23415") is True

def test_example_3():
    assert isTransformable("12345", "12435") is False

def test_identical_strings():
    assert isTransformable("12345", "12345") is True

def test_mismatched_characters():
    assert isTransformable("123", "124") is False
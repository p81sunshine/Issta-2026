from solution import *

def test_example_1():
    assert is_transformable("84532", "34852") is True

def test_example_2():
    assert is_transformable("34521", "23415") is True

def test_example_3():
    assert is_transformable("12345", "12435") is False

def test_same_string():
    assert is_transformable("123", "123") is True

def test_different_lengths():
    assert is_transformable("123", "1234") is False
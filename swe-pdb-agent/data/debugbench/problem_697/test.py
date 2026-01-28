from solution import *

def test_example_1():
    assert isTransformable("84532", "34852") is True

def test_example_2():
    assert isTransformable("34521", "23415") is True

def test_example_3():
    assert isTransformable("12345", "12435") is False

def test_same_strings():
    assert isTransformable("123", "123") is True

def test_reverse_order():
    assert isTransformable("21", "12") is True
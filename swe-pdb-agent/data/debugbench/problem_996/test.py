from solution import *

def test_example_1():
    assert doesValidArrayExist([1,1,0]) is True, "Failed for [1,1,0]"

def test_example_2():
    assert doesValidArrayExist([1,1]) is True, "Failed for [1,1]"

def test_example_3():
    assert doesValidArrayExist([1,0]) is False, "Failed for [1,0]"

def test_single_element_zero():
    assert doesValidArrayExist([0]) is True, "Failed for [0]"

def test_single_element_one():
    assert doesValidArrayExist([1]) is False, "Failed for [1]"
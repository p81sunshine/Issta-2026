from solution import *

def test_example_1():
    assert checkValidString("()") is True, "Input: () should return True"

def test_example_2():
    assert checkValidString("(*)") is True, "Input: (*) should return True"

def test_example_3():
    assert checkValidString("(*))") is True, "Input: (*)) should return True"

def test_case_1():
    assert checkValidString("(()*") is True, "Input: (()* should return True when star can act as left parenthesis"

def test_case_2():
    assert checkValidString("(*()") is True, "Input: (*() should return True when star can act as left or empty"
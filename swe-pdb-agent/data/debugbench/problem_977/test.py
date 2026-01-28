from solution import *

def test_example_1():
    assert checkValidString("()") is True, "Failed for input '()'"

def test_example_2():
    assert checkValidString("(*)") is True, "Failed for input '(*)'"

def test_example_3():
    assert checkValidString("(*))") is True, "Failed for input '(*))'"

def test_star_as_closing_parenthesis():
    assert checkValidString("(*") is True, "Failed for input '(*'"

def test_mixed_parentheses_and_stars():
    assert checkValidString("(*()") is True, "Failed for input '(*()'"

def test_unbalanced_parenthesis():
    assert checkValidString("(") is False, "Failed for input '('"
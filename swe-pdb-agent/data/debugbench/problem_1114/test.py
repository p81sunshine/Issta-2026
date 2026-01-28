from solution import *

def test_example_1():
    assert checkValidString("()") is True, "Failed for input '()'"
    
def test_example_2():
    assert checkValidString("(*)") is True, "Failed for input '(*)'"
    
def test_example_3():
    assert checkValidString("(*))") is True, "Failed for input '(*))'"

def test_empty_string():
    assert checkValidString("") is True, "Failed for empty string"

def test_all_stars():
    assert checkValidString("***") is True, "Failed for all stars"

def test_invalid_case():
    assert checkValidString(")(") is False, "Failed for invalid input ')('"
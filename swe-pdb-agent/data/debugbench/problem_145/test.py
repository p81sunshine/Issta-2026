from solution import *

def test_example_1():
    assert checkValidString("()") == True, "Example 1 failed"

def test_example_2():
    assert checkValidString("(*)") == True, "Example 2 failed"

def test_example_3():
    assert checkValidString("(*))") == True, "Example 3 failed"

def test_case_4():
    assert checkValidString("(()*") == True, "Test case for position-based matching failure in buggy code"

def test_case_5():
    assert checkValidString("(*()") == True, "Test case for incorrect star-parenthesis ordering in buggy code"
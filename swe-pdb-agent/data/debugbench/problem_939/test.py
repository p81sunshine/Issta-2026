from solution import *

def test_example_1():
    assert checkValidString("()") == True, "Example 1 failed"

def test_example_2():
    assert checkValidString("(*)") == True, "Example 2 failed"

def test_example_3():
    assert checkValidString("(*))") == True, "Example 3 failed"

def test_case_4():
    assert checkValidString("(*") == True, "Test case with single left parenthesis and star failed"

def test_case_5():
    assert checkValidString("((*)") == True, "Test case with nested parenthesis and star failed"
from solution import *

def test_example_1():
    assert canConstruct("a", "b") is False, "Example 1 failed"

def test_example_2():
    assert canConstruct("aa", "ab") is False, "Example 2 failed"

def test_example_3():
    assert canConstruct("aa", "aab") is True, "Example 3 failed"

def test_extra_case_1():
    assert canConstruct("aa", "a") is False, "Extra case 1 failed (buggy code would return True here)"

def test_extra_case_2():
    assert canConstruct("abc", "abcc") is True, "Extra case 2 failed (buggy code would return False here)"
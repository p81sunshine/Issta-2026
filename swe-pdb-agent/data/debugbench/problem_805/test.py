from solution import *

def test_example_1():
    assert checkAlmostEquivalent("aaaa", "bccb") is False, "Example 1 failed"

def test_example_2():
    assert checkAlmostEquivalent("abcdeef", "abaaacc") is True, "Example 2 failed"

def test_example_3():
    assert checkAlmostEquivalent("cccddabba", "babababab") is True, "Example 3 failed"

def test_buggy_case_1():
    assert checkAlmostEquivalent("", "aaaa") is False, "Buggy case 1 failed"

def test_buggy_case_2():
    assert checkAlmostEquivalent("a", "bbbbb") is False, "Buggy case 2 failed"
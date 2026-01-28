from solution import *

def test_example_1():
    assert checkAlmostEquivalent("aaaa", "bccb") is False, "Example 1 failed"

def test_example_2():
    assert checkAlmostEquivalent("abcdeef", "abaaacc") is True, "Example 2 failed"

def test_example_3():
    assert checkAlmostEquivalent("cccddabba", "babababab") is True, "Example 3 failed"

def test_high_word1_same():
    # Buggy returns False, correct returns True
    assert checkAlmostEquivalent("aaaa", "aaaa") is True, "High word1 frequency test failed"

def test_high_word2_only():
    # Buggy returns True, correct returns False
    assert checkAlmostEquivalent("", "aaaa") is False, "High word2 frequency test failed"
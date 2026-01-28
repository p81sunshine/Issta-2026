from solution import *

def test_example_1():
    assert checkAlmostEquivalent("aaaa", "bccb") is False, "Example 1 failed"

def test_example_2():
    assert checkAlmostEquivalent("abcdeef", "abaaacc") is True, "Example 2 failed"

def test_example_3():
    assert checkAlmostEquivalent("cccddabba", "babababab") is True, "Example 3 failed"

def test_case_excess_in_word2():
    assert checkAlmostEquivalent("aaa", "dddd") is False, "Buggy code should fail for excess characters in word2"

def test_case_b_char_disbalance():
    assert checkAlmostEquivalent("a", "bbbb") is False, "Buggy code should fail for 'b' disbalance"
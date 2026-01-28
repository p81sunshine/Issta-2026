from solution import *

def test_example_1():
    assert checkAlmostEquivalent("aaaa", "bccb") is False, "Example 1 failed"

def test_example_2():
    assert checkAlmostEquivalent("abcdeef", "abaaacc") is True, "Example 2 failed"

def test_example_3():
    assert checkAlmostEquivalent("cccddabba", "babababab") is True, "Example 3 failed"

def test_edge_case_diff_exactly_3():
    assert checkAlmostEquivalent("aaa", "") is True, "Difference of exactly 3 should be allowed"

def test_edge_case_diff_exceeds_3():
    assert checkAlmostEquivalent("aaaa", "") is False, "Difference of 4 should be disallowed"
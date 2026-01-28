from solution import *

def test_example_1():
    assert checkAlmostEquivalent("aaaa", "bccb") is False, "Example 1 should return False"

def test_example_2():
    assert checkAlmostEquivalent("abcdeef", "abaaacc") is True, "Example 2 should return True"

def test_example_3():
    assert checkAlmostEquivalent("cccddabba", "babababab") is True, "Example 3 should return True"

def test_a_b_mismatch():
    assert checkAlmostEquivalent("aaaa", "bbbb") is False, "Test case with a/b index shift should return False"

def test_edge_case_exact_limit():
    assert checkAlmostEquivalent("aaa", "") is True, "Edge case with exact 3 difference should return True"
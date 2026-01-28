from solution import *

def test_example_1():
    assert smallestString("cbabc") == "baabc", "Example 1 failed: should decrement 'c' to 'b' and 'b' to 'a'"

def test_example_2():
    assert smallestString("acbbc") == "abaab", "Example 2 failed: should process non-a substring correctly"

def test_example_3():
    assert smallestString("leetcode") == "kddsbncd", "Example 3 failed: should decrement all characters except leading a's"

def test_edge_case_all_a():
    assert smallestString("aaaa") == "aaaz", "All a's case failed: should replace last a with z"

def test_edge_case_single_a():
    assert smallestString("a") == "z", "Single 'a' case failed: should transform to 'z'"

def test_edge_case_single_z():
    assert smallestString("z") == "y", "Single 'z' case failed: should decrement to 'y'"

def test_mixed_case():
    assert smallestString("ab") == "aa", "Mixed 'ab' case failed: should decrement 'b' to 'a'"
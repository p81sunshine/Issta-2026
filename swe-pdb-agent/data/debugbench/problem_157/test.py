from solution import *

def test_example_1():
    assert kSimilarity("ab", "ba") == 1, "Example 1 failed"

def test_example_2():
    assert kSimilarity("abc", "bca") == 2, "Example 2 failed"

def test_case_1():
    assert kSimilarity("abac", "baac") == 1, "Test case with swapped positions and equality check failed"

def test_case_2():
    assert kSimilarity("abc", "cba") == 1, "Test case with direct swap required failed"

def test_edge_case():
    assert kSimilarity("abc", "abc") == 0, "Edge case with identical inputs failed"
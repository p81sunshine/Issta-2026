from solution import *

def test_example_1():
    assert kSimilarity("ab", "ba") == 1, "Example 1 failed"

def test_example_2():
    assert kSimilarity("abc", "bca") == 2, "Example 2 failed"

def test_identical_strings():
    assert kSimilarity("abcd", "abcd") == 0, "Identical strings should return 0"

def test_no_solution():
    assert kSimilarity("abc", "acb") == 1, "Should require 1 swap for 'abc'->'acb'"

def test_longer_string():
    assert kSimilarity("abcdef", "fedcba") >= 3, "Long string should require multiple swaps"
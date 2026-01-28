from solution import *

def test_example_1():
    assert longestSubstring("aaabb", 3) == 3, "Example 1: 'aaabb', k=3 should return 3"

def test_example_2():
    assert longestSubstring("ababbc", 2) == 5, "Example 2: 'ababbc', k=2 should return 5"

def test_k_1_case():
    assert longestSubstring("aa", 1) == 2, "Case where x=2 and k=1 should return 2"

def test_k_zero_case():
    assert longestSubstring("abc", 0) == 3, "Edge case with k=0 should return full length"

def test_x_less_than_k():
    assert longestSubstring("a", 2) == 0, "Case where x=1 < k=2 should return 0"
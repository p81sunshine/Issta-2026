from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_filtered_s1():
    assert get_max_repetitions("abc", 2, "ac", 1) == 2, "Filtered s1 calculation failed"

def test_n1_zero():
    assert get_max_repetitions("abc", 0, "ab", 1) == 0, "n1=0 edge case failed"

def test_s2_not_subset():
    assert get_max_repetitions("abc", 5, "abd", 1) == 0, "s2 not subset check failed"
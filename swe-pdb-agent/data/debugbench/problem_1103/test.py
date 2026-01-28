from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1

def test_missing_characters():
    assert get_max_repetitions("abc", 3, "abcd", 1) == 0

def test_cycle_case():
    assert get_max_repetitions("aba", 2, "ab", 1) == 2

def test_zero_n1():
    assert get_max_repetitions("a", 0, "a", 1) == 0
from solution import *

def test_example_1():
    assert get_max_repetitions("acb", 4, "ab", 2) == 2, "Example 1 should return 2"

def test_example_2():
    assert get_max_repetitions("acb", 1, "acb", 1) == 1, "Example 2 should return 1"

def test_edge_case_not_subset():
    assert get_max_repetitions("a", 3, "ab", 1) == 0, "s2 has character not in s1, should return 0"

def test_cycle_case():
    assert get_max_repetitions("ab", 3, "ab", 2) == 1, "Cycle case should return 1"
from solution import get_max_repetitions as getMaxRepetitions

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2, "Example 1 failed"

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1, "Example 2 failed"

def test_s2_not_subset():
    assert getMaxRepetitions("abc", 3, "abd", 1) == 0, "s2 not subset case failed"

def test_n1_zero():
    assert getMaxRepetitions("a", 0, "a", 1) == 0, "n1=0 case failed"

def test_no_cycle_case():
    assert getMaxRepetitions("ab", 2, "ab", 1) == 2, "No cycle case failed"
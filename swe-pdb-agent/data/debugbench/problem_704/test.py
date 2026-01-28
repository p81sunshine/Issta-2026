from solution import *

def test_example_1():
    assert getMaxRepetitions("acb", 4, "ab", 2) == 2

def test_example_2():
    assert getMaxRepetitions("acb", 1, "acb", 1) == 1

def test_return_early_condition():
    assert getMaxRepetitions("a", 1, "a", 1) == 1

def test_s2_not_subset():
    assert getMaxRepetitions("a", 3, "ab", 1) == 0

def test_n1_zero():
    assert getMaxRepetitions("abc", 0, "abc", 1) == 0
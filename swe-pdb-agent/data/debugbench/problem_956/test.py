from solution import *

def test_example_1():
    assert are_almost_equal("bank", "kanb") is True, "Should return True for swappable strings"

def test_example_2():
    assert are_almost_equal("attack", "defend") is False, "Should return False for non-swappable strings"

def test_example_3():
    assert are_almost_equal("kelb", "kelb") is True, "Should return True for identical strings"

def test_empty_strings():
    assert are_almost_equal("", "") is True, "Should return True for empty strings"

def test_different_lengths():
    assert are_almost_equal("abc", "abcd") is False, "Should return False for different length strings"
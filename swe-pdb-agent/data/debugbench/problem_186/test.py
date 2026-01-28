from solution import *

def test_example_1():
    assert are_almost_equal("bank", "kanb") is True, "Should return True for two swapped characters"

def test_example_2():
    assert are_almost_equal("attack", "defend") is False, "Should return False when more than two differences"

def test_example_3():
    assert are_almost_equal("kelb", "kelb") is True, "Should return True for identical strings"

def test_swapped_pair():
    assert are_almost_equal("ab", "ba") is True, "Should return True for exactly two swapped characters"

def test_single_difference():
    assert are_almost_equal("a", "b") is False, "Should return False when there is one differing character"
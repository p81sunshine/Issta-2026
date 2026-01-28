from solution import *

def test_example_1():
    assert longestString(2, 5, 1) == 12, "Example 1 failed"

def test_example_2():
    assert longestString(3, 2, 2) == 14, "Example 2 failed"

def test_z_addition_case():
    assert longestString(2, 2, 3) == 14, "Z addition case failed"

def test_min_uses_2x_plus_1():
    assert longestString(3, 1, 5) == 16, "Min selection case failed"

def test_swap_and_z_case():
    assert longestString(5, 3, 2) == 18, "Swap and Z calculation failed"
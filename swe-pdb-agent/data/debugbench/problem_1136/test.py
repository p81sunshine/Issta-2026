from solution import *

def test_example_1():
    assert findMaxK([-1, 2, -3, 3]) == 3, "Example 1 should return 3"

def test_example_2():
    assert findMaxK([-1, 10, 6, 7, -7, 1]) == 7, "Example 2 should return 7"

def test_example_3():
    assert findMaxK([-10, 8, 6, 7, -2, -3]) == -1, "Example 3 should return -1"

def test_off_by_one_case():
    assert findMaxK([2, -2]) == 2, "Off-by-one case should return 2"

def test_no_valid_k_case():
    assert findMaxK([1, 2, 3]) == -1, "No valid k case should return -1"
from solution import *

def test_example_1():
    assert findMaxK([-1, 2, -3, 3]) == 3, "Example 1 failed"

def test_example_2():
    assert findMaxK([-1, 10, 6, 7, -7, 1]) == 7, "Example 2 failed"

def test_example_3():
    assert findMaxK([-10, 8, 6, 7, -2, -3]) == -1, "Example 3 failed"

def test_zero_case():
    assert findMaxK([0]) == 0, "Zero case failed"

def test_empty_list():
    assert findMaxK([]) == -1, "Empty list case failed"
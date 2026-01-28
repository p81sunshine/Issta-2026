from solution import *

def test_example_1():
    assert findMaxK([-1, 2, -3, 3]) == 3, "Example 1 should return 3"

def test_example_2():
    assert findMaxK([-1, 10, 6, 7, -7, 1]) == 7, "Example 2 should return 7"

def test_example_3():
    assert findMaxK([-10, 8, 6, 7, -2, -3]) == -1, "Example 3 should return -1"

def test_custom_case():
    assert findMaxK([2, 2, -1, 1]) == 1, "Custom case with [2,2,-1,1] should return 1"

def test_another_case():
    assert findMaxK([4, 4, -2, 2]) == 2, "Test case [4,4,-2,2] should return 2"
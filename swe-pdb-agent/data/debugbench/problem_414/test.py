from solution import *

def test_example_1():
    assert findMaxK([-1, 2, -3, 3]) == 3, "Should return 3 for [-1,2,-3,3]"

def test_example_2():
    assert findMaxK([-1, 10, 6, 7, -7, 1]) == 7, "Should return 7 for [-1,10,6,7,-7,1]"

def test_example_3():
    assert findMaxK([-10, 8, 6, 7, -2, -3]) == -1, "Should return -1 for [-10,8,6,7,-2,-3]"

def test_empty_list():
    assert findMaxK([]) == -1, "Should return -1 for empty list"

def test_zero_case():
    assert findMaxK([0, 0]) == 0, "Should return 0 for [0,0] as 0 and -0 are considered"
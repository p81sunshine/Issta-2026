from solution import *

def test_example_1():
    assert findMaxK([-1, 2, -3, 3]) == 3, "Should return 3 as the maximum valid k"

def test_example_2():
    assert findMaxK([-1, 10, 6, 7, -7, 1]) == 7, "Should return 7 as the maximum valid k"

def test_example_3():
    assert findMaxK([-10, 8, 6, 7, -2, -3]) == -1, "Should return -1 as no valid k exists"

def test_max_pair_selection():
    assert findMaxK([3, -3, 5, -5]) == 5, "Should return 5 as the maximum valid pair"
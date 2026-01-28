from solution import *

def test_example_1():
    assert findMaxK([-1, 2, -3, 3]) == 3, "Failed for example 1"

def test_example_2():
    assert findMaxK([-1, 10, 6, 7, -7, 1]) == 7, "Failed for example 2"

def test_example_3():
    assert findMaxK([-10, 8, 6, 7, -2, -3]) == -1, "Failed for example 3"

def test_max_not_first():
    assert findMaxK([1, -1, 4, -4]) == 4, "Failed for max not first element"

def test_empty_list():
    assert findMaxK([]) == -1, "Failed for empty list"
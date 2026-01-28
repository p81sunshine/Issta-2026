from solution import *

def test_example_1():
    assert findMaxK([-1, 2, -3, 3]) == 3

def test_example_2():
    assert findMaxK([-1, 10, 6, 7, -7, 1]) == 7

def test_example_3():
    assert findMaxK([-10, 8, 6, 7, -2, -3]) == -1

def test_single_element():
    assert findMaxK([5]) == -1

def test_positive_negative_pair():
    assert findMaxK([2, -2, 4]) == 2
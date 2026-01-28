from solution import *

def test_example_1():
    assert findMaxK([-1,2,-3,3]) == 3

def test_example_2():
    assert findMaxK([-1,10,6,7,-7,1]) == 7

def test_example_3():
    assert findMaxK([-10,8,6,7,-2,-3]) == -1

def test_case_with_correct_in_middle():
    assert findMaxK([3, -2, 2]) == 2

def test_case_zero():
    assert findMaxK([0]) == 0
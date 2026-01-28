from solution import *

def test_example_1():
    assert closest_cost([1,7], [3,4], 10) == 10

def test_example_2():
    assert closest_cost([2,3], [4,5,100], 18) == 17

def test_example_3():
    assert closest_cost([3,10], [2,5], 9) == 8

def test_tie_case():
    assert closest_cost([4,6], [], 5) == 4
from solution import *

def test_example_1():
    assert findTheArrayConcVal([7,52,2,4]) == 596, "Example 1 failed"

def test_example_2():
    assert findTheArrayConcVal([5,14,13,8,12]) == 673, "Example 2 failed"

def test_single_element():
    assert findTheArrayConcVal([13]) == 13, "Single element test failed"

def test_two_elements():
    assert findTheArrayConcVal([5,6]) == 56, "Two elements test failed"

def test_three_elements():
    assert findTheArrayConcVal([1,2,3]) == 15, "Three elements test failed"
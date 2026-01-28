from solution import *

def test_example_1():
    assert findTheArrayConcVal([7, 52, 2, 4]) == 596, "Failed for example 1"

def test_example_2():
    assert findTheArrayConcVal([5, 14, 13, 8, 12]) == 673, "Failed for example 2"

def test_single_element():
    assert findTheArrayConcVal([5]) == 5, "Failed for single element case"

def test_two_elements():
    assert findTheArrayConcVal([1, 2]) == 12, "Failed for two elements case"

def test_four_elements():
    assert findTheArrayConcVal([1, 2, 3, 4]) == 37, "Failed for four elements case"
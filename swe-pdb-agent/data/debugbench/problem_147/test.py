from solution import *

def test_example_1():
    assert findTheArrayConcVal([7,52,2,4]) == 596, "Should return 596 for [7,52,2,4]"

def test_example_2():
    assert findTheArrayConcVal([5,14,13,8,12]) == 673, "Should return 673 for [5,14,13,8,12]"

def test_single_element():
    assert findTheArrayConcVal([5]) == 5, "Should return 5 for single-element array"

def test_two_elements():
    assert findTheArrayConcVal([1,2]) == 12, "Should return 12 for two-element array"

def test_three_elements():
    assert findTheArrayConcVal([1,2,3]) == 15, "Should return 15 for three-element array [1,2,3]"
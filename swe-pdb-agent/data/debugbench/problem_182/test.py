from solution import *

def test_example_1():
    assert thirdMax([3, 2, 1]) == 1

def test_example_2():
    assert thirdMax([1, 2]) == 2

def test_example_3():
    assert thirdMax([2, 2, 3, 1]) == 1

def test_unique_len_2():
    assert thirdMax([5, 4, 4]) == 5, "Should return max when unique elements < 3"

def test_unique_len_1():
    assert thirdMax([5, 5, 5]) == 5, "Should return max when only one unique element"

def test_unique_len_4():
    assert thirdMax([5, 4, 3, 2]) == 3, "Should return third max when unique elements > 3"
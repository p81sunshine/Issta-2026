from solution import *

def test_example_1():
    assert sortArray([5,2,3,1]) == [1,2,3,5], "Example 1 failed"

def test_example_2():
    assert sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5], "Example 2 failed"

def test_single_element():
    assert sortArray([1]) == [1], "Single element test failed"

def test_all_same_elements():
    assert sortArray([2,2,2]) == [2,2,2], "All same elements test failed"

def test_negative_numbers():
    assert sortArray([-3, -1, -2]) == [-3, -2, -1], "Negative numbers test failed"
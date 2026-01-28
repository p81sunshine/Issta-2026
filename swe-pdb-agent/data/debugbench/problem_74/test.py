from solution import *

def test_example_1():
    assert sortArray([5,2,3,1]) == [1,2,3,5], "Example 1 failed"

def test_example_2():
    assert sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5], "Example 2 failed"

def test_empty_list():
    assert sortArray([]) == [], "Test with empty list failed"

def test_single_element():
    assert sortArray([42]) == [42], "Test with single element failed"

def test_already_sorted():
    assert sortArray([1,2,3,4]) == [1,2,3,4], "Test with already sorted list failed"
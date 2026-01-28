from solution import *

def test_example_1():
    assert sortArray([5,2,3,1]) == [1,2,3,5], "Example 1 failed"

def test_example_2():
    assert sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5], "Example 2 failed"

def test_duplicate_elements():
    assert sortArray([2,2,2]) == [2,2,2], "Failed on all duplicates"

def test_negative_numbers():
    assert sortArray([3,-1,0]) == [-1,0,3], "Failed with negative numbers"

def test_single_element():
    assert sortArray([42]) == [42], "Failed for single-element array"
from solution import *

def test_example_1():
    assert sortArray([5,2,3,1]) == [1,2,3,5], "Example 1 failed"

def test_example_2():
    assert sortArray([5,1,1,2,0,0]) == [0,0,1,1,2,5], "Example 2 failed"

def test_single_element():
    assert sortArray([3]) == [3], "Single element test failed"

def test_consecutive_elements():
    assert sortArray([2,3]) == [2,3], "Consecutive elements test failed"

def test_sorted_consecutive():
    assert sortArray([1,2,3,4]) == [1,2,3,4], "Sorted consecutive test failed"
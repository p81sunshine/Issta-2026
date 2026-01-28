from solution import *

def test_example_1():
    assert getSumAbsoluteDifferences([2,3,5]) == [4,3,5], "Example 1 failed"

def test_example_2():
    assert getSumAbsoluteDifferences([1,4,6,8,10]) == [24,15,13,15,21], "Example 2 failed"

def test_single_element():
    assert getSumAbsoluteDifferences([5]) == [0], "Single element test failed"

def test_two_elements():
    assert getSumAbsoluteDifferences([1,2]) == [1,1], "Two elements test failed"

def test_all_same_elements():
    assert getSumAbsoluteDifferences([3,3,3]) == [0,0,0], "All same elements test failed"
from solution import *

def test_example_1():
    assert maxDistance([1,1,1,6,1,1,1]) == 3, "Failed for example 1"

def test_example_2():
    assert maxDistance([1,8,3,8,3]) == 4, "Failed for example 2"

def test_example_3():
    assert maxDistance([0,1]) == 1, "Failed for example 3"

def test_all_same_colors():
    assert maxDistance([2,2,2]) == 0, "Failed for all same colors case"

def test_single_element():
    assert maxDistance([5]) == 0, "Failed for single element case"
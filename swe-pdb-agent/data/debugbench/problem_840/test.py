from solution import *

def test_example_1():
    assert countMaxOrSubsets([3,1]) == 2, "Failed for example 1"

def test_example_2():
    assert countMaxOrSubsets([2,2,2]) == 7, "Failed for example 2"

def test_example_3():
    assert countMaxOrSubsets([3,2,1,5]) == 6, "Failed for example 3"

def test_single_element():
    assert countMaxOrSubsets([5]) == 1, "Failed for single element case"

def test_all_zeros():
    assert countMaxOrSubsets([0,0]) == 3, "Failed for all zeros case"
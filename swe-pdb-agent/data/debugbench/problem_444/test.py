from solution import *

def test_example_1():
    assert maximumGap([3,6,9,1]) == 3, "Failed for example 1: maximum gap calculation"

def test_example_2():
    assert maximumGap([10]) == 0, "Failed for single-element case"

def test_two_elements():
    assert maximumGap([1, 2]) == 1, "Failed for two elements case"

def test_three_elements():
    assert maximumGap([1, 2, 4]) == 2, "Failed for three elements with max gap between last two"

def test_all_same_elements():
    assert maximumGap([5, 5, 5]) == 0, "Failed for all identical elements case"
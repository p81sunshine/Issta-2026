from solution import *

def test_example_1():
    assert maximumGap([3,6,9,1]) == 3, "Failed for example case 1"

def test_example_2():
    assert maximumGap([10]) == 0, "Failed for example case 2"

def test_two_elements():
    assert maximumGap([1, 2]) == 1, "Failed for two-element case"

def test_negative_numbers():
    assert maximumGap([5, -3, 8]) == 8, "Failed for negative numbers case"

def test_all_same_elements():
    assert maximumGap([5,5,5]) == 0, "Failed for all same elements case"
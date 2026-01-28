from solution import *

def test_example_1():
    assert maximumGap([3,6,9,1]) == 3, "Failed for example case with max gap 3"

def test_example_2():
    assert maximumGap([10]) == 0, "Failed for single-element input"

def test_two_elements():
    assert maximumGap([1, 2]) == 1, "Failed for two-element input"

def test_all_same_elements():
    assert maximumGap([5,5,5]) == 0, "Failed for all same elements"

def test_empty_list():
    assert maximumGap([]) == 0, "Failed for empty list"
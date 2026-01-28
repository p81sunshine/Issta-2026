from solution import *

def test_example_1():
    assert maximumGap([3,6,9,1]) == 3, "Failed for example 1"

def test_example_2():
    assert maximumGap([10]) == 0, "Failed for example 2"

def test_two_elements():
    assert maximumGap([10, 5]) == 5, "Failed for two elements case"

def test_max_in_first_pair():
    assert maximumGap([5, 8, 10]) == 3, "Failed when max gap is in first pair"

def test_all_same():
    assert maximumGap([2, 2, 2]) == 0, "Failed for all same elements case"
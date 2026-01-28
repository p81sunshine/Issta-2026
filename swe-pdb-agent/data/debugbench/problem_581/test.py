from solution import *

def test_example_1():
    assert maximumGap([3,6,9,1]) == 3, "Should return 3 for [3,6,9,1]"

def test_example_2():
    assert maximumGap([10]) == 0, "Should return 0 for single-element array"

def test_two_elements():
    assert maximumGap([1, 2]) == 1, "Should return 1 for two elements [1,2]"

def test_all_same_elements():
    assert maximumGap([5,5,5,5]) == 0, "Should return 0 for all same elements"

def test_larger_array():
    assert maximumGap([1, 4, 6, 10]) == 4, "Should return 4 for [1,4,6,10]"
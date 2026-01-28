from solution import *

def test_example_1():
    assert maximumGap([3,6,9,1]) == 3, "Failed for [3,6,9,1] with expected 3"

def test_example_2():
    assert maximumGap([10]) == 0, "Failed for [10] with expected 0"

def test_two_elements():
    assert maximumGap([1, 2]) == 1, "Failed for [1,2] with expected 1"

def test_multiple_gaps():
    assert maximumGap([1, 3, 6, 10]) == 4, "Failed for [1,3,6,10] with expected 4"

def test_empty_input():
    assert maximumGap([]) == 0, "Failed for empty list with expected 0"
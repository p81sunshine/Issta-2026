from solution import *

def test_example_1():
    assert averageValue([1,3,6,10,12,15]) == 9, "Example 1 failed"

def test_example_2():
    assert averageValue([1,2,4,7,10]) == 0, "Example 2 failed"

def test_mixed_numbers():
    assert averageValue([6, 7, 12]) == 9, "Mixed numbers test failed"

def test_partial_valid_numbers():
    assert averageValue([2, 4, 6]) == 6, "Only 6 is valid, average should be 6"

def test_empty_valid_list():
    assert averageValue([3, 5, 7]) == 0, "No valid numbers should return 0"
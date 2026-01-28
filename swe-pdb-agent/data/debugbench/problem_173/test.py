from solution import *

def test_example_1():
    assert minPairSum([3,5,2,3]) == 7, "Failed example 1: [3,5,2,3] should return 7"

def test_example_2():
    assert minPairSum([3,5,4,2,4,6]) == 8, "Failed example 2: [3,5,4,2,4,6] should return 8"

def test_buggy_case_1():
    assert minPairSum([1,3,3,3]) == 6, "Failed to handle correct pairing for [1,3,3,3]"

def test_buggy_case_2():
    assert minPairSum([1,2,2,2]) == 4, "Failed to handle correct pairing for [1,2,2,2]"
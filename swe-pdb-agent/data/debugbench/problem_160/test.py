from solution import *

def test_example_1():
    assert minOperations([2,3,2,4,3], [9,6,9,3,15]) == 2, "Example 1 should return 2"

def test_example_2():
    assert minOperations([4,3,6], [8,2,6,10]) == -1, "Example 2 should return -1"

def test_case_3():
    assert minOperations([2,4], [4,8,12]) == 0, "Test case where correct code returns 0 but buggy returns 1"

def test_case_4():
    assert minOperations([3,2], [2,3]) == -1, "Test case where correct code returns -1 but buggy returns 0"
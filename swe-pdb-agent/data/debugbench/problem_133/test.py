from solution import *

def test_example_1():
    assert isReachable(6, 9) is False, "Example 1 failed"

def test_example_2():
    assert isReachable(4, 7) is True, "Example 2 failed"

def test_case_2_2():
    assert isReachable(2, 2) is True, "Test case (2,2) failed"

def test_case_1_1():
    assert isReachable(1, 1) is True, "Test case (1,1) failed"

def test_case_8_8():
    assert isReachable(8, 8) is True, "Test case (8,8) failed"
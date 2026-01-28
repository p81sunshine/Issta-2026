from solution import *

def test_example_1():
    assert sequentialDigits(100, 300) == [123, 234], "Example 1 failed"

def test_example_2():
    assert sequentialDigits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345], "Example 2 failed"

def test_low_10_high_20():
    assert sequentialDigits(10, 20) == [12], "Test case low=10, high=20 failed"

def test_low_1_high_10():
    assert sequentialDigits(1, 10) == list(range(1, 10)), "Test case low=1, high=10 failed"

def test_low_10_high_109():
    expected = [12, 23, 34, 45, 56, 67, 78, 89]
    assert sequentialDigits(10, 109) == expected, "Test case low=10, high=109 failed"
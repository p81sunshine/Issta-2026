from solution import *

def test_example_1():
    assert sequentialDigits(100, 300) == [123, 234], "Example 1 failed"

def test_example_2():
    assert sequentialDigits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345], "Example 2 failed"

def test_low_high_10_20():
    assert sequentialDigits(10, 20) == [12], "Test case for 10-20 range failed"

def test_low_high_100_110():
    assert sequentialDigits(100, 110) == [], "Test case for 100-110 range failed"

def test_low_high_1_10():
    assert sequentialDigits(1, 10) == [1, 2, 3, 4, 5, 6, 7, 8, 9], "Test case for 1-10 range failed"
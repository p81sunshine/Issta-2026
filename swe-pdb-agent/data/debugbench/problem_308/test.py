from solution import *

def test_example_1():
    assert minimum_partition("165462", 60) == 4, "Example 1 failed"

def test_example_2():
    assert minimum_partition("238182", 5) == -1, "Example 2 failed"

def test_single_digit_valid():
    assert minimum_partition("3", 5) == 1, "Single valid digit failed"

def test_single_digit_invalid():
    assert minimum_partition("6", 5) == -1, "Single invalid digit failed"

def test_full_partition():
    assert minimum_partition("12", 120) == 1, "Full partition case failed"

def test_multiple_splits():
    assert minimum_partition("1234", 9) == 4, "Multiple splits case failed"
from solution import *

def test_example_1():
    assert minimumPartition("165462", 60) == 4, "Example 1 failed"

def test_example_2():
    assert minimumPartition("238182", 5) == -1, "Example 2 failed"

def test_single_digit():
    assert minimumPartition("5", 5) == 1, "Single digit test failed"

def test_split_each_digit():
    assert minimumPartition("1111", 1) == 4, "Split each digit test failed"

def test_split_into_two_parts():
    assert minimumPartition("1234", 100) == 2, "Split into two parts test failed"
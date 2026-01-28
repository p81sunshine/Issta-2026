from solution import *

def test_example_1():
    assert sequential_digits(100, 300) == [123, 234], "Example 1 failed"

def test_example_2():
    assert sequential_digits(1000, 13000) == [1234, 2345, 3456, 4567, 5678, 6789, 12345], "Example 2 failed"

def test_edge_case_two_digits():
    assert sequential_digits(10, 99) == [12, 23, 34, 45, 56, 67, 78, 89], "Two-digit sequential failed"

def test_edge_case_single_number():
    assert sequential_digits(123, 123) == [123], "Single number failed"
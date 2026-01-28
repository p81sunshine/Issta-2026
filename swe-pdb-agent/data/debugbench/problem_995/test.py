from solution import *

def test_example_1():
    assert find_complement(5) == 2, "Example 1 failed: 5 -> 101 -> 010 (2)"

def test_example_2():
    assert find_complement(1) == 0, "Example 2 failed: 1 -> 1 -> 0 (0)"

def test_case_7():
    assert find_complement(7) == 0, "Test case 7 failed: 111 -> 000 (0)"

def test_case_2():
    assert find_complement(2) == 1, "Test case 2 failed: 10 -> 01 (1)"

def test_case_4():
    assert find_complement(4) == 3, "Test case 4 failed: 100 -> 011 (3)"
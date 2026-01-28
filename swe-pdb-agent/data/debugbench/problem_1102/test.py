from solution import *

def test_example_1():
    assert longestWPI([9,9,6,0,6,6,9]) == 3, "First example test case failed"

def test_example_2():
    assert longestWPI([6,6,6]) == 0, "Second example test case failed"

def test_case_3():
    assert longestWPI([8, 9]) == 1, "Test case where correct code returns 1 but buggy returns 0"

def test_case_4():
    assert longestWPI([8, 9, 8]) == 1, "Test case where correct code outperforms buggy logic"
from solution import *

def test_example_1():
    assert totalNQueens(4) == 2, "Test case n=4 failed"

def test_example_2():
    assert totalNQueens(1) == 1, "Test case n=1 failed"

def test_case_n2():
    assert totalNQueens(2) == 0, "Test case n=2 failed"

def test_case_n3():
    assert totalNQueens(3) == 0, "Test case n=3 failed"

def test_case_n5():
    assert totalNQueens(5) == 10, "Test case n=5 failed"
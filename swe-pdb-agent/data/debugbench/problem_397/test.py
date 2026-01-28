from solution import *

def test_example_1():
    assert totalNQueens(4) == 2, "Failed for input n=4"

def test_example_2():
    assert totalNQueens(1) == 1, "Failed for input n=1"

def test_edge_case_n2():
    assert totalNQueens(2) == 0, "Failed for input n=2"

def test_edge_case_n3():
    assert totalNQueens(3) == 0, "Failed for input n=3"

def test_case_n5():
    assert totalNQueens(5) == 10, "Failed for input n=5"
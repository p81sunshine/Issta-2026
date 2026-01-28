from solution import *

def test_example_1():
    assert totalNQueens(4) == 2, "Failed for n=4"

def test_example_2():
    assert totalNQueens(1) == 1, "Failed for n=1"

def test_n_2_case():
    assert totalNQueens(2) == 0, "Failed for n=2"

def test_n_3_case():
    assert totalNQueens(3) == 0, "Failed for n=3"
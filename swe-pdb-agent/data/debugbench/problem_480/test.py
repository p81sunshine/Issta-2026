from solution import *

def test_example_1():
    assert tribonacci(4) == 4, "Failed for n=4: expected 4"

def test_example_2():
    assert tribonacci(25) == 1389537, "Failed for n=25: expected 1389537"

def test_case_n_5():
    assert tribonacci(5) == 7, "Failed for n=5: expected 7"

def test_edge_case_zero():
    assert tribonacci(0) == 0, "Edge case n=0 failed"

def test_edge_case_one():
    assert tribonacci(1) == 1, "Edge case n=1 failed"
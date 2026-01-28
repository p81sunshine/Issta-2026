from solution import *

def test_example_1():
    assert tribonacci(4) == 4, "Failed for n=4"

def test_example_2():
    assert tribonacci(25) == 1389537, "Failed for n=25"

def test_edge_case_0():
    assert tribonacci(0) == 0, "Failed for n=0"

def test_edge_case_1():
    assert tribonacci(3) == 2, "Failed for n=3"

def test_edge_case_2():
    assert tribonacci(1) == 1, "Failed for n=1"
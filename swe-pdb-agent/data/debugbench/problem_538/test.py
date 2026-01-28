from solution import *

def test_example_1():
    assert fib(2) == 1, "Input: n = 2 should return 1"

def test_example_2():
    assert fib(3) == 2, "Input: n = 3 should return 2"

def test_example_3():
    assert fib(4) == 3, "Input: n = 4 should return 3"

def test_edge_case_0():
    assert fib(0) == 0, "Input: n = 0 should return 0"

def test_edge_case_1():
    assert fib(1) == 1, "Input: n = 1 should return 1"
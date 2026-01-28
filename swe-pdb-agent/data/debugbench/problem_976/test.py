from solution import *

def test_edge_case_0():
    assert fib(0) == 0, "F(0) should be 0"

def test_edge_case_1():
    assert fib(1) == 1, "F(1) should be 1"

def test_example_1():
    assert fib(2) == 1, "F(2) should be F(1)+F(0) = 1+0 = 1"

def test_example_2():
    assert fib(3) == 2, "F(3) should be F(2)+F(1) = 1+1 = 2"

def test_example_3():
    assert fib(4) == 3, "F(4) should be F(3)+F(2) = 2+1 = 3"
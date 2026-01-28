from solution import *

def test_example_1():
    assert isReachable(6, 9) is False, "Example 1 failed"

def test_example_2():
    assert isReachable(4, 7) is True, "Example 2 failed"

def test_edge_case_1():
    assert isReachable(1, 1) is True, "Origin point should be reachable"

def test_edge_case_2():
    assert isReachable(2, 2) is True, "Double power-of-two case"

def test_edge_case_3():
    assert isReachable(3, 6) is False, "Odd GCD case should be unreachable"
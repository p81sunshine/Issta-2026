from solution import *

def test_example_1():
    assert equationsPossible(["a==b","b!=a"]) is False, "Example 1 failed"

def test_example_2():
    assert equationsPossible(["b==a","a==b"]) is True, "Example 2 failed"

def test_edge_case_1():
    assert equationsPossible(["a==b"]) is True, "Edge case 1 failed"

def test_edge_case_2():
    assert equationsPossible(["a!=b"]) is True, "Edge case 2 failed"

def test_edge_case_3():
    assert equationsPossible(["a!=a"]) is False, "Edge case 3 failed"
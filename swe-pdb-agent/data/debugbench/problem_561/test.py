from solution import *

def test_example_1():
    assert equationsPossible(["a==b","b!=a"]) is False, "Should return False for conflicting equality and inequality"

def test_example_2():
    assert equationsPossible(["b==a","a==b"]) is True, "Should return True for consistent equalities"

def test_edge_case_inequality():
    assert equationsPossible(["a!=b"]) is True, "Should return True for non-connected variables in inequality"

def test_inequality_after_equality():
    assert equationsPossible(["a==b", "b!=a"]) is False, "Should return False for contradictory equality and inequality"

def test_same_variable_inequality():
    assert equationsPossible(["a!=a"]) is False, "Should return False for same-variable inequality"
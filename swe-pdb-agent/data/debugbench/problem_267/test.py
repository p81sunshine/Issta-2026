from solution import *

def test_example_1():
    equations = ["a==b","b!=a"]
    assert equations_possible(equations) is False, "Should return False for conflicting equality and inequality"

def test_example_2():
    equations = ["b==a","a==b"]
    assert equations_possible(equations) is True, "Should return True for all valid equalities"

def test_edge_case_self_inequality():
    equations = ["a!=a"]
    assert equations_possible(equations) is False, "Variable cannot be unequal to itself"

def test_cycle_conflict():
    equations = ["a==b", "b==c", "a!=c"]
    assert equations_possible(equations) is False, "Inequality violates connected equality chain"

def test_disconnected_valid_inequality():
    equations = ["a==b", "c==d", "a!=c"]
    assert equations_possible(equations) is True, "Inequality between disconnected groups should be valid"
from solution import *

def test_example_1():
    equations = ["a==b","b!=a"]
    assert equationsPossible(equations) is False, "Should return False for conflicting equality and inequality"

def test_example_2():
    equations = ["b==a","a==b"]
    assert equationsPossible(equations) is True, "Should return True for consistent equalities"

def test_single_equality():
    equations = ["a==a"]
    assert equationsPossible(equations) is True, "Should handle trivial equality"

def test_single_inequality():
    equations = ["a!=b"]
    assert equationsPossible(equations) is True, "Should return True for valid inequality"

def test_chain_equality_inequality():
    equations = ["a==b","b==c","a!=c"]
    assert equationsPossible(equations) is False, "Should detect contradiction in chained equalities and inequality"
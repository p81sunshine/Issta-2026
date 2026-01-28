from solution import *

def test_example_1():
    equations = ["a==b","b!=a"]
    assert equationsPossible(equations) is False, "Should return False for conflicting equations"

def test_example_2():
    equations = ["b==a","a==b"]
    assert equationsPossible(equations) is True, "Should return True for consistent equations"

def test_single_equation():
    equations = ["a==a"]
    assert equationsPossible(equations) is True, "Should handle single valid equation"

def test_empty_equations():
    equations = []
    assert equationsPossible(equations) is True, "Should return True for empty input"

def test_complex_case():
    equations = ["a==b", "b==c", "a!=c"]
    assert equationsPossible(equations) is False, "Should detect contradiction in connected components"
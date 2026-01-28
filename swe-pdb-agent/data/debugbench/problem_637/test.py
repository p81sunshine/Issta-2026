from solution import *

def test_example_1():
    equations = ["a==b","b!=a"]
    assert equationsPossible(equations) is False, "Example 1 should return False"

def test_example_2():
    equations = ["b==a","a==b"]
    assert equationsPossible(equations) is True, "Example 2 should return True"

def test_single_equality():
    equations = ["a==b"]
    assert equationsPossible(equations) is True, "Single equality should return True"

def test_self_inequality():
    equations = ["a!=a"]
    assert equationsPossible(equations) is False, "Self inequality should return False"

def test_non_conflicting_inequality():
    equations = ["a==b", "b!=c"]
    assert equationsPossible(equations) is True, "Non-conflicting inequality should return True"

def test_conflicting_inequality_in_same_set():
    equations = ["a==b", "b==c", "a!=c"]
    assert equationsPossible(equations) is False, "Conflicting inequality in same set should return False"
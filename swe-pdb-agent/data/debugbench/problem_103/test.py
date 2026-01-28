from solution import *

def test_example_1():
    equations = ["a==b","b!=a"]
    assert equations_possible(equations) is False, "Example 1 should return False"

def test_example_2():
    equations = ["b==a","a==b"]
    assert equations_possible(equations) is True, "Example 2 should return True"

def test_buggy_undef_crash():
    equations = ["a==b"]
    assert equations_possible(equations) is True, "Valid equality should not crash and return True"

def test_indirect_conflict():
    equations = ["a==b","b==c","a!=c"]
    assert equations_possible(equations) is False, "Indirect conflict should return False"

def test_disconnected_valid():
    equations = ["a==b","c==d","a!=c"]
    assert equations_possible(equations) is True, "Disconnected groups with valid inequality should return True"
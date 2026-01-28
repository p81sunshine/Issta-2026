from solution import *

def test_example_1():
    assert equationsPossible(["a==b","b!=a"]) is False, "Example 1 should return False"

def test_example_2():
    assert equationsPossible(["b==a","a==b"]) is True, "Example 2 should return True"

def test_single_equality():
    assert equationsPossible(["a==b"]) is True, "Single equality should return True"

def test_empty_list():
    assert equationsPossible([]) is True, "Empty list should return True"

def test_self_inequality():
    assert equationsPossible(["a!=a"]) is False, "Self inequality should return False"
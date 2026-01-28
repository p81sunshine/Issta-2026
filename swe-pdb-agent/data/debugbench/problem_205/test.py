from solution import *

def test_example_1():
    # Input: ["a==b","b!=a"], Output: False
    assert equations_possible(["a==b","b!=a"]) is False, "Example 1 failed"

def test_example_2():
    # Input: ["b==a","a==b"], Output: True
    assert equations_possible(["b==a","a==b"]) is True, "Example 2 failed"

def test_single_inequality():
    # Input: ["a!=b"], Output: True
    assert equations_possible(["a!=b"]) is True, "Single inequality should be True"

def test_self_equality():
    # Input: ["a==a"], Output: True
    assert equations_possible(["a==a"]) is True, "Self equality should be True"

def test_self_inequality():
    # Input: ["a!=a"], Output: False
    assert equations_possible(["a!=a"]) is False, "Self inequality should be False"
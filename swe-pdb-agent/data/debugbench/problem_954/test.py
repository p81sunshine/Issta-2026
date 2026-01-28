from solution import *

def test_example_1():
    assert equations_possible(["a==b","b!=a"]) is False, "Example 1 failed"

def test_example_2():
    assert equations_possible(["b==a","a==b"]) is True, "Example 2 failed"

def test_dual_inequality():
    assert equations_possible(["a!=b", "b!=a"]) is True, "Dual inequality test failed"

def test_cycle_inequality():
    assert equations_possible(["a==b","b==c","a!=c"]) is False, "Cycle with inequality test failed"

def test_self_inequality():
    assert equations_possible(["a!=a"]) is False, "Self-inequality test failed"
from solution import *
from pytest import approx

def test_example_1():
    assert frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 2, 4) == approx(0.16666666666666666)

def test_example_2():
    assert frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 7) == approx(0.3333333333333333)

def test_single_node():
    assert frogPosition(1, [], 0, 1) == 1.0
    assert frogPosition(1, [], 5, 1) == 1.0

def test_time_too_short():
    assert frogPosition(7, [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], 1, 4) == 0.0

def test_bug_scenario():
    # This test exposes the loop range bug in the buggy implementation
    assert frogPosition(3, [[1,2],[2,3]], 1, 2) == approx(1.0)
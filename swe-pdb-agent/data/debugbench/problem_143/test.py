from solution import *
import pytest

def test_example_1():
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 2
    target = 4
    expected = 0.16666666666666666
    assert frog_position(n, edges, t, target) == pytest.approx(expected)

def test_example_2():
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 1
    target = 7
    expected = 0.3333333333333333
    assert frog_position(n, edges, t, target) == pytest.approx(expected)

def test_case_3():
    n = 3
    edges = [[1,2],[2,3]]
    t = 1
    target = 2
    expected = 1.0
    assert frog_position(n, edges, t, target) == pytest.approx(expected)

def test_edge_case_1():
    n = 1
    edges = []
    t = 0
    target = 1
    expected = 1.0
    assert frog_position(n, edges, t, target) == pytest.approx(expected)

def test_edge_case_2():
    n = 2
    edges = [[1,2]]
    t = 1
    target = 1
    expected = 0.0
    assert frog_position(n, edges, t, target) == pytest.approx(expected)
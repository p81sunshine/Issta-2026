from solution import *
import pytest

def test_example_1():
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 2
    target = 4
    expected = 1/6
    result = frog_position(n, edges, t, target)
    assert result == pytest.approx(expected), f"Expected {expected}, but got {result}"

def test_example_2():
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 1
    target = 7
    expected = 1/3
    result = frog_position(n, edges, t, target)
    assert result == pytest.approx(expected), f"Expected {expected}, but got {result}"

def test_single_node():
    n = 1
    edges = []
    t = 0
    target = 1
    expected = 1.0
    result = frog_position(n, edges, t, target)
    assert result == expected, f"Expected {expected} for single node, got {result}"

def test_time_longer_than_needed():
    n = 2
    edges = [[1,2]]
    t = 2
    target = 2
    expected = 1.0
    result = frog_position(n, edges, t, target)
    assert result == pytest.approx(expected), f"Expected {expected} for fixed position, got {result}"

def test_unreachable_target():
    n = 3
    edges = [[1,2]]
    t = 1
    target = 3
    expected = 0.0
    result = frog_position(n, edges, t, target)
    assert result == expected, f"Expected {expected} for unreachable target, got {result}"
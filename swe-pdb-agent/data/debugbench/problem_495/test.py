from solution import *

def test_example_1():
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 2
    target = 4
    expected = 0.16666666666666666
    result = frogPosition(n, edges, t, target)
    assert result == expected, f"Expected {expected}, got {result}"

def test_example_2():
    n = 7
    edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]]
    t = 1
    target = 7
    expected = 0.3333333333333333
    result = frogPosition(n, edges, t, target)
    assert result == expected, f"Expected {expected}, got {result}"

def test_single_node():
    n = 1
    edges = []
    t = 0
    target = 1
    expected = 1.0
    result = frogPosition(n, edges, t, target)
    assert result == expected, f"Expected {expected}, got {result}"

def test_reach_target_at_exact_time():
    n = 2
    edges = [[1,2]]
    t = 1
    target = 2
    expected = 1.0
    result = frogPosition(n, edges, t, target)
    assert result == expected, f"Expected {expected}, got {result}"

def test_multiple_choices():
    n = 3
    edges = [[1,2], [1,3]]
    t = 1
    target = 3
    expected = 0.5
    result = frogPosition(n, edges, t, target)
    assert result == expected, f"Expected {expected}, got {result}"
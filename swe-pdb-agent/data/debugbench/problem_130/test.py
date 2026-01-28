from solution import *

def test_example_1():
    edges = [1,0,0,0,0,7,7,5]
    assert edgeScore(edges) == 7, "First example failed"

def test_example_2():
    edges = [2,0,0,2]
    assert edgeScore(edges) == 0, "Second example failed"

def test_last_iteration_max():
    edges = [0, 1]
    assert edgeScore(edges) == 1, "Last iteration should update max"

def test_last_iteration_tie_break():
    edges = [1, 1, 0]
    assert edgeScore(edges) == 0, "Last iteration should break tie with lower index"

def test_multiple_updates_in_last():
    edges = [1, 2, 0]
    assert edgeScore(edges) == 0, "Last iteration adds to node 0 which becomes max"
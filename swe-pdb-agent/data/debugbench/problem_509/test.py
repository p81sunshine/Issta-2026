from solution import *

def test_example_1():
    edges = [3,3,4,2,3]
    assert longestCycle(edges) == 3, "Failed on example 1: should detect cycle of length 3"

def test_example_2():
    edges = [2,-1,3,1]
    assert longestCycle(edges) == -1, "Failed on example 2: no cycles should be present"

def test_single_node_cycle():
    edges = [0]
    assert longestCycle(edges) == 1, "Failed on single-node cycle"

def test_two_node_cycle():
    edges = [1, 0]
    assert longestCycle(edges) == 2, "Failed on two-node cycle"

def test_three_node_cycle():
    edges = [2, 0, 1]
    assert longestCycle(edges) == 3, "Failed on three-node cycle"
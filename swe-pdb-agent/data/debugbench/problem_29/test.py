from solution import *

def test_example_1():
    n = 7
    edges = [[0,1],[1,2],[3,1],[4,0],[0,5],[5,6]]
    restricted = [4,5]
    assert reachable_nodes(n, edges, restricted) == 4, "Example 1 failed"

def test_example_2():
    n = 7
    edges = [[0,1],[0,2],[0,5],[0,4],[3,2],[6,5]]
    restricted = [4,2,1]
    assert reachable_nodes(n, edges, restricted) == 3, "Example 2 failed"

def test_start_node_restricted():
    n = 1
    edges = []
    restricted = [0]
    assert reachable_nodes(n, edges, restricted) == 0, "Start node restricted failed"

def test_no_restricted():
    n = 3
    edges = [[0,1],[0,2]]
    restricted = []
    assert reachable_nodes(n, edges, restricted) == 3, "No restrictions test failed"

def test_simple_chain_with_restriction():
    n = 3
    edges = [[0,1],[1,2]]
    restricted = [1]
    assert reachable_nodes(n, edges, restricted) == 1, "Chain with middle restriction failed"
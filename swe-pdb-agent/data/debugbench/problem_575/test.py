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

def test_starting_node_restricted():
    n = 1
    edges = []
    restricted = [0]
    assert reachable_nodes(n, edges, restricted) == 0, "Starting node restricted failed"

def test_no_restricted_nodes():
    n = 3
    edges = [[0,1], [0,2]]
    restricted = []
    assert reachable_nodes(n, edges, restricted) == 3, "No restrictions failed"

def test_all_neighbors_restricted():
    n = 3
    edges = [[0,1], [0,2]]
    restricted = [1,2]
    assert reachable_nodes(n, edges, restricted) == 1, "All neighbors restricted failed"
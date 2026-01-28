from solution import *

def test_example_1():
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    expected = 2
    assert closestMeetingNode(edges, node1, node2) == expected, "Failed for example 1"

def test_example_2():
    edges = [1, 2, -1]
    node1 = 0
    node2 = 2
    expected = 2
    assert closestMeetingNode(edges, node1, node2) == expected, "Failed for example 2"

def test_no_common_nodes():
    edges = [1, -1, 3, -1]
    node1 = 0
    node2 = 2
    expected = -1
    assert closestMeetingNode(edges, node1, node2) == expected, "Failed for no common nodes case"

def test_same_starting_node():
    edges = [-1]
    node1 = 0
    node2 = 0
    expected = 0
    assert closestMeetingNode(edges, node1, node2) == expected, "Failed for same starting node"

def test_cycle_handling():
    edges = [1, 2, 0]
    node1 = 0
    node2 = 2
    expected = 2
    # node1's distances: 0→1 (1), 1→2 (2), 2→0 (loop stops)
    # node2's distances: 2 (0), 0→1 (1), 1→2 (already visited)
    # node 2: max(2, 0) = 2; node 0: max(0, 1) = 1; node 1: max(1, 2) = 2
    # correct answer is 0
    assert closestMeetingNode(edges, node1, node2) == 0, "Failed for cycle handling case"
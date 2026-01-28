from solution import *

def test_example_1():
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    expected = 2
    assert closestMeetingNode(edges, node1, node2) == expected

def test_example_2():
    edges = [1, 2, -1]
    node1 = 0
    node2 = 2
    expected = 2
    assert closestMeetingNode(edges, node1, node2) == expected

def test_edge_case_cycle():
    edges = [1, 0, -1]
    node1 = 0
    node2 = 1
    expected = 0
    assert closestMeetingNode(edges, node1, node2) == expected
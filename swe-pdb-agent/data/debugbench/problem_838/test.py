from solution import *

def test_example_1():
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
    expected = 2
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed on example 1"

def test_example_2():
    edges = [1,2,-1]
    node1 = 0
    node2 = 2
    expected = 2
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed on example 2"

def test_no_meeting_node():
    edges = [-1, -1]
    node1 = 0
    node2 = 1
    expected = -1
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed on no meeting node case"

def test_cycle_case():
    edges = [1, 2, 0]
    node1 = 0
    node2 = 1
    expected = 1
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed on cycle case"

def test_direct_connection():
    edges = [1, -1]
    node1 = 0
    node2 = 1
    expected = 1
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed on direct connection case"
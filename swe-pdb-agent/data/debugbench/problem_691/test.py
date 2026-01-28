from solution import *

def test_example_1():
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    expected = 2
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed for example 1"

def test_example_2():
    edges = [1, 2, -1]
    node1 = 0
    node2 = 2
    expected = 2
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed for example 2"

def test_no_meeting_node():
    edges = [1, -1, 3, -1]
    node1 = 0
    node2 = 2
    expected = -1
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed for no meeting node case"

def test_same_node():
    edges = [-1]
    node1 = 0
    node2 = 0
    expected = 0
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed for same node case"

def test_tie_for_min_max():
    edges = [3, 3, -1, -1]
    node1 = 0
    node2 = 1
    expected = 3
    assert closest_meeting_node(edges, node1, node2) == expected, "Failed for tie in min max distance"
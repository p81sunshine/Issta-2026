from solution import *

def test_example_1():
    edges = [2, 2, 3, -1]
    node1 = 0
    node2 = 1
    assert closestMeetingNode(edges, node1, node2) == 2, "Example 1 failed"

def test_example_2():
    edges = [1, 2, -1]
    node1 = 0
    node2 = 2
    assert closestMeetingNode(edges, node1, node2) == 2, "Example 2 failed"

def test_no_meeting_node():
    edges = [1, 2, 0, -1]
    node1 = 0
    node2 = 3
    assert closestMeetingNode(edges, node1, node2) == -1, "No meeting node case failed"

def test_edge_case_cycle():
    edges = [1, -1]
    node1 = 0
    node2 = 1
    assert closestMeetingNode(edges, node1, node2) == 1, "Cycle case failed"
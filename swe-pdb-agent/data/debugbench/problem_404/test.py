from solution import *

def test_example_1():
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
    assert closestMeetingNode(edges, node1, node2) == 2, "Example 1 should return node 2"

def test_example_2():
    edges = [1,2,-1]
    node1 = 0
    node2 = 2
    assert closestMeetingNode(edges, node1, node2) == 2, "Example 2 should return node 2"

def test_custom_case_buggy():
    edges = [2, -1, 1]
    node1 = 0
    node2 = 1
    assert closestMeetingNode(edges, node1, node2) == 1, "Buggy code should fail this cycle case"

def test_no_meeting_node():
    edges = [0, 1, 2, -1]
    node1 = 0
    node2 = 3
    assert closestMeetingNode(edges, node1, node2) == -1, "No common meeting node should return -1"
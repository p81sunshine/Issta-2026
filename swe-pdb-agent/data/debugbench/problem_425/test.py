from solution import *

def test_example_1():
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
    assert closestMeetingNode(edges, node1, node2) == 2

def test_example_2():
    edges = [1,2,-1]
    node1 = 0
    node2 = 2
    assert closestMeetingNode(edges, node1, node2) == 2

def test_cycle_case():
    edges = [2, -1, 0]
    node1 = 0
    node2 = 2
    assert closestMeetingNode(edges, node1, node2) == 0

def test_no_meeting_node():
    edges = [1, -1, 3, -1, 2]
    node1 = 0
    node2 = 2
    assert closestMeetingNode(edges, node1, node2) == -1

def test_tie_case():
    edges = [1, -1, 1]
    node1 = 0
    node2 = 2
    assert closestMeetingNode(edges, node1, node2) == 1
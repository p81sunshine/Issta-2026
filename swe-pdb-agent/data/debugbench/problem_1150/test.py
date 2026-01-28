from solution import *

def test_example_1():
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
    assert closestMeetingNode(edges, node1, node2) == 2, "Example 1 failed"

def test_example_2():
    edges = [1,2,-1]
    node1 = 0
    node2 = 2
    assert closestMeetingNode(edges, node1, node2) == 2, "Example 2 failed"

def test_buggy_indexing_case():
    edges = [2, 3, -1, 2]
    node1 = 0
    node2 = 1
    assert closestMeetingNode(edges, node1, node2) == 2, "Buggy indexing case failed"

def test_cycle_case():
    edges = [1, 0]
    node1 = 0
    node2 = 1
    assert closestMeetingNode(edges, node1, node2) == 0, "Cycle case failed"
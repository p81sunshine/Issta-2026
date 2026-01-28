from solution import *

def test_example_1():
    edges = [2,2,3,-1]
    node1 = 0
    node2 = 1
    assert closest_meeting_node(edges, node1, node2) == 2

def test_example_2():
    edges = [1,2,-1]
    node1 = 0
    node2 = 2
    assert closest_meeting_node(edges, node1, node2) == 2

def test_no_common_node():
    edges = [1,-1,3,-1]
    node1 = 0
    node2 = 2
    assert closest_meeting_node(edges, node1, node2) == -1

def test_same_node():
    edges = [1,-1]
    node1 = 0
    node2 = 0
    assert closest_meeting_node(edges, node1, node2) == 0

def test_edge_case_single_node():
    edges = [-1]
    node1 = 0
    node2 = 0
    assert closest_meeting_node(edges, node1, node2) == 0
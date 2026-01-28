from solution import *

def test_example_1():
    # Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
    assert closestMeetingNode([2,2,3,-1], 0, 1) == 2, "First example should return 2"

def test_example_2():
    # Input: edges = [1,2,-1], node1 = 0, node2 = 2
    assert closestMeetingNode([1,2,-1], 0, 2) == 2, "Second example should return 2"

def test_cycle_case():
    # Test case where correct code passes and buggy code fails
    # edges = [1, 0, -1], node1=0, node2=1 → correct output is 0
    assert closestMeetingNode([1, 0, -1], 0, 1) == 0, "Cycle case should return 0"

def test_single_node():
    # Edge case with single node
    assert closestMeetingNode([-1], 0, 0) == 0, "Single node case should return 0"
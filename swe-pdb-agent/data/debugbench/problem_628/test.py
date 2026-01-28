from solution import *

def test_example_1():
    # Input: edges = [2,2,3,-1], node1 = 0, node2 = 1
    # Output: 2
    assert closestMeetingNode([2,2,3,-1], 0, 1) == 2, "Example 1 failed"

def test_example_2():
    # Input: edges = [1,2,-1], node1 = 0, node2 = 2
    # Output: 2
    assert closestMeetingNode([1,2,-1], 0, 2) == 2, "Example 2 failed"

def test_cycle_case():
    # Test case where buggy code fails: edges = [1, 0, -1], node1=0, node2=1
    # Correct answer is 0, buggy returns 1
    assert closestMeetingNode([1, 0, -1], 0, 1) == 0, "Cycle case failed"

def test_no_meeting_node():
    # Input: edges = [-1,-1], node1 = 0, node2 = 1
    # Output: -1
    assert closestMeetingNode([-1,-1], 0, 1) == -1, "No meeting node case failed"
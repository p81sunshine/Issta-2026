from solution import *

def test_example_1():
    # head = [3,2,0,-4], pos = 1
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2  # create cycle
    assert hasCycle(n1) is True, "Should detect cycle in example 1"

def test_example_2():
    # head = [1,2], pos = 0
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n2.next = n1  # create cycle
    assert hasCycle(n1) is True, "Should detect cycle in example 2"

def test_example_3():
    # head = [1], pos = -1
    n1 = ListNode(1)
    assert hasCycle(n1) is False, "Should return False for no cycle in example 3"

def test_edge_empty_list():
    # Empty list
    assert hasCycle(None) is False, "Empty list should return False"

def test_two_nodes_no_cycle():
    # Two nodes with no cycle
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert hasCycle(n1) is False, "Two nodes with no cycle should return False"
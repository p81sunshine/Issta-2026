from solution import *

def test_example_1():
    nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
    for i in range(3):
        nodes[i].next = nodes[i + 1]
    nodes[3].next = nodes[1]  # Create cycle
    assert hasCycle(nodes[0]) is True, "Test example 1 failed"

def test_example_2():
    nodes = [ListNode(1), ListNode(2)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[0]  # Create cycle
    assert hasCycle(nodes[0]) is True, "Test example 2 failed"

def test_example_3():
    head = ListNode(1)
    assert hasCycle(head) is False, "Test example 3 failed"

def test_single_node_cycle():
    node = ListNode(1)
    node.next = node  # Cycle pointing to itself
    assert hasCycle(node) is True, "Single node cycle should return True"

def test_empty_list():
    assert hasCycle(None) is False, "Empty list should return False"
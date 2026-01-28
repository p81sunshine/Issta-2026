from solution import *

def test_example_1():
    values = [3, 2, 0, -4]
    pos = 1
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    assert hasCycle(nodes[0]) is True, "Example 1 failed"

def test_example_2():
    values = [1, 2]
    pos = 0
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    assert hasCycle(nodes[0]) is True, "Example 2 failed"

def test_example_3():
    node = ListNode(1)
    assert hasCycle(node) is False, "Example 3 failed"

def test_empty_list():
    assert hasCycle(None) is False, "Empty list should return False"

def test_no_cycle_two_nodes():
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    assert hasCycle(node1) is False, "Two-node list with no cycle should return False"
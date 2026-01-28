from solution import *

def test_example_1():
    nodes = [ListNode(3), ListNode(2), ListNode(0), ListNode(-4)]
    for i in range(3):
        nodes[i].next = nodes[i + 1]
    nodes[3].next = nodes[1]  # pos=1
    assert has_cycle(nodes[0]) is True, "Expected True for cyclic list"

def test_example_2():
    nodes = [ListNode(1), ListNode(2)]
    nodes[0].next = nodes[1]
    nodes[1].next = nodes[0]  # pos=0
    assert has_cycle(nodes[0]) is True, "Expected True for cyclic list"

def test_example_3():
    head = ListNode(1)
    assert has_cycle(head) is False, "Expected False for acyclic list"

def test_empty_list():
    assert has_cycle(None) is False, "Expected False for empty list"

def test_single_node_cycle():
    node = ListNode(5)
    node.next = node  # cycle to self
    assert has_cycle(node) is True, "Single-node cycle should return True"
from solution import *

def create_linked_list_with_cycle(values, pos):
    if not values:
        return None
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

def test_example_1():
    head = [3, 2, 0, -4]
    pos = 1
    expected = True
    head_node = create_linked_list_with_cycle(head, pos)
    result = hasCycle(head_node)
    assert result == expected, "Test example 1 failed"

def test_example_2():
    head = [1, 2]
    pos = 0
    expected = True
    head_node = create_linked_list_with_cycle(head, pos)
    result = hasCycle(head_node)
    assert result == expected, "Test example 2 failed"

def test_example_3():
    head = [1]
    pos = -1
    expected = False
    head_node = create_linked_list_with_cycle(head, pos)
    result = hasCycle(head_node)
    assert result == expected, "Test example 3 failed"

def test_empty_list():
    head = None
    expected = False
    result = hasCycle(head)
    assert result == expected, "Test empty list failed"

def test_single_node_no_cycle():
    head = [5]
    pos = -1
    expected = False
    head_node = create_linked_list_with_cycle(head, pos)
    result = hasCycle(head_node)
    assert result == expected, "Test single node no cycle failed"
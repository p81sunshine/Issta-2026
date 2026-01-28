from solution import *

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def create_linked_list(values, pos):
    if not values:
        return None
    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes)-1):
        nodes[i].next = nodes[i+1]
    if pos != -1:
        nodes[-1].next = nodes[pos]
    return nodes[0]

def test_example_1():
    head = create_linked_list([3,2,0,-4], 1)
    assert hasCycle(head) is True, "Example 1: Cycle detection failed"

def test_example_2():
    head = create_linked_list([1,2], 0)
    assert hasCycle(head) is True, "Example 2: Cycle detection failed"

def test_example_3():
    head = create_linked_list([1], -1)
    assert hasCycle(head) is False, "Example 3: False positive for cycle"

def test_acyclic_two_nodes():
    head = create_linked_list([1,2], -1)
    assert hasCycle(head) is False, "Test 4: Acyclic two-node list falsely detected as cyclic"

def test_acyclic_three_nodes():
    head = create_linked_list([1,2,3], -1)
    assert hasCycle(head) is False, "Test 5: Acyclic three-node list falsely detected as cyclic"
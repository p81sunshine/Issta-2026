from solution import *

def list_to_linked(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def test_example_1():
    input_list = [1,2,3,4,5]
    k = 2
    expected = [2,1,4,3,5]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected, f"Expected {expected}, got {linked_to_list(result)}"

def test_example_2():
    input_list = [1,2,3,4,5]
    k = 3
    expected = [3,2,1,4,5]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected, f"Expected {expected}, got {linked_to_list(result)}"

def test_k_larger_than_list():
    input_list = [1,2,3]
    k = 4
    expected = [1,2,3]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected

def test_empty_list():
    head = None
    k = 2
    expected = None
    result = reverseKGroup(head, k)
    assert result is None

def test_single_node():
    input_list = [5]
    k = 1
    expected = [5]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected

def test_k_1():
    input_list = [1,2,3,4]
    k = 1
    expected = [1,2,3,4]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected
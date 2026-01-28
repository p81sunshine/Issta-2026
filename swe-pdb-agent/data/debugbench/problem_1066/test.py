from solution import *

def list_to_linked(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_example_1():
    input_list = [1,2,3,4,5]
    k = 2
    expected = [2,1,4,3,5]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected, f"Failed for input {input_list} with k={k}"

def test_example_2():
    input_list = [1,2,3,4,5]
    k = 3
    expected = [3,2,1,4,5]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected, f"Failed for input {input_list} with k={k}"

def test_edge_case_k_1():
    input_list = [1,2,3,4,5]
    k = 1
    expected = [1,2,3,4,5]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected, "Failed for k=1"

def test_edge_case_single_node():
    input_list = [1]
    k = 1
    expected = [1]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected, "Failed for single node"

def test_edge_case_incomplete_group():
    input_list = [1,2,3]
    k = 2
    expected = [2,1,3]
    head = list_to_linked(input_list)
    result = reverseKGroup(head, k)
    assert linked_to_list(result) == expected, "Failed for incomplete group"
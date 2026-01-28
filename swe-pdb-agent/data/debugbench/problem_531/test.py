from solution import *

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def test_example_1():
    input_list = [1,2,3,4,5]
    k = 2
    expected = [2,1,4,3,5]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected, "Example 1 failed"

def test_example_2():
    input_list = [1,2,3,4,5]
    k = 3
    expected = [3,2,1,4,5]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected, "Example 2 failed"

def test_longer_list_k2():
    input_list = [1,2,3,4,5,6]
    k = 2
    expected = [2,1,4,3,6,5]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected, "Longer list with k=2 failed"

def test_k3_with_7_elements():
    input_list = [1,2,3,4,5,6,7]
    k = 3
    expected = [3,2,1,6,5,4,7]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected, "Test with k=3 and 7 elements failed"

def test_edge_case_k1():
    input_list = [1,2,3,4,5]
    k = 1
    expected = [1,2,3,4,5]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected, "Edge case with k=1 failed"
from solution import *

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst

def test_example_1():
    input_list = [1,2,3,4,5]
    k = 2
    expected = [2,1,4,3,5]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected, f"Expected {expected}, but got {linkedlist_to_list(result)}"

def test_example_2():
    input_list = [1,2,3,4,5]
    k = 3
    expected = [3,2,1,4,5]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected, f"Expected {expected}, but got {linkedlist_to_list(result)}"

def test_edge_case_k_1():
    input_list = [1,2,3]
    k = 1
    expected = [1,2,3]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected

def test_edge_case_k_large():
    input_list = [1,2,3,4]
    k = 5
    expected = [1,2,3,4]
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected

def test_edge_empty():
    input_list = []
    k = 2
    expected = []
    head = list_to_linkedlist(input_list)
    result = reverseKGroup(head, k)
    assert linkedlist_to_list(result) == expected
from solution import *

def list_to_linkedlist(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def linkedlist_to_list(head):
    lst = []
    current = head
    while current:
        lst.append(current.val)
        current = current.next
    return lst

def test_example_1():
    input_head = [1,2,6,3,4,5,6]
    val = 6
    expected = [1,2,3,4,5]
    head = list_to_linkedlist(input_head)
    result = removeElements(head, val)
    assert linkedlist_to_list(result) == expected, "Test case 1 failed"

def test_example_2():
    input_head = []
    val = 1
    expected = []
    head = list_to_linkedlist(input_head)
    result = removeElements(head, val)
    assert linkedlist_to_list(result) == expected, "Test case 2 failed"

def test_example_3():
    input_head = [7,7,7,7]
    val = 7
    expected = []
    head = list_to_linkedlist(input_head)
    result = removeElements(head, val)
    assert linkedlist_to_list(result) == expected, "Test case 3 failed"

def test_remove_last_element():
    input_head = [1,2,3]
    val = 3
    expected = [1,2]
    head = list_to_linkedlist(input_head)
    result = removeElements(head, val)
    assert linkedlist_to_list(result) == expected, "Test remove last element failed"

def test_single_node_removal():
    input_head = [3]
    val = 3
    expected = []
    head = list_to_linkedlist(input_head)
    result = removeElements(head, val)
    assert linkedlist_to_list(result) == expected, "Test single node removal failed"
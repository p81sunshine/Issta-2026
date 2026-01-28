from solution import *

def create_linked_list(values):
    head = ListNode()
    current = head
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return head.next

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_example_1():
    lists = [
        create_linked_list([1,4,5]),
        create_linked_list([1,3,4]),
        create_linked_list([2,6]),
    ]
    result = mergeKLists(lists)
    assert linked_list_to_list(result) == [1,1,2,3,4,4,5,6]

def test_example_2():
    lists = []
    result = mergeKLists(lists)
    assert linked_list_to_list(result) == []

def test_example_3():
    lists = [create_linked_list([])]
    result = mergeKLists(lists)
    assert linked_list_to_list(result) == []

def test_additional_case():
    lists = [
        create_linked_list([5]),
        None,
        create_linked_list([3,4]),
    ]
    result = mergeKLists(lists)
    assert linked_list_to_list(result) == [3,4,5]
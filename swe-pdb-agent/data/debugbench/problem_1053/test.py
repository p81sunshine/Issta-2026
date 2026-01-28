from solution import *

def list_to_linked(py_list):
    dummy = ListNode()
    current = dummy
    for val in py_list:
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
    # Test merging multiple sorted lists
    lists = [
        list_to_linked([1,4,5]),
        list_to_linked([1,3,4]),
        list_to_linked([2,6])
    ]
    expected = [1,1,2,3,4,4,5,6]
    result = mergeKLists(lists)
    assert linked_to_list(result) == expected, "Failed to merge lists in ascending order"

def test_example_2():
    # Test empty input
    lists = []
    expected = []
    result = mergeKLists(lists)
    assert linked_to_list(result) == expected, "Failed for empty input"

def test_example_3():
    # Test list containing a single empty list
    lists = [list_to_linked([])]
    expected = []
    result = mergeKLists(lists)
    assert linked_to_list(result) == expected, "Failed for list with empty sublist"

def test_edge_case_single_element():
    # Test with one list containing a single element
    lists = [list_to_linked([5])]
    expected = [5]
    result = mergeKLists(lists)
    assert linked_to_list(result) == expected, "Failed for single-element list"
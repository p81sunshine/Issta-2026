from solution import *

def list_to_linkedlist(items):
    if not items:
        return None
    head = ListNode(items[0])
    current = head
    for val in items[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_lists(parts):
    result = []
    for part in parts:
        sublist = []
        current = part
        while current:
            sublist.append(current.val)
            current = current.next
        result.append(sublist)
    return result

def test_example_1():
    head = list_to_linkedlist([1,2,3])
    k = 5
    expected = [[1], [2], [3], [], []]
    result = splitListToParts(head, k)
    actual = linkedlist_to_lists(result)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_2():
    head = list_to_linkedlist([1,2,3,4,5,6,7,8,9,10])
    k = 3
    expected = [[1,2,3,4], [5,6,7], [8,9,10]]
    result = splitListToParts(head, k)
    actual = linkedlist_to_lists(result)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_empty_list():
    head = None
    k = 2
    expected = [[], []]
    result = splitListToParts(head, k)
    actual = linkedlist_to_lists(result)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_equal_length_k():
    head = list_to_linkedlist([1,2,3,4])
    k = 4
    expected = [[1], [2], [3], [4]]
    result = splitListToParts(head, k)
    actual = linkedlist_to_lists(result)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_parts_with_difference_one():
    head = list_to_linkedlist([1,2,3,4,5])
    k = 2
    expected = [[1,2,3], [4,5]]
    result = splitListToParts(head, k)
    actual = linkedlist_to_lists(result)
    assert actual == expected, f"Expected {expected}, got {actual}"
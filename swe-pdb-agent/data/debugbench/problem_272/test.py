from solution import *

def listnode_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def test_example_1():
    head = create_linked_list([1, 2, 3])
    k = 5
    result = splitListToParts(head, k)
    expected = [[1], [2], [3], [], []]
    converted = [listnode_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected}, but got {converted}"

def test_example_2():
    head = create_linked_list(list(range(1, 11)))  # Values 1 to 10
    k = 3
    result = splitListToParts(head, k)
    expected = [[1,2,3,4], [5,6,7], [8,9,10]]
    converted = [listnode_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected}, but got {converted}"

def test_empty_list():
    head = None
    k = 2
    result = splitListToParts(head, k)
    expected = [[], []]
    converted = [listnode_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected}, but got {converted}"

def test_split_equal_length():
    head = create_linked_list([1, 2, 3])
    k = 3
    result = splitListToParts(head, k)
    expected = [[1], [2], [3]]
    converted = [listnode_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected}, but got {converted}"

def test_single_element_split():
    head = create_linked_list([5])
    k = 2
    result = splitListToParts(head, k)
    expected = [[5], []]
    converted = [listnode_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected}, but got {converted}"
from solution import *

def to_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def test_example_1():
    # Input: [1,2,3], k=5
    head = to_linked_list([1, 2, 3])
    k = 5
    expected = [[1], [2], [3], [], []]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected, f"Expected {expected}, but got {converted}"

def test_example_2():
    # Input: [1,2,3,4,5,6,7,8,9,10], k=3
    head = to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 3
    expected = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected, f"Expected {expected}, but got {converted}"

def test_empty_list():
    # Input: [], k=2
    head = to_linked_list([])
    k = 2
    expected = [[], []]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected

def test_k_equal_length():
    # Input: [1,2,3], k=3
    head = to_linked_list([1, 2, 3])
    k = 3
    expected = [[1], [2], [3]]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected

def test_even_split():
    # Input: [1,2,3,4,5,6], k=3
    head = to_linked_list([1, 2, 3, 4, 5, 6])
    k = 3
    expected = [[1, 2], [3, 4], [5, 6]]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected
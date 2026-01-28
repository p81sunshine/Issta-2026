from solution import *

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def test_example_1():
    head = ListNode(1, ListNode(2, ListNode(3)))
    k = 5
    expected = [[1], [2], [3], [], []]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected, f"Expected {expected}, but got {converted}"

def test_example_2():
    nodes = [ListNode(i) for i in range(1, 11)]
    for i in range(9):
        nodes[i].next = nodes[i+1]
    head = nodes[0]
    k = 3
    expected = [
        [1,2,3,4],
        [5,6,7],
        [8,9,10]
    ]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected, f"Expected {expected} but got {converted}"

def test_empty_list():
    head = None
    k = 2
    expected = [[], []]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected, "Empty list test failed"

def test_split_with_zero_length_part():
    head = ListNode(1)
    k = 2
    expected = [[1], []]
    result = splitListToParts(head, k)
    converted = [to_list(part) for part in result]
    assert converted == expected, f"Expected {expected} but got {converted}"
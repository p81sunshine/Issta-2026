from solution import *
import pytest

def list_to_linkedlist(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linkedlist_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def test_example_1():
    # Input: [1,2,3], k=5
    head = list_to_linkedlist([1,2,3])
    k = 5
    expected = [[1], [2], [3], [], []]
    result = split_list_to_parts(head, k)
    converted = [linkedlist_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected} but got {converted}"

def test_example_2():
    # Input: [1-10], k=3
    head = list_to_linkedlist([1,2,3,4,5,6,7,8,9,10])
    k = 3
    expected = [[1,2,3,4], [5,6,7], [8,9,10]]
    result = split_list_to_parts(head, k)
    converted = [linkedlist_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected} but got {converted}"

def test_empty_list():
    # Empty list with k=3
    head = list_to_linkedlist([])
    k = 3
    expected = [[], [], []]
    result = split_list_to_parts(head, k)
    converted = [linkedlist_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected} but got {converted}"

def test_split_larger_k():
    # List shorter than k
    head = list_to_linkedlist([1,2])
    k = 3
    expected = [[1], [2], []]
    result = split_list_to_parts(head, k)
    converted = [linkedlist_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected} but got {converted}"

def test_even_split():
    # Even split case
    head = list_to_linkedlist([1,2,3,4])
    k = 2
    expected = [[1,2], [3,4]]
    result = split_list_to_parts(head, k)
    converted = [linkedlist_to_list(part) for part in result]
    assert converted == expected, f"Expected {expected} but got {converted}"
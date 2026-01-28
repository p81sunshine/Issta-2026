from solution import *
import pytest

def list_to_linked(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_to_parts_list(parts):
    result = []
    for part in parts:
        if part is None:
            result.append([])
        else:
            lst = []
            current = part
            while current:
                lst.append(current.val)
                current = current.next
            result.append(lst)
    return result

def test_example_1():
    head = list_to_linked([1, 2, 3])
    k = 5
    result = splitListToParts(head, k)
    expected = [[1], [2], [3], [], []]
    actual = linked_to_parts_list(result)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_example_2():
    head = list_to_linked([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 3
    result = splitListToParts(head, k)
    expected = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    actual = linked_to_parts_list(result)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_empty_list():
    head = None
    k = 2
    result = splitListToParts(head, k)
    expected = [[], []]
    actual = linked_to_parts_list(result)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_short_list():
    head = list_to_linked([1, 2])
    k = 3
    result = splitListToParts(head, k)
    expected = [[1], [2], []]
    actual = linked_to_parts_list(result)
    assert actual == expected, f"Expected {expected}, got {actual}"

def test_divisible_list():
    head = list_to_linked([1, 2, 3, 4])
    k = 2
    result = splitListToParts(head, k)
    expected = [[1, 2], [3, 4]]
    actual = linked_to_parts_list(result)
    assert actual == expected, f"Expected {expected}, got {actual}"
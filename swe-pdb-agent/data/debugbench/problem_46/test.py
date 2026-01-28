from solution import *

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def to_list(head):
    arr = []
    current = head
    while current:
        arr.append(current.val)
        current = current.next
    return arr

def test_example_1():
    head = to_linked_list([1, 2, 3])
    k = 5
    result = splitListToParts(head, k)
    expected = [[1], [2], [3], [], []]
    actual = [to_list(part) if part else [] for part in result]
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_example_2():
    head = to_linked_list(list(range(1, 11)))
    k = 3
    result = splitListToParts(head, k)
    expected = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    actual = [to_list(part) if part else [] for part in result]
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_empty_list():
    head = None
    k = 2
    result = splitListToParts(head, k)
    expected = [[], []]
    actual = [to_list(part) if part else [] for part in result]
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_split_equal_length():
    head = to_linked_list([1, 2, 3])
    k = 3
    result = splitListToParts(head, k)
    expected = [[1], [2], [3]]
    actual = [to_list(part) if part else [] for part in result]
    assert actual == expected, f"Expected {expected}, but got {actual}"

def test_k_1():
    head = to_linked_list([1, 2, 3, 4])
    k = 1
    result = splitListToParts(head, k)
    expected = [[1, 2, 3, 4]]
    actual = [to_list(part) if part else [] for part in result]
    assert actual == expected, f"Expected {expected}, but got {actual}"
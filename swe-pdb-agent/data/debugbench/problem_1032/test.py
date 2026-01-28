from solution import *

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

def test_example_1():
    # Input: head = [1,2,3], k = 5
    head = create_linked_list([1, 2, 3])
    k = 5
    result = split_list_to_parts(head, k)
    expected = [[1], [2], [3], [], []]
    assert len(result) == k, f"Expected {k} parts, got {len(result)}"
    for i in range(k):
        actual = linked_list_to_list(result[i]) if result[i] else []
        assert actual == expected[i], f"Part {i} failed. Expected {expected[i]}, got {actual}"

def test_example_2():
    # Input: head = [1,2,3,4,5,6,7,8,9,10], k = 3
    head = create_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    k = 3
    result = split_list_to_parts(head, k)
    expected = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
    assert len(result) == k, f"Expected {k} parts, got {len(result)}"
    for i in range(k):
        actual = linked_list_to_list(result[i]) if result[i] else []
        assert actual == expected[i], f"Part {i} failed. Expected {expected[i]}, got {actual}"

def test_edge_empty_list():
    # Empty list with k=2
    head = None
    k = 2
    result = split_list_to_parts(head, k)
    assert len(result) == k, f"Expected {k} parts, got {len(result)}"
    for part in result:
        assert part is None, "All parts should be None for empty input"

def test_edge_single_element():
    # Single element list with k=1
    head = create_linked_list([5])
    k = 1
    result = split_list_to_parts(head, k)
    assert len(result) == k, f"Expected {k} parts, got {len(result)}"
    actual = linked_list_to_list(result[0]) if result[0] else []
    assert actual == [5], f"Expected [5], got {actual}"

def test_case_length_less_than_k():
    # List length (2) is less than k (3)
    head = create_linked_list([1, 2])
    k = 3
    result = split_list_to_parts(head, k)
    expected = [[1], [2], []]
    assert len(result) == k, f"Expected {k} parts, got {len(result)}"
    for i in range(k):
        actual = linked_list_to_list(result[i]) if result[i] else []
        assert actual == expected[i], f"Part {i} failed. Expected {expected[i]}, got {actual}"
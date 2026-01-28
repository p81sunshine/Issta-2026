from solution import *

def to_linked_list(py_list):
    if not py_list:
        return None
    return ListNode(py_list[0], to_linked_list(py_list[1:]))

def to_py_list(node):
    if not node:
        return []
    return [node.val] + to_py_list(node.next)

def test_example_1():
    lists = [
        to_linked_list([1,4,5]),
        to_linked_list([1,3,4]),
        to_linked_list([2,6]),
    ]
    expected = [1,1,2,3,4,4,5,6]
    result = mergeKLists(lists)
    assert to_py_list(result) == expected, "Failed to merge lists in correct ascending order"

def test_example_2():
    assert to_py_list(mergeKLists([])) == [], "Empty input should return empty list"

def test_example_3():
    assert to_py_list(mergeKLists([[]])) == [], "Input with single empty list should return empty list"

def test_single_list():
    input_list = to_linked_list([2,1,3])
    expected = [1,2,3]
    result = mergeKLists([input_list])
    assert to_py_list(result) == expected, "Single list should be sorted in ascending order"
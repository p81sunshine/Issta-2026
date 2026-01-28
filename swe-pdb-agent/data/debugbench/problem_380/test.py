from solution import *
import pytest

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def create_tree(values_list):
    if not values_list or values_list[0] is None:
        return None
    root = TreeNode(values_list[0])
    queue = [root]
    i = 1
    while i < len(values_list):
        current_node = queue.pop(0)
        if i < len(values_list):
            left_val = values_list[i]
            if left_val is not None:
                current_node.left = TreeNode(left_val)
                queue.append(current_node.left)
            else:
                current_node.left = None
            i += 1
        if i < len(values_list):
            right_val = values_list[i]
            if right_val is not None:
                current_node.right = TreeNode(right_val)
                queue.append(current_node.right)
            else:
                current_node.right = None
            i += 1
    return root

def test_example_1():
    head_vals = [4, 2, 8]
    root_vals = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    head = create_linked_list(head_vals)
    root = create_tree(root_vals)
    assert isSubPath(head, root) is True, "Example 1 should return True"

def test_example_2():
    head_vals = [1, 4, 2, 6]
    root_vals = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    head = create_linked_list(head_vals)
    root = create_tree(root_vals)
    assert isSubPath(head, root) is True, "Example 2 should return True"

def test_example_3():
    head_vals = [1, 4, 2, 6, 8]
    root_vals = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    head = create_linked_list(head_vals)
    root = create_tree(root_vals)
    assert isSubPath(head, root) is False, "Example 3 should return False"

def test_empty_linked_list():
    head = None
    root = create_tree([1])
    assert isSubPath(head, root) is True, "Empty linked list should return True"

def test_empty_tree():
    root = None
    head = create_linked_list([1])
    assert isSubPath(head, root) is False, "Empty tree should return False"
from solution import *
from collections import deque

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def build_tree(values):
    if not values:
        return None
    idx = 0
    root = TreeNode(values[idx])
    idx += 1
    queue = deque([root])
    while queue and idx < len(values):
        node = queue.popleft()
        if values[idx] is not None:
            node.left = TreeNode(values[idx])
            queue.append(node.left)
        idx += 1
        if idx < len(values) and values[idx] is not None:
            node.right = TreeNode(values[idx])
            queue.append(node.right)
        idx += 1
    return root

def test_example_1():
    head = build_linked_list([4,2,8])
    root_values = [1,4,4, None,2,2, None,1, None,6,8, None, None, None, None,1,3]
    root = build_tree(root_values)
    assert is_sub_path(head, root) is True

def test_example_2():
    head = build_linked_list([1,4,2,6])
    root_values = [1,4,4, None,2,2, None,1, None,6,8, None, None, None, None,1,3]
    root = build_tree(root_values)
    assert is_sub_path(head, root) is True

def test_example_3():
    head = build_linked_list([1,4,2,6,8])
    root_values = [1,4,4, None,2,2, None,1, None,6,8, None, None, None, None,1,3]
    root = build_tree(root_values)
    assert is_sub_path(head, root) is False

def test_case_4():
    head = build_linked_list([1,2])
    root_values = [1,3,1, None, None, 2, None]
    root = build_tree(root_values)
    assert is_sub_path(head, root) is True

def test_head_none():
    head = None
    root = build_tree([0])
    assert is_sub_path(head, root) is True

def test_root_none():
    head = build_linked_list([1])
    root = None
    assert is_sub_path(head, root) is False
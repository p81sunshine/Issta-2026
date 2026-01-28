from solution import *

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
    root = TreeNode(values[0])
    queue = [root]
    idx = 1
    while queue and idx < len(values):
        node = queue.pop(0)
        if idx < len(values):
            left_val = values[idx]
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            else:
                node.left = None
            idx += 1
        if idx < len(values):
            right_val = values[idx]
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
            else:
                node.right = None
            idx += 1
    return root

def test_example_1():
    head_values = [4, 2, 8]
    tree_values = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    head = build_linked_list(head_values)
    root = build_tree(tree_values)
    assert isSubPath(head, root) is True, "Example 1 failed"

def test_example_2():
    head_values = [1, 4, 2, 6]
    tree_values = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    head = build_linked_list(head_values)
    root = build_tree(tree_values)
    assert isSubPath(head, root) is True, "Example 2 failed"

def test_example_3():
    head_values = [1, 4, 2, 6, 8]
    tree_values = [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3]
    head = build_linked_list(head_values)
    root = build_tree(tree_values)
    assert isSubPath(head, root) is False, "Example 3 failed"

def test_empty_list():
    head = None
    tree_values = [1]
    root = build_tree(tree_values)
    assert isSubPath(head, root) is True, "Empty list should return True"

def test_empty_tree():
    head = build_linked_list([1])
    root = None
    assert isSubPath(head, root) is False, "Empty tree should return False"

def test_single_node():
    head_values = [1]
    tree_values = [1, 2, 3]
    head = build_linked_list(head_values)
    root = build_tree(tree_values)
    assert isSubPath(head, root) is True, "Single node in list should match root"
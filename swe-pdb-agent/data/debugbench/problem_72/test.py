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
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def test_example_1():
    head_values = [4,2,8]
    root_values = [1,4,4, None,2,2, None,1, None,6,8, None, None, None, None,1,3]
    head = build_linked_list(head_values)
    root = build_tree(root_values)
    assert isSubPath(head, root) is True, "Example 1 should return True"

def test_example_2():
    head_values = [1,4,2,6]
    root_values = [1,4,4, None,2,2, None,1, None,6,8, None, None, None, None,1,3]
    head = build_linked_list(head_values)
    root = build_tree(root_values)
    assert isSubPath(head, root) is True, "Example 2 should return True"

def test_example_3():
    head_values = [1,4,2,6,8]
    root_values = [1,4,4, None,2,2, None,1, None,6,8, None, None, None, None,1,3]
    head = build_linked_list(head_values)
    root = build_tree(root_values)
    assert isSubPath(head, root) is False, "Example 3 should return False"

def test_edge_case_head_empty():
    head = None
    root = build_tree([1])
    assert isSubPath(head, root) is True, "Empty head should always return True"

def test_edge_case_root_empty():
    head = build_linked_list([1])
    root = None
    assert isSubPath(head, root) is False, "Empty root with non-empty head should return False"
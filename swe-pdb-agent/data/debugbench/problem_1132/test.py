from solution import *

def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def list_to_tree(level_order):
    if not level_order:
        return None
    root = TreeNode(level_order[0])
    queue = [root]
    idx = 1
    while idx < len(level_order) and queue:
        current_node = queue.pop(0)
        if idx < len(level_order):
            if level_order[idx] is not None:
                current_node.left = TreeNode(level_order[idx])
                queue.append(current_node.left)
            else:
                current_node.left = None
            idx += 1
        if idx < len(level_order):
            if level_order[idx] is not None:
                current_node.right = TreeNode(level_order[idx])
                queue.append(current_node.right)
            else:
                current_node.right = None
            idx += 1
    return root

def test_example_1():
    head = list_to_linkedlist([4,2,8])
    root = list_to_tree([1,4,4, None, 2,2, None, 1, None, 6,8, None, None, None, None, 1,3])
    assert isSubPath(head, root) == True, "Example 1 should return True"

def test_example_2():
    head = list_to_linkedlist([1,4,2,6])
    root = list_to_tree([1,4,4, None, 2,2, None, 1, None, 6,8, None, None, None, None, 1,3])
    assert isSubPath(head, root) == True, "Example 2 should return True"

def test_example_3():
    head = list_to_linkedlist([1,4,2,6,8])
    root = list_to_tree([1,4,4, None, 2,2, None, 1, None, 6,8, None, None, None, None, 1,3])
    assert isSubPath(head, root) == False, "Example 3 should return False"

def test_minimal_case():
    head = list_to_linkedlist([1,2])
    root = list_to_tree([1, None, 2])
    assert isSubPath(head, root) == True, "Minimal case should return True"

def test_no_match_case():
    head = list_to_linkedlist([1,3])
    root = list_to_tree([1, 2, None])
    assert isSubPath(head, root) == False, "No matching path should return False"
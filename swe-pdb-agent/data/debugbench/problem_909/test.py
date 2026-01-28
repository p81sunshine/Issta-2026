from solution import *
from collections import deque

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        current = queue.popleft()
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1
    return root

def test_example_1():
    root = build_tree([3,9,20,None,None,15,7])
    assert levelOrderBottom(root) == [[15,7],[9,20],[3]], "Test case 1 failed"

def test_example_2():
    root = build_tree([1])
    assert levelOrderBottom(root) == [[1]], "Test case 2 failed"

def test_example_3():
    root = build_tree([])
    assert levelOrderBottom(root) == [], "Test case 3 failed"

def test_edge_case_empty_queue():
    # Test when processing leads to empty queue
    root = build_tree([1, 2])
    assert levelOrderBottom(root) == [[2], [1]], "Edge case with partial tree failed"
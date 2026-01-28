from solution import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(list_values):
    if not list_values:
        return None
    root = TreeNode(list_values[0])
    queue = [root]
    i = 1
    while queue and i < len(list_values):
        current = queue.pop(0)
        if list_values[i] is not None:
            current.left = TreeNode(list_values[i])
            queue.append(current.left)
        else:
            current.left = None
        i += 1
        if i < len(list_values) and list_values[i] is not None:
            current.right = TreeNode(list_values[i])
            queue.append(current.right)
        else:
            current.right = None
        i += 1
    return root

def test_example_1():
    root = build_tree([1, None, 2, 3])
    expected = [1, 3, 2]
    result = inorderTraversal(root)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_2():
    root = build_tree([])
    expected = []
    result = inorderTraversal(root)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_3():
    root = build_tree([1])
    expected = [1]
    result = inorderTraversal(root)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_additional_case():
    root = build_tree([3, 1, 5, 0, 2, 4, 6])
    expected = [0, 1, 2, 3, 4, 5, 6]
    result = inorderTraversal(root)
    assert result == expected, f"Expected {expected}, but got {result}"
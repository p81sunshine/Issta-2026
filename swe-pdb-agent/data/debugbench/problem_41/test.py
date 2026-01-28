from solution import *

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree(list_input):
    if not list_input:
        return None
    root = TreeNode(list_input[0])
    queue = [root]
    i = 1
    while queue and i < len(list_input):
        current = queue.pop(0)
        if i < len(list_input):
            if list_input[i] is not None:
                current.left = TreeNode(list_input[i])
                queue.append(current.left)
            i += 1
        if i < len(list_input):
            if list_input[i] is not None:
                current.right = TreeNode(list_input[i])
                queue.append(current.right)
            i += 1
    return root

def test_example_1():
    root = build_tree([1, None, 2, 3])
    result = inorder_traversal(root)
    assert result == [1, 3, 2], "Expected [1,3,2] for input [1,null,2,3]"

def test_example_2():
    root = build_tree([])
    result = inorder_traversal(root)
    assert result == [], "Expected [] for empty input"

def test_example_3():
    root = build_tree([1])
    result = inorder_traversal(root)
    assert result == [1], "Expected [1] for input [1]"

def test_left_skewed_tree():
    # Left-skewed tree: [4,2,5,1,3]
    root = TreeNode(4)
    root.left = TreeNode(2, TreeNode(1), TreeNode(3))
    root.right = TreeNode(5)
    expected = [1, 2, 3, 4, 5]
    result = inorder_traversal(root)
    assert result == expected, f"Expected {expected} for left-skewed tree"
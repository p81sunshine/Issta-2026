from solution import *
from collections import deque

def tree_to_list(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Trim trailing Nones
    while result and result[-1] is None:
        result.pop()
    return result

def test_example_1():
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    expected = [3,9,20,None,None,15,7]
    root = buildTree(preorder, inorder)
    assert tree_to_list(root) == expected, "Failed for example 1"

def test_example_2():
    preorder = [-1]
    inorder = [-1]
    expected = [-1]
    root = buildTree(preorder, inorder)
    assert tree_to_list(root) == expected, "Failed for example 2"

def test_left_right_swap_case():
    preorder = [1,2]
    inorder = [2,1]
    expected = [1,2]
    root = buildTree(preorder, inorder)
    assert tree_to_list(root) == expected, "Left-right swap case failed"

def test_another_swap_case():
    preorder = [3,1,2]
    inorder = [1,3,2]
    expected = [3,1,2]
    root = buildTree(preorder, inorder)
    assert tree_to_list(root) == expected, "Another swap case failed"
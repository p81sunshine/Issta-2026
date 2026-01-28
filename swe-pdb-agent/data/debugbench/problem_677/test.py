from solution import *

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            if values[i] is not None:
                node.left = TreeNode(values[i])
                queue.append(node.left)
            i += 1
        if i < len(values):
            if values[i] is not None:
                node.right = TreeNode(values[i])
                queue.append(node.right)
            i += 1
    return root

def test_case_1():
    root = build_tree([3,9,20,None,None,15,7])
    expected = [[15,7],[9,20],[3]]
    assert levelOrderBottom(root) == expected, "Test case 1 failed"

def test_case_2():
    root = build_tree([1])
    expected = [[1]]
    assert levelOrderBottom(root) == expected, "Test case 2 failed"

def test_case_3():
    root = build_tree([])
    expected = None  # Correct code returns None for empty tree
    assert levelOrderBottom(root) == expected, "Test case 3 failed"

def test_case_4():
    root = build_tree([1,2,3])
    expected = [[2,3],[1]]
    assert levelOrderBottom(root) == expected, "Test case 4 failed"
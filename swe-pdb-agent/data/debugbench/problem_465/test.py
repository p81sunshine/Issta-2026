from solution import *

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
    root = build_tree([3,9,20,None,None,15,7])
    expected = [[15,7],[9,20],[3]]
    actual = levelOrderBottom(root)
    assert actual == expected, f"Example 1 failed. Expected {expected}, got {actual}"

def test_example_2():
    root = build_tree([1])
    expected = [[1]]
    actual = levelOrderBottom(root)
    assert actual == expected, f"Example 2 failed. Expected {expected}, got {actual}"

def test_null_child():
    root = build_tree([1, None, 2])
    expected = [[2], [1]]
    actual = levelOrderBottom(root)
    assert actual == expected, f"Test null child failed. Expected {expected}, got {actual}"

def test_empty_tree():
    root = build_tree([])
    expected = None
    actual = levelOrderBottom(root)
    assert actual == expected, f"Test empty tree failed. Expected {expected}, got {actual}"
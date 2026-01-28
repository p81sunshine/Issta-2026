from solution import *

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    idx = 1
    while queue and idx < len(values):
        current = queue.pop(0)
        if idx < len(values):
            if values[idx] is not None:
                current.left = TreeNode(values[idx])
                queue.append(current.left)
            idx += 1
        if idx < len(values):
            if values[idx] is not None:
                current.right = TreeNode(values[idx])
                queue.append(current.right)
            idx += 1
    return root

def test_example_1():
    root = build_tree([3,9,20,None,None,15,7])
    expected = [[15,7], [9,20], [3]]
    result = levelOrderBottom(root)
    assert result == expected, f"Expected {expected} but got {result}"

def test_example_2():
    root = build_tree([1])
    expected = [[1]]
    result = levelOrderBottom(root)
    assert result == expected, f"Expected {expected} but got {result}"

def test_example_3():
    root = build_tree([])
    expected = None
    result = levelOrderBottom(root)
    assert result == expected, f"Expected {expected} but got {result}"
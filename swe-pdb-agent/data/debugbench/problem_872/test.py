from solution import *

def build_tree(level_order):
    if not level_order:
        return None
    root = TreeNode(level_order[0])
    i = 1
    queue = [root]
    while queue and i < len(level_order):
        current = queue.pop(0)
        if i < len(level_order):
            val = level_order[i]
            if val is not None:
                current.left = TreeNode(val)
                queue.append(current.left)
            i += 1
        if i < len(level_order):
            val = level_order[i]
            if val is not None:
                current.right = TreeNode(val)
                queue.append(current.right)
            i += 1
    return root

def test_example_1():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    expected = [[15, 7], [9, 20], [3]]
    result = levelOrderBottom(root)
    assert result == expected, "Test case 1 failed: Incorrect level order reversal"

def test_example_2():
    root = build_tree([1])
    expected = [[1]]
    result = levelOrderBottom(root)
    assert result == expected, "Test case 2 failed: Single node tree"

def test_three_level_tree():
    root = build_tree([1, 2, 3, 4, 5])
    expected = [[4, 5], [2, 3], [1]]
    result = levelOrderBottom(root)
    assert result == expected, "Test case 3 failed: Three-level tree reversal"

def test_empty_tree():
    root = build_tree([])
    expected = None
    result = levelOrderBottom(root)
    assert result == expected, "Test case 4 failed: Empty tree should return None"
from solution import *

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    idx = 1
    while queue and idx < len(values):
        node = queue.pop(0)
        if idx < len(values):
            val = values[idx]
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            idx += 1
        if idx < len(values):
            val = values[idx]
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
            idx += 1
    return root

def test_case_1():
    root = build_tree([3, 9, 20, None, None, 15, 7])
    expected = [[15, 7], [9, 20], [3]]
    assert level_order_bottom(root) == expected, "Test case 1 failed"

def test_case_2():
    root = build_tree([1])
    expected = [[1]]
    assert level_order_bottom(root) == expected, "Test case 2 failed"

def test_case_3():
    root = build_tree([])
    expected = None
    assert level_order_bottom(root) == expected, "Test case 3 failed"

def test_case_4():
    root = build_tree([1, 2])
    expected = [[2], [1]]
    assert level_order_bottom(root) == expected, "Test case 4 failed"
from solution import *

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while i < len(values):
        current = queue.pop(0)
        if values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        else:
            current.left = None
        i += 1
        if i < len(values):
            if values[i] is not None:
                current.right = TreeNode(values[i])
                queue.append(current.right)
            else:
                current.right = None
            i += 1
    return root

def test_example_1():
    root = build_tree([3,9,20,None,None,15,7])
    assert level_order_bottom(root) == [[15,7],[9,20],[3]]

def test_example_2():
    root = build_tree([1])
    assert level_order_bottom(root) == [[1]]

def test_example_3():
    root = build_tree([])
    assert level_order_bottom(root) == []

def test_additional_case():
    root = build_tree([1, None, 2])
    assert level_order_bottom(root) == [[2], [1]]
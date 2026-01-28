from solution import *

def build_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    index = 1
    while queue and index < len(values):
        node = queue.pop(0)
        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1
        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1
    return root

def test_example_1():
    root = build_tree([1, None, 2, 3])
    assert inorder_traversal(root) == [1, 3, 2], "Test case 1 failed"

def test_example_2():
    root = build_tree([])
    assert inorder_traversal(root) == [], "Test case 2 failed"

def test_example_3():
    root = build_tree([1])
    assert inorder_traversal(root) == [1], "Test case 3 failed"

def test_additional_case():
    root = build_tree([1, 2, 3])
    assert inorder_traversal(root) == [2, 1, 3], "Test additional case failed"

def test_complex_case():
    root = build_tree([3, 1, 4, None, 2])
    expected = [1, 2, 3, 4]
    assert inorder_traversal(root) == expected, "Test complex case failed"
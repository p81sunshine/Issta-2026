from solution import *

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        current = queue.pop(0)
        if i < len(lst) and lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

def test_example_1():
    root = list_to_tree([3,9,20,None,None,15,7])
    assert maxDepth(root) == 3, "Test case 1 failed"

def test_example_2():
    root = list_to_tree([1,None,2])
    assert maxDepth(root) == 2, "Test case 2 failed"

def test_empty_tree():
    root = list_to_tree([])
    assert maxDepth(root) == 0, "Empty tree should have depth 0"

def test_single_node():
    root = list_to_tree([1])
    assert maxDepth(root) == 1, "Single node tree should have depth 1"

def test_linear_tree():
    root = TreeNode(5)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.right.right = TreeNode(8)
    assert maxDepth(root) == 4, "Linear tree depth calculation failed"
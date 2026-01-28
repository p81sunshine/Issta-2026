from solution import *

def create_tree_from_list(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        current = queue.pop(0)
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

def test_example_1():
    root = create_tree_from_list([3,9,20,None,None,15,7])
    expected = [[15,7],[9,20],[3]]
    assert levelOrderBottom(root) == expected, "Failed for example 1"

def test_example_2():
    root = create_tree_from_list([1])
    expected = [[1]]
    assert levelOrderBottom(root) == expected, "Failed for example 2"

def test_example_3():
    root = create_tree_from_list([])
    expected = None
    assert levelOrderBottom(root) == expected, "Failed for example 3"
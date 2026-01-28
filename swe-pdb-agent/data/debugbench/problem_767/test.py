from solution import *

def list_to_tree(lst):
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
        else:
            current.left = None
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        else:
            current.right = None
        i += 1
    return root

def test_example_1():
    root = list_to_tree([3,9,20,None,None,15,7])
    expected = [[15,7], [9,20], [3]]
    assert levelOrderBottom(root) == expected, "Failed on example 1"

def test_example_2():
    root = list_to_tree([1])
    expected = [[1]]
    assert levelOrderBottom(root) == expected, "Failed on example 2"

def test_example_3():
    root = list_to_tree([])
    expected = None
    assert levelOrderBottom(root) == expected, "Failed on example 3"

def test_three_levels():
    root = list_to_tree([1,2,3,4,5,6,7])
    expected = [[4,5,6,7], [2,3], [1]]
    assert levelOrderBottom(root) == expected, "Failed on three-level tree"
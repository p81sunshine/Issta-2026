from solution import *
from collections import deque

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = deque([root])
    i = 1
    while queue and i < len(lst):
        current = queue.popleft()
        if lst[i] is not None:
            current.left = TreeNode(lst[i])
            queue.append(current.left)
        else:
            current.left = None
        i += 1
        if i < len(lst):
            if lst[i] is not None:
                current.right = TreeNode(lst[i])
                queue.append(current.right)
            else:
                current.right = None
            i += 1
        else:
            break
    return root

def test_example_1():
    root = list_to_tree([3,9,20,None,None,15,7])
    assert levelOrderBottom(root) == [[15,7],[9,20],[3]], "Test case 1 failed"

def test_example_2():
    root = list_to_tree([1])
    assert levelOrderBottom(root) == [[1]], "Test case 2 failed"

def test_example_3():
    root = list_to_tree([])
    assert levelOrderBottom(root) == [], "Test case 3 failed"

def test_two_levels():
    root = list_to_tree([1,2,3])
    assert levelOrderBottom(root) == [[2,3],[1]], "Test two levels failed"

def test_skewed_tree():
    root = list_to_tree([1,2,None,3])
    assert levelOrderBottom(root) == [[3],[2],[1]], "Test skewed tree failed"
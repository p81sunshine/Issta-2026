from solution import *

def list_to_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while i < len(lst):
        current = queue.pop(0)
        if i < len(lst):
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
    return root

def test_example_1():
    root = list_to_tree([5,8,9,2,1,3,7,4,6])
    assert kthLargestLevelSum(root, 2) == 13, "Failed for example 1"

def test_example_2():
    root = list_to_tree([1,2,None,3])
    assert kthLargestLevelSum(root, 1) == 3, "Failed for example 2"

def test_k_larger_than_levels():
    root = list_to_tree([1])
    assert kthLargestLevelSum(root, 2) == -1, "Should return -1 when k exceeds level count"

def test_single_node():
    root = list_to_tree([10])
    assert kthLargestLevelSum(root, 1) == 10, "Should return value of single node for k=1"
    assert kthLargestLevelSum(root, 2) == -1, "Should return -1 for k=2 in single-node tree"
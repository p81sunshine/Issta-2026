from solution import *

def build_tree(lst):
    if not lst:
        return None
    root = TreeNode(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        node = queue.pop(0)
        if lst[i] is not None:
            node.left = TreeNode(lst[i])
            queue.append(node.left)
        i += 1
        if i < len(lst) and lst[i] is not None:
            node.right = TreeNode(lst[i])
            queue.append(node.right)
        i += 1
    return root

def test_example_1():
    root = build_tree([5,8,9,2,1,3,7,4,6])
    k = 2
    expected = 13
    result = kthLargestLevelSum(root, k)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_example_2():
    root = build_tree([1,2,None,3])
    k = 1
    expected = 3
    result = kthLargestLevelSum(root, k)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_case_two_levels_k_1():
    root = build_tree([1,3,2])
    k = 1
    expected = 5
    result = kthLargestLevelSum(root, k)
    assert result == expected, f"Expected {expected}, but got {result}"

def test_k_larger_than_levels():
    root = build_tree([1])
    k = 2
    expected = -1
    result = kthLargestLevelSum(root, k)
    assert result == expected, f"Expected {expected}, but got {result}"
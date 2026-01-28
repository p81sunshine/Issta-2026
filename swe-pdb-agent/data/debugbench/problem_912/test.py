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
        i += 1
        if i < len(lst) and lst[i] is not None:
            current.right = TreeNode(lst[i])
            queue.append(current.right)
        i += 1
    return root

def test_example_1():
    root = list_to_tree([5,8,9,2,1,3,7,4,6])
    assert kthLargestLevelSum(root, 2) == 13, "Failed on first example case"

def test_example_2():
    root = list_to_tree([1,2,None,3])
    assert kthLargestLevelSum(root, 1) == 3, "Failed on second example case"

def test_edge_case_k_larger_than_levels():
    root = list_to_tree([1])
    assert kthLargestLevelSum(root, 2) == -1, "Failed when k exceeds level count"

def test_edge_case_single_node():
    root = list_to_tree([5])
    assert kthLargestLevelSum(root, 1) == 5, "Failed single-node case"

def test_level_with_same_sum():
    root = list_to_tree([3, 1, 2])
    assert kthLargestLevelSum(root, 2) == 3, "Failed same-sum level case"

def test_k_1_with_multiple_levels():
    root = list_to_tree([10,20])
    assert kthLargestLevelSum(root, 1) == 20, "Failed top-level sum case"
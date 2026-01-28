from solution import *

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_tree(arr):
    if not arr:
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while i < len(arr):
        node = queue.pop(0)
        if i < len(arr):
            val = arr[i]
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
            else:
                node.left = None
            i += 1
        if i < len(arr):
            val = arr[i]
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
            else:
                node.right = None
            i += 1
    return root

def test_example_1():
    root = create_tree([0,1,2,3,4,3,4])
    assert smallestFromLeaf(root) == "dba"

def test_example_2():
    root = create_tree([25,1,3,1,3,0,2])
    assert smallestFromLeaf(root) == "adz"

def test_example_3():
    root = create_tree([2,2,1,None,1,0,None,0])
    assert smallestFromLeaf(root) == "abc"

def test_single_node():
    root = create_tree([0])
    assert smallestFromLeaf(root) == "a"

def test_two_nodes():
    root = create_tree([1,0])
    assert smallestFromLeaf(root) == "ab"
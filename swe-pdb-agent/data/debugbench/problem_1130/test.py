from solution import *

def test_example_1():
    # Construct input [1,null,3,2,4,null,5,6]
    root = Node(1)
    child3 = Node(3)
    child2 = Node(2, [])
    child4 = Node(4, [])
    root.children = [child3, child2, child4]
    child5 = Node(5, [])
    child6 = Node(6, [])
    child3.children = [child5, child6]
    assert maxDepth(root) == 3, "Example 1 should return 3"

def test_example_2():
    # Construct a tree leading to depth 5
    root = Node(1)
    # Level 2 children: 2, 3, 4, 5
    root.children = [Node(2, []), Node(3, []), Node(4, []), Node(5, [])]
    # Node 3 (index 1) has children 6, 7
    node3 = root.children[1]
    node3.children = [Node(6, []), Node(7, [])]
    # Node 7 (index 1 of node3's children) has child 8
    node7 = node3.children[1]
    node7.children = [Node(8, [])]
    # Node 8 has child 9
    node8 = node7.children[0]
    node8.children = [Node(9, [])]
    assert maxDepth(root) == 5, "Example 2 should return 5"

def test_single_node():
    root = Node(1, [])
    assert maxDepth(root) == 1, "Single node tree should have depth 1"

def test_single_child():
    root = Node(1, [Node(2, [])])
    assert maxDepth(root) == 2, "Single child should result in depth 2"

def test_empty_tree():
    assert maxDepth(None) == 0, "Empty tree should have depth 0"
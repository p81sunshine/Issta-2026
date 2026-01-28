from solution import *

def test_example_1():
    root = Node(1, [
        Node(3, [Node(5, []), Node(6, [])]),
        Node(2, []),
        Node(4, [])
    ])
    assert maxDepth(root) == 3, "Example 1 failed"

def test_example_2():
    root = Node(1, [
        Node(2, [
            Node(6, [
                Node(11, [
                    Node(12, [])
                ])
            ]),
            Node(7, [])
        ]),
        Node(3, [
            Node(8, [
                Node(13, [
                    Node(14, [])
                ])
            ])
        ]),
        Node(4, [
            Node(9, []),
            Node(10, [])
        ]),
        Node(5, [])
    ])
    assert maxDepth(root) == 5, "Example 2 failed"

def test_empty():
    assert maxDepth(None) == 0, "Empty tree test failed"

def test_single_node():
    root = Node(1, [])
    assert maxDepth(root) == 1, "Single node test failed"

def test_two_levels():
    root = Node(1, [Node(2, []), Node(3, [])])
    assert maxDepth(root) == 2, "Two levels test failed"
from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import parse_string, Node

def inorder_traversal(root):
    if root is None:
        return []
    return inorder_traversal(root.left) + [root.value] + inorder_traversal(root.right)

def test_parse_simple_expression():
    expr = "a + b"
    tree = parse_string(expr)
    assert inorder_traversal(tree) == ['a', '+', 'b']

def test_parse_expression_with_parentheses():
    expr = "((a+b)+c) + d"
    tree = parse_string(expr)
    assert inorder_traversal(tree) == ['a', '+', 'b', '+', 'c', '+', 'd']

def test_parse_expression_with_multiple_operators():
    expr = "a*b + c/d"
    tree = parse_string(expr)
    assert inorder_traversal(tree) == ['a', '*', 'b', '+', 'c', '/', 'd']

def test_parse_expression_with_nested_parentheses():
    expr = "(a + (b + c)) * d"
    tree = parse_string(expr)
    assert inorder_traversal(tree) == ['a', '+', 'b', '+', 'c', '*', 'd']
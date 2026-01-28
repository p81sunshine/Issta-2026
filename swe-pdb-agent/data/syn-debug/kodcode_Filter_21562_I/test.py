from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import BinaryTree

def test_dfs_combinations():
    tree = BinaryTree()
    tree.insert(8)
    tree.insert(3)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(14)
    tree.insert(4)
    tree.insert(7)
    tree.insert(13)
    
    expected_dfs_result = [
        [8],
        [8, 3],
        [8, 3, 1],
        [8, 3, 6],
        [8, 3, 6, 4],
        [8, 3, 6, 7],
        [8, 10],
        [8, 10, 14],
        [8, 10, 14, 13]
    ]
    
    assert tree.dfs_combinations() == expected_dfs_result

def test_bfs_combinations():
    tree = BinaryTree()
    tree.insert(8)
    tree.insert(3)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(14)
    tree.insert(4)
    tree.insert(7)
    tree.insert(13)
    
    expected_bfs_result = [
        [8],
        [8, 3],
        [8, 10],
        [8, 3, 1],
        [8, 3, 6],
        [8, 10, 14],
        [8, 3, 6, 4],
        [8, 3, 6, 7],
        [8, 10, 14, 13]
    ]
    
    assert tree.bfs_combinations() == expected_bfs_result
from solution import *

import math

from solution import *

import math

from solution import *

import math

def test_longest_path_dag():
    # Test Case 1
    N, M = 4, 4
    edges = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (1, 3, 2)]
    assert longest_path_dag(N, M, edges) == 12

    # Test Case 2
    N, M = 3, 2
    edges = [(1, 2, 5), (2, 3, 7)]
    assert longest_path_dag(N, M, edges) == 12
    
    # Test Case 3
    N, M = 3, 1
    edges = [(1, 2, 1)]
    assert longest_path_dag(N, M, edges) == 1
    
    # Test Case 4 - Disconnected Graph
    N, M = 3, 1
    edges = [(1, 2, 1)]
    assert longest_path_dag(N, M, edges) == 1

    # Test Case 5 - Graph with no edges
    N, M = 4, 0
    edges = []
    assert longest_path_dag(N, M, edges) == 0
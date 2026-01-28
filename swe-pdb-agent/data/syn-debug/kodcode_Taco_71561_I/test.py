from solution import *

import math

from solution import *

import math

from solution import *

import math

def test_unique_paths_with_obstacles():
    grid1 = [
        ['.', '.', '.'],
        ['.', '#', '.'],
        ['.', '.', '.']
    ]
    assert unique_paths_with_obstacles(grid1) == 2
    
    grid2 = [
        ['.', '#'],
        ['#', '.']
    ]
    assert unique_paths_with_obstacles(grid2) == 0
    
    grid3 = [
        ['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']
    ]
    assert unique_paths_with_obstacles(grid3) == 6
    
    grid4 = [
        ['#', '.'],
        ['.', '.']
    ]
    assert unique_paths_with_obstacles(grid4) == 0
    
    grid5 = [
        ['.', '.'],
        ['.', '#']
    ]
    assert unique_paths_with_obstacles(grid5) == 0
    
    grid6 = [
        ['.', '.', '#'],
        ['.', '#', '.'],
        ['#', '.', '.']
    ]
    assert unique_paths_with_obstacles(grid6) == 0

def test_empty_single_cell():
    grid = [['.']]
    assert unique_paths_with_obstacles(grid) == 1

def test_obstacle_single_cell():
    grid = [['#']]
    assert unique_paths_with_obstacles(grid) == 0
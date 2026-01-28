from solution import *

import math

from solution import *

import math

from solution import *

import math

def test_rotate_matrix_90_degrees():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    assert rotate_matrix_90_degrees(matrix) == expected

def test_rotate_matrix():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    # Rotate 2 times
    expected_twice = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]
    assert rotate_matrix(matrix, 2) == expected_twice
    
    # Rotate 3 times
    expected_thrice = [
        [3, 6, 9],
        [2, 5, 8],
        [1, 4, 7]
    ]
    assert rotate_matrix(matrix, 3) == expected_thrice

def test_solve_game_configuration():
    n = 3
    l = 2
    initial_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    levels = [2, 3]
    expected_result = [
        [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ],
        [
            [3, 6, 9],
            [2, 5, 8],
            [1, 4, 7]
        ]
    ]
    assert solve_game_configuration(n, l, initial_matrix, levels) == expected_result
from solution import *

import math

from solution import *

import math

from solution import *

import math

import pytest
from solution import longest_connected_path

def test_example_1():
    n = 4
    grid = [
        '.X..',
        '.X..',
        '..X.',
        '....'
    ]
    assert longest_connected_path(n, grid) == 4

def test_example_2():
    n = 5
    grid = [
        'X....',
        '.XX..',
        '..X..',
        '....X',
        'XXXXX'
    ]
    assert longest_connected_path(n, grid) == 5

def test_all_empty():
    n = 3
    grid = [
        '...',
        '...',
        '...'
    ]
    assert longest_connected_path(n, grid) == 3

def test_all_obstacles():
    n = 2
    grid = [
        'XX',
        'XX'
    ]
    assert longest_connected_path(n, grid) == 2

def test_mixed():
    n = 3
    grid = [
        'X.X',
        '.X.',
        'X.X'
    ]
    assert longest_connected_path(n, grid) == 1

def test_single_element():
    n = 1
    grid = [
        'X'
    ]
    assert longest_connected_path(n, grid) == 1

    grid = [
        '.'
    ]
    assert longest_connected_path(n, grid) == 1
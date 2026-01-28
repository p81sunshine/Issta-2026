from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import max_load_transport

def test_example_case():
    m = 5
    w = 6
    A = 1
    B = 5
    edges = [
        (1, 2, 100),
        (2, 3, 50),
        (3, 5, 100),
        (1, 4, 200),
        (4, 5, 300),
        (2, 4, 150)
    ]
    assert max_load_transport(m, w, A, B, edges) == 200

def test_simple_case():
    m = 2
    w = 1
    A = 1
    B = 2
    edges = [
        (1, 2, 100)
    ]
    assert max_load_transport(m, w, A, B, edges) == 100

def test_no_path_case():
    m = 3
    w = 2
    A = 1
    B = 3
    edges = [
        (1, 2, 100),
        (2, 3, 100)
    ]
    assert max_load_transport(m, w, A, B, edges) == 100

def test_multiple_paths():
    m = 4
    w = 5
    A = 1
    B = 4
    edges = [
        (1, 2, 100),
        (2, 3, 50),
        (3, 4, 100),
        (1, 3, 200),
        (3, 4, 150)
    ]
    assert max_load_transport(m, w, A, B, edges) == 150

def test_large_capacity():
    m = 3
    w = 2
    A = 1
    B = 3
    edges = [
        (1, 2, 5000),
        (2, 3, 3000)
    ]
    assert max_load_transport(m, w, A, B, edges) == 3000
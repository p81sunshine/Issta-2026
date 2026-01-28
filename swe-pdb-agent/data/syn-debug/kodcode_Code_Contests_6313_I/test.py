from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import find_order, process_input

def test_find_order_no_dependencies():
    assert find_order(3, []) == [0, 1, 2] or find_order(3, []) == [2, 1, 0]

def test_find_order_linear_dependencies():
    assert find_order(4, [(1, 0), (2, 1), (3, 2)]) == [0, 1, 2, 3]

def test_find_order_multiple_possible_orders():
    result = find_order(3, [(2, 1), (1, 0)])
    assert result in [[0, 1, 2]]

def test_find_order_cycle_detected():
    assert find_order(3, [(0, 1), (1, 2), (2, 0)]) == "Cycle detected"

def test_process_input():
    data = """4 3
1 0
2 1
3 2

3 2
2 1
1 0

3 2
2 1
1 0
2 0

3 4
2 1
1 0
2 0
0 2

0 0"""
    expected = [
        "0 1 2 3",
        "0 1 2",
        "0 1 2",
        "Cycle detected"
    ]
    assert process_input(data) == expected
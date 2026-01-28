from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import solve_2_sat

def test_solve_2_sat_valid_solution():
    formula = [(('x', False), ('y', False)),
               (('y', True), ('y', True)),
               (('a', False), ('b', False)),
               (('a', True), ('c', True)),
               (('c', False), ('b', True))]
    solution = solve_2_sat(formula)
    assert solution is not None
    assert solution['x'] == True or solution['y'] == True
    assert solution['y'] == False or solution['y'] == False
    assert solution['a'] == True or solution['b'] == True
    assert solution['a'] == False or solution['c'] == False
    assert solution['c'] == True or solution['b'] == False

def test_solve_2_sat_no_solution():
    formula = [(('x', False), ('x', False)),
               (('x', True), ('x', True))]
    solution = solve_2_sat(formula)
    assert solution is None

def test_solve_2_sat_single_variable():
    formula = [(('x', False), ('x', True))]
    solution = solve_2_sat(formula)
    assert solution == {'x': True}

def test_solve_2_sat_complex_valid_solution():
    formula = [(('a', True), ('b', False)),
               (('b', True), ('c', False)),
               (('c', True), ('a', True))]
    solution = solve_2_sat(formula)
    assert solution is not None
    assert isinstance(solution, dict)
    assert solution['a'] or solution['b']
    assert solution['b'] or solution['c']
    assert solution['c'] or solution['a']

def test_solve_2_sat_redundant_clauses():
    formula = [(('x', False), ('y', False)),
               (('x', False), ('y', False))]
    solution = solve_2_sat(formula)
    assert solution is not None
    assert solution['x'] or solution['y']
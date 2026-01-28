from solution import *

import math

from solution import *

import math

from solution import *

import math

from solution import solve

def test_example_1():
    input_str = "2\n3\n1: \n2: 1\n3: 2\n4\n1: \n2: \n3: 1 2\n4: 2 3\n"
    output = solve(input_str)
    assert output == ["1 2 3", "1 2 3 4"] or output == ["1 2 3", "2 1 3 4"]

def test_example_2():
    input_str = "1\n4\n1: 2\n2: 3\n3: 4\n4: 1\n"
    output = solve(input_str)
    assert output == ["IMPOSSIBLE"]

def test_no_dependencies():
    input_str = "1\n3\n1: \n2: \n3: \n"
    output = solve(input_str)
    assert output == ["1 2 3"] or output == ["1 3 2"] or output == ["2 1 3"] or output == ["2 3 1"] or output == ["3 1 2"] or output == ["3 2 1"]

def test_single_task():
    input_str = "1\n1\n1: \n"
    output = solve(input_str)
    assert output == ["1"]

def test_circular_dependency():
    input_str = "1\n2\n1: 2\n2: 1\n"
    output = solve(input_str)
    assert output == ["IMPOSSIBLE"]
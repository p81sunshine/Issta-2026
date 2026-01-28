from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_count_element_in_list_base():
    assert count_element_in_list([[1, 3], [5, 7], [1, 11], [1, 15, 7]], 1) == 3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'A') == 3
    assert count_element_in_list([['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']], 'E') == 1

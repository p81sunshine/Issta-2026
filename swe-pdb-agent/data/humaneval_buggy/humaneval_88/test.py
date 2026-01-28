from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_sort_array_base():
    assert sort_array([]) == []
    assert sort_array([5]) == [5]
    assert sort_array([2, 4, 3, 0, 1, 5]) == [0, 1, 2, 3, 4, 5]
    assert sort_array([2, 4, 3, 0, 1, 5, 6]) == [6, 5, 4, 3, 2, 1, 0]
    assert sort_array([2, 1]) == [1, 2]
    assert sort_array([15, 42, 87, 32, 11, 0]) == [0, 11, 15, 32, 42, 87]
    assert sort_array([21, 14, 23, 11]) == [23, 21, 14, 11]

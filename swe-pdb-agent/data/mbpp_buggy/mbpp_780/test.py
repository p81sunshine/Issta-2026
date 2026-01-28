from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_find_combinations_base():
    assert find_combinations([[1, 2, 3], [3, 4, 5]]) == [(4, 6, 8)]
    assert find_combinations([[2, 4], [6, 7], [5, 1], [6, 10]]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
    assert find_combinations([[3, 5], [7, 8], [6, 2], [7, 11]]) == [(10, 13), (9, 7), (10, 16), (13, 10), (14, 19), (13, 13)]
    assert find_combinations([[4, 6], [8, 9], [7, 3], [8, 12]]) == [(12, 15), (11, 9), (12, 18), (15, 12), (16, 21), (15, 15)]

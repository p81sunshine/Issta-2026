from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_count_nums_base():
    assert count_nums([]) == 0
    assert count_nums([-1, -2, 0]) == 0
    assert count_nums([1, 1, 2, -2, 3, 4, 5]) == 6
    assert count_nums([1, 6, 9, -6, 0, 1, 5]) == 5
    assert count_nums([1, 100, 98, -7, 1, -1]) == 4
    assert count_nums([12, 23, 34, -45, -56, 0]) == 5
    assert count_nums([0, 1]) == 1
    assert count_nums([1]) == 1

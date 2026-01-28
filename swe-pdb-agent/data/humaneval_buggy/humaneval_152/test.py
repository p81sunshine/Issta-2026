from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_compare_base():
    assert compare([1, 2, 3, 4, 5, 1], [1, 2, 3, 4, 2, -2]) == [0, 0, 0, 0, 3, 3]
    assert compare([0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]) == [0, 0, 0, 0, 0, 0]
    assert compare([1, 2, 3], [-1, -2, -3]) == [2, 4, 6]
    assert compare([1, 2, 3, 5], [-1, 2, 3, 4]) == [2, 0, 0, 1]

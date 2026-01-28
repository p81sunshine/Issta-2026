from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_merge_base():
    assert merge([['x', 'y'], ['a', 'b'], ['m', 'n']]) == [['x', 'a', 'm'], ['y', 'b', 'n']]
    assert merge([[1, 2], [3, 4], [5, 6], [7, 8]]) == [[1, 3, 5, 7], [2, 4, 6, 8]]
    assert merge([[[1], [2]], [[3], [4]], [[5], [6]], [[7], [8]]]) == [[[1], [3], [5], [7]], [[2], [4], [6], [8]]]

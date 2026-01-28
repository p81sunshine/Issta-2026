from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_pluck_base():
    assert pluck([4, 2, 3]) == [2, 1]
    assert pluck([1, 2, 3]) == [2, 1]
    assert pluck([]) == []
    assert pluck([5, 0, 3, 0, 4, 2]) == [0, 1]
    assert pluck([1, 2, 3, 0, 5, 3]) == [0, 3]
    assert pluck([5, 4, 8, 4, 8]) == [4, 1]
    assert pluck([7, 6, 7, 1]) == [6, 1]
    assert pluck([7, 9, 7, 1]) == []

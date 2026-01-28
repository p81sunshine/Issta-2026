from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_intersection_base():
    assert intersection([1, 2], [2, 3]) == 'NO'
    assert intersection([-1, 1], [0, 4]) == 'NO'
    assert intersection([-3, -1], [-5, 5]) == 'YES'
    assert intersection([-2, 2], [-4, 0]) == 'YES'
    assert intersection([-11, 2], [-1, -1]) == 'NO'
    assert intersection([1, 2], [3, 5]) == 'NO'
    assert intersection([1, 2], [1, 2]) == 'NO'
    assert intersection([-2, -2], [-3, -2]) == 'NO'

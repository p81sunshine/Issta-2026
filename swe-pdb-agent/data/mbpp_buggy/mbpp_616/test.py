from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_tuple_modulo_base():
    assert tuple_modulo([10, 4, 5, 6], [5, 6, 7, 5]) == (0, 4, 5, 1)
    assert tuple_modulo([11, 5, 6, 7], [6, 7, 8, 6]) == (5, 5, 6, 1)
    assert tuple_modulo([12, 6, 7, 8], [7, 8, 9, 7]) == (5, 6, 7, 1)

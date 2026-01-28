from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_max_fill_base():
    assert max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5
    assert max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0
    assert max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 2) == 4
    assert max_fill([[1, 1, 1, 1], [1, 1, 1, 1]], 9) == 2

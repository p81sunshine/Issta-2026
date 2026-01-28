from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_Find_Max_base():
    assert Find_Max([['A'], ['A', 'B'], ['A', 'B', 'C']]) == ['A', 'B', 'C']
    assert Find_Max([[1], [1, 2], [1, 2, 3]]) == [1, 2, 3]
    assert Find_Max([[1, 1], [1, 2, 3], [1, 5, 6, 1]]) == [1, 5, 6, 1]

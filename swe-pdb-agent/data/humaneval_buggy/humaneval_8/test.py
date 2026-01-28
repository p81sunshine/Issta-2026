from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_sum_product_base():
    assert sum_product([]) == (0, 1)
    assert sum_product([1, 1, 1]) == (3, 1)
    assert sum_product([100, 0]) == (100, 0)
    assert sum_product([3, 5, 7]) == (15, 105)
    assert sum_product([10]) == (10, 10)

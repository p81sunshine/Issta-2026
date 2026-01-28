from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_multiply_num_base():
    result = multiply_num([8, 2, 3, -1, 7])
    expected = -67.2
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = multiply_num([-10, -20, -30])
    expected = -2000.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)
    result = multiply_num([19, 15, 18])
    expected = 1710.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=0.0001)

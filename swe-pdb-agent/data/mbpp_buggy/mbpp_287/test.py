from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_square_Sum_base():
    result = square_Sum(2)
    expected = 20.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = square_Sum(3)
    expected = 56.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = square_Sum(4)
    expected = 120.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)

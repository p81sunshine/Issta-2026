from solution import *

import math

from solution import *

import math

from solution import *

import math

import numpy as np
def test_sum_base():
    result = sum(10, 15)
    expected = 6.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = sum(100, 150)
    expected = 93.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
    result = sum(4, 6)
    expected = 3.0
    if result == expected:
        assert True
    else:
        assert np.allclose(result, expected, rtol=1e-07, atol=1e-06)
